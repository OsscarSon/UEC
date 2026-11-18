"""Rebuild the authored five-chapter increment and its catalogues in dependency order."""
import subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
for c in range(7,12):subprocess.run(['python',f'data/authoring/chem{c:02}.py'],cwd=R,check=True)
for tool in ['build_base_lessons','build_notes','register_batch04','build_illustration_prompts','build_batch04_reports']:
 subprocess.run(['python',f'tools/{tool}.py'],cwd=R,check=True)
