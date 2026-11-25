"""Recette Chromium headless réelle, locale ; aucun navigateur utilisateur contrôlé."""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import threading,subprocess,json,re,html,time,socket,argparse
from urllib.request import urlopen
parser=argparse.ArgumentParser();parser.add_argument('--suite',default='tools/browser-qa-s19.js');parser.add_argument('--target',default='dist/index.html');parser.add_argument('--report',default='docs/recette-navigateur-S19.json');parser.add_argument('--output',default='tmp/qa-refonte-S19');parser.add_argument('--no-captures',action='store_true');parser.add_argument('--capture-mode',default='atelier');args=parser.parse_args()
R=Path(__file__).resolve().parents[1];T=R/args.output;T.mkdir(parents=True,exist_ok=True)
js=(R/args.suite).read_text(encoding='utf-8')
js=js.replace('})();',"})().finally(()=>fetch('/__qa_complete'));",1)
(T/'qa.html').write_text('<!doctype html><meta charset="utf-8"><title>QA locale en cours</title><iframe style="width:1280px;height:1000px;border:0" src="/'+args.target+'"></iframe><img src="/__qa_hold.gif" alt="" hidden><pre id="results">PENDING</pre><script>'+js+'</script>',encoding='utf-8')
completed=threading.Event()
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
    def do_GET(self):
        if self.path=='/__qa_complete':
            completed.set();self.send_response(200);self.end_headers();self.wfile.write(b'OK');return
        if self.path=='/__qa_hold.gif':
            completed.wait(40);self.send_response(200);self.send_header('Content-Type','image/gif');self.end_headers();self.wfile.write(bytes.fromhex('47494638396101000100800000000000ffffff21f90401000000002c00000000010001000002024401003b'));return
        super().do_GET()
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(R)));thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
chrome=Path('C:/Program Files/Google/Chrome/Application/chrome.exe')
common=[str(chrome),'--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check','--disable-extensions','--disable-background-networking','--disable-component-update','--no-proxy-server','--force-device-scale-factor=1']
try:
    result=subprocess.run(common+['--user-data-dir='+str(T/('profile-'+str(time.time_ns()))),'--dump-dom',f'http://127.0.0.1:{server.server_port}/{T.relative_to(R).as_posix()}/qa.html'],capture_output=True,text=True,encoding='utf-8',timeout=55)
    (T/'chrome-stderr.txt').write_text(result.stderr,encoding='utf-8');(T/'dom.html').write_text(result.stdout,encoding='utf-8')
    match=re.search(r'<pre id="results">(.*?)</pre>',result.stdout,re.S)
    assert match,'Résultats absents ; voir tmp/qa-refonte-S19/chrome-stderr.txt'
    report=json.loads(html.unescape(match.group(1)));(R/args.report).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'status':report['status'],'checks':len(report['results']),'error':report.get('error')},ensure_ascii=False))
    assert report['status']=='passed',report.get('error')
    if args.no_captures:raise SystemExit(0)
    profile=T/('capture-profile-'+str(time.time_ns()))
    with socket.socket()as temporary:
        temporary.bind(('127.0.0.1',0));port=temporary.getsockname()[1]
    with (T/'capture-chrome.log').open('w',encoding='utf-8')as log:
        process=subprocess.Popen(common+['--user-data-dir='+str(profile),'--remote-debugging-port='+str(port),'about:blank'],stdout=log,stderr=log)
        try:
            for _ in range(100):
                try:
                    with urlopen(f'http://127.0.0.1:{port}/json/list',timeout=.2)as response:
                        if response.status==200:break
                except OSError:pass
                time.sleep(.05)
            capture=subprocess.run(['node',str(R/'tools/capture-s19.mjs'),str(port),f'http://127.0.0.1:{server.server_port}',str(T),args.capture_mode],capture_output=True,text=True,encoding='utf-8',timeout=40)
            print(capture.stdout);assert capture.returncode==0,capture.stderr
        finally:
            if process.poll()is None:process.terminate()
finally:server.shutdown();server.server_close();thread.join()
