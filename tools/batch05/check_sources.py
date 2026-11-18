"""Check source HTTP reachability; never call this scientific validation."""
from pathlib import Path
import concurrent.futures,json,urllib.request,urllib.error,urllib.parse
R=Path(__file__).resolve().parents[2];urls=set()
for p in (R/'data/batch05').glob('*-sections.json'):
 for u in json.loads((R/'data/notes'/(p.name.split('-')[0]+'.json')).read_text()).values():
  urls.update(s['url'] for s in u['content_sources'])
def check(url):
 try:
  r=urllib.request.urlopen(urllib.request.Request(urllib.parse.quote(url,safe=':/?&=#%'),method='HEAD'),timeout=12)
  return dict(url=url,http_status=r.status,final_url=r.url,check='HEAD reachability only; no scientific endorsement')
 except urllib.error.HTTPError as e:return dict(url=url,http_status=e.code,error=str(e),check='No authentication or bypass attempted')
 except Exception as e:return dict(url=url,http_status=None,error=str(e),check='Network result does not establish source accuracy')
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(check,sorted(urls)))
out=dict(status='reachability_checked',note='HTTP200仅证明链接可达，不表示逐段内容已核对；403/网络错误不等于原来源不存在。科学内容仍部分核实，见SOURCES.md。',sources=rows)
(R/'reports/batch05/SOURCE_LINK_CHECK.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Checked',len(rows),'unique source URLs')
for x in rows:
 if x['http_status']!=200:print(x['http_status'],x['url'])

