"""Explicit visual transcription ledger. This is authored from rendered PDF pages,
not a heuristic promotion of imported CSV confidence labels. Original PDFs stay private.
"""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2];O=R/'data/math-exams';sources=json.loads((O/'source-inventory.json').read_text());rows=[]
C='';F='';Y=2026

def exam(code,filename):
 global C,F
 C=code;F=next(x['source_id'] for x in sources if x['exam_type']==code and x['filename']==filename)
def q(p,n,sub,page,marks,ch,latex,topic,answer=None,figure='原卷无图；无图形依赖',secondary=None,options=None,note='',difficulty=None):
 rows.append(dict(id=f'{C}:{Y}:{p}:{n}:{sub}',exam_type=C,year=Y,paper=p,question=str(n),subquestion=sub,source_pdf_id=F,source_page=page,printed_marks=marks,primary_chapter=ch,secondary_chapters=secondary or [],subchapter_id=None,formula_latex_verified=latex,figure_description_verified=figure,options_verified=options,answer_verified=answer,answer_status='author_solved_sample_checks_separate' if answer is not None else 'needs_review',verification_status='visual_fields_checked',evidence_fields={k:'visual_pdf_page' for k in ['year','paper','question','subquestion','formula','figure','marks','chapter']},verified_by='Codex visual review of source PDF rendering',verification_method='Read actual page; retain conditions, bounds and figure dependencies; independent calculations are itemized separately.',topic=topic,difficulty=dict(level=difficulty,status='estimated' if difficulty else 'not_estimated',basis='Author estimate from operations, modelling and dependencies; no student response data.'),notes=note,actual_marks=None,effective_marks_model=None,chapter_basis='Teaching classification against original site chapter dictionary; not an official chapter label.'))
def mc(n,page,ch,latex,topic,opts,answer,**kw):q('mcq',n,'whole',page,2,ch,latex,topic,answer,options=dict(zip('ABCD',opts.split('|'))),**kw)
def wr(n,sub,page,marks,ch,latex,topic,answer=None,**kw):q('written',n,sub,page,marks,ch,latex,topic,answer,**kw)
