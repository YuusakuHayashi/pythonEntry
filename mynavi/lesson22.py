import markdown
text ='''
# ウサギについて
全身が柔らかい体毛で覆われている小型獣である
'''

md = markdown.core.Markdown()
body = md.convert(text)

html = '<html lang="ja"><meta charset="utf-8"><body>'
html += body + '</body></html>'

with open('out.html', "w", encoding="utf-8") as wf:
    wf.write(html)
