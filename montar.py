# Gera docs/index.html (GitHub Pages) a partir da fonte do levantamento, que é escrita sem <html>/<head>.
import pathlib, re
fonte = pathlib.Path(r"C:\Users\amara\OneDrive\Documentos\Antigravity\Projeto Regente\datacenter-ia\consolidado\ia-local-ufg.html")
s = fonte.read_text(encoding="utf-8")
s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
head_fim = s.index("</style>") + len("</style>")
desc = "Quanto uma universidade do porte da UFG gastaria em 5 anos para rodar IA própria, comparado com contratar o serviço."
html = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<meta name="description" content="{desc}">\n'
        '<meta property="og:title" content="IA própria na universidade">\n'
        f'<meta property="og:description" content="{desc}">\n'
        + s[:head_fim] + '\n</head>\n<body>\n' + s[head_fim:].strip() + '\n</body>\n</html>\n')
html = html.replace("body{background:var(--bg)", "body{margin:0;background:var(--bg)", 1)
pathlib.Path(__file__).with_name("docs").joinpath("index.html").write_text(html, encoding="utf-8")
print("ok", len(html))
