"""Gera o index.html a partir de src/template.html, embutindo imagens e logos.
Uso:  python3 build.py
"""
import json, re, base64, pathlib
ROOT = pathlib.Path(__file__).parent
t = (ROOT / "src/template.html").read_text(encoding="utf-8")
imgs = json.loads((ROOT / "assets/images/produtos.json").read_text())
svg = lambda f: "data:image/svg+xml;base64," + base64.b64encode((ROOT / f).read_bytes()).decode()
t = t.replace("{{LOGO_D}}", svg("assets/logo/logo_dark.svg")).replace("{{LOGO_L}}", svg("assets/logo/logo_light.svg"))
t = re.sub(r"\{\{IMG:(\w+)\}\}", lambda m: imgs[m.group(1)], t)
t = t.replace("{{IMGS_JSON}}", json.dumps({k: v for k, v in imgs.items() if k != "hero"}))
assert "{{" not in t, "placeholder sem substituir"
(ROOT / "index.html").write_text(t, encoding="utf-8")
print("index.html gerado:", len(t) // 1024, "KB")
