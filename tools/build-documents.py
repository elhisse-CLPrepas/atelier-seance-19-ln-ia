"""Entrée conservée : génère les supports du parcours JSON / HTTP / DOM."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('build-workshop-documents.py')), run_name='__main__')
