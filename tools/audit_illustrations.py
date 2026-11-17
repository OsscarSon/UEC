"""Compatibility entry point for the current audit.
The complete original audit implementation/results are preserved at daa3637.
Current work is authorized to change notes and add deterministic SVGs.
"""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parents[1]/'tests/batch02_audit.py'),run_name='__main__')
