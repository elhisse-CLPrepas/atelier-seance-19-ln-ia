"use strict";
const $ = s => document.querySelector(s);
const projectsElement = $('#projects');
let projects = [], generation = 0, controller, currentSource = '';
let lastAction = () => loadProjects();
const normalize = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();
function validateProjects(data) {
  if (!Array.isArray(data)) throw Error('Le JSON doit contenir un tableau.');
  data.forEach((p, i) => {
    if (!p || typeof p !== 'object' || Array.isArray(p) ||
        ['title','category','description'].some(k => typeof p[k] !== 'string' || !p[k].trim()))
      throw Error('Objet ' + (i + 1) + ' : title, category et description doivent être des textes non vides.');
  });
  return data;
}
function setState(message, kind = 'info') {
  $('#status').textContent = message;
  $('#status').classList.toggle('error', kind === 'error');
  $('#status').dataset.state = kind;
  $('#retry-button').hidden = kind !== 'error';
}
function createProjectCard(p) {
  const card = document.createElement('article'); card.className = 'card';
  for (const [tag,key,cls] of [['span','category','tag'],['h3','title',''],['p','description','']]) {
    const node = document.createElement(tag); node.className = cls; node.textContent = p[key]; card.append(node);
  }
  return card;
}
function render() {
  const query = normalize($('#search').value), category = $('#category').value;
  const visible = projects.filter(p => (!category || category === p.category) &&
    normalize(p.title + ' ' + p.category + ' ' + p.description).includes(query));
  projectsElement.replaceChildren(...visible.map(createProjectCard));
  $('#result-count').textContent = visible.length + ' / ' + projects.length + ' projet(s)';
  if (!projects.length) setState('Aucun projet disponible : le tableau est vide.', 'empty');
  else if (!visible.length) setState('Aucun résultat pour ces filtres. Effacez la recherche ou changez de catégorie.', 'empty');
  else setState(visible.length + ' projet(s) affiché(s). Source : ' + currentSource + '.', 'success');
}
function clearFilters() { $('#search').value = ''; $('#category').value = ''; }
function accept(data, source) {
  projects = validateProjects(data); currentSource = source;
  const selected = $('#category').value;
  const all = document.createElement('option'); all.value = ''; all.textContent = 'Toutes les catégories';
  const options = [...new Set(projects.map(p => p.category))].sort().map(c => {
    const o = document.createElement('option'); o.value = c; o.textContent = c; return o;
  });
  $('#category').replaceChildren(all, ...options);
  $('#category').value = options.some(o => o.value === selected) ? selected : '';
  $('#json-preview').textContent = JSON.stringify(projects, null, 2); render();
}
async function execute(task, source) {
  const token = ++generation;
  controller?.abort(); controller = new AbortController();
  const activeController = controller, signal = controller.signal;
  projects = []; projectsElement.replaceChildren();
  $('#result-count').textContent = '…'; $('#json-preview').textContent = 'Chargement en cours…';
  $('#search').disabled = $('#category').disabled = true;
  $('#download-json').disabled = true;
  projectsElement.setAttribute('aria-busy', 'true'); setState('Chargement des projets…', 'loading');
  const timeout = setTimeout(() => activeController.abort(), 10000);
  try {
    const data = await task(signal);
    if (token !== generation) return;
    signal.throwIfAborted();
    accept(data, source); $('#download-json').disabled = false;
  } catch (error) {
    if (token !== generation) return;
    const detail = signal.aborted ? 'Délai de 10 secondes dépassé. Vérifiez le serveur puis réessayez.' :
      error.name === 'SyntaxError' ? 'JSON invalide : vérifiez les guillemets et les virgules.' : error.message;
    setState('Chargement impossible. ' + detail, 'error');
    $('#json-preview').textContent = detail; $('#result-count').textContent = '0 projet';
  } finally {
    clearTimeout(timeout);
    if (token === generation) {
      projectsElement.setAttribute('aria-busy','false');
      $('#search').disabled = $('#category').disabled = false;
    }
  }
}
async function fetchProjects(signal, url = './data/projets.json') {
  const response = await fetch(url, {cache:'no-store', signal});
  if (!response.ok) throw Error('Erreur HTTP ' + response.status + ' : ' + url + '. Vérifiez le chemin.');
  return response.json();
}
function loadProjects() {
  lastAction = () => loadProjects(); $('#scenario').value = 'success';
  if (location.protocol === 'file:') {
    $('#environment').textContent = 'Mode fichier local : exemple intégré en lecture. Pour relire projets.json, démarrez le serveur local ou importez votre fichier.';
    return execute(async () => structuredClone(window.S19_DEMO_DATA), 'exemple intégré, sans requête HTTP');
  }
  $('#environment').textContent = 'Mode serveur : Recharger relit data/projets.json sans cache. Les scénarios ne modifient pas le fichier.';
  return execute(signal => fetchProjects(signal), 'data/projets.json via HTTP');
}
function runScenario() {
  const choice = $('#scenario').value; clearFilters(); lastAction = () => runScenario();
  if (choice === 'success') return loadProjects();
  return execute(async signal => {
    if (choice === 'http') {
      if (location.protocol === 'file:') throw Error('Simulation HTTP 404 : fichier absent. Un vrai test HTTP nécessite le serveur local.');
      return fetchProjects(signal, './data/fichier-manquant.json');
    }
    if (choice === 'slow') await new Promise((resolve,reject) => {
      const timer = setTimeout(resolve,1500);
      signal.addEventListener('abort',() => {clearTimeout(timer); reject(Error('Requête annulée'));},{once:true});
    });
    if (choice === 'empty') return [];
    if (choice === 'invalid') return JSON.parse('{"title":');
    if (choice === 'schema') return [{title:42}];
    return structuredClone(window.S19_DEMO_DATA);
  }, 'simulation pédagogique' + (choice === 'slow' ? ' avec délai de 1,5 s' : ''));
}
$('#reload-button').addEventListener('click',() => {clearFilters(); return loadProjects();});
$('#retry-button').addEventListener('click',() => lastAction());
$('#search').addEventListener('input',render);
$('#category').addEventListener('change',render);
$('#clear-search').addEventListener('click',() => {clearFilters(); if (projectsElement.getAttribute('aria-busy') !== 'true') render(); $('#search').focus();});
$('#run-scenario').addEventListener('click',runScenario);
$('#restore-button').addEventListener('click',() => {clearFilters(); return loadProjects();});
$('#import-json').addEventListener('change',async event => {
  const file = event.target.files[0]; if (!file) return;
  clearFilters();
  const action = () => execute(async () => {
    if (file.size > 1024 * 1024) throw Error('Choisissez un fichier JSON de moins de 1 Mo.');
    return JSON.parse(await file.text());
  }, 'import local : ' + file.name);
  lastAction = action; await action(); event.target.value = '';
});
$('#copy-json').addEventListener('click',async () => {
  try {
    await navigator.clipboard.writeText($('#json-preview').textContent);
    $('#copy-status').textContent = 'Texte copié.';
  } catch {
    const range = document.createRange(); range.selectNodeContents($('#json-preview'));
    const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range);
    $('#copy-status').textContent = 'Copie automatique indisponible. Texte sélectionné : utilisez Ctrl+C ou Copier.';
  }
});
$('#download-json').addEventListener('click',() => {
  const url = URL.createObjectURL(new Blob([JSON.stringify(projects,null,2)],{type:'application/json;charset=utf-8'}));
  const link = document.createElement('a'); link.href = url; link.download = 'projets-export.json'; link.click();
  setTimeout(() => URL.revokeObjectURL(url),1000);
  $('#copy-status').textContent = 'Export JSON demandé : vérifiez vos téléchargements.';
});
loadProjects();
