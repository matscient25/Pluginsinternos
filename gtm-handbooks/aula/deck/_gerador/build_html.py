#!/usr/bin/env python3
"""Monta um HTML único (offline) com o deck: versão curta e completa, navegação por teclado, notas."""
import json, os, re, sys, html

S = os.path.dirname(os.path.abspath(__file__))
CURTA_DIR = os.path.join(S, "deck", "project")
FULL_DIR = os.path.join(S, "deck-completo", "project")
OUT = sys.argv[1]

ICONS = {  # traços simples, 24x24
    "Book": '<path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v17H6.5A2.5 2.5 0 0 0 4 21.5z"/><path d="M4 21.5A2.5 2.5 0 0 1 6.5 19H20v3H6.5"/>',
    "Chart": '<path d="M3 3v18h18"/><rect x="7" y="12" width="3" height="6"/><rect x="12" y="8" width="3" height="10"/><rect x="17" y="5" width="3" height="13"/>',
    "Chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
    "Clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "Lightbulb": '<path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.1V18h6v-1.2c0-.8.4-1.6 1-2.1A7 7 0 0 0 12 2z"/>',
    "Search": '<circle cx="11" cy="11" r="7"/><path d="M21 21l-5-5"/>',
    "Users": '<circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0"/><path d="M16 4a4 4 0 0 1 0 8M22 21a7 7 0 0 0-5-6.7"/>',
    "Verified": '<path d="M12 2l2.4 2.1 3.2-.3.7 3.1 2.8 1.6-1.3 2.9 1.3 2.9-2.8 1.6-.7 3.1-3.2-.3L12 22l-2.4-2.1-3.2.3-.7-3.1-2.8-1.6L4.2 12 2.9 9.1l2.8-1.6.7-3.1 3.2.3z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
}


def style_get(st, prop):
    m = re.search(r'(?:^|;)\s*' + prop + r'\s*:\s*([^;]+)', st)
    return m.group(1).strip() if m else None


def conv(sec):
    def icon(m):
        name, st = m.group(1), m.group(2)
        body = ICONS.get(name, '<circle cx="12" cy="12" r="9"/>')
        return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
                f'stroke-linejoin="round" style="{st};flex:none">{body}</svg>')
    sec = re.sub(r'<x-icon name="([A-Za-z]+)" style="([^"]*)"></x-icon>', icon, sec)

    def shape(m):
        kind, st = m.group(1), m.group(2)
        if kind == "arrow-right":
            col = style_get(st, "background") or "#A0B0E8"
            st2 = re.sub(r'background\s*:[^;]+;?', '', st)
            return (f'<svg viewBox="0 0 44 24" preserveAspectRatio="none" style="{st2};flex:none">'
                    f'<path d="M0 7h26V0l18 12-18 12v-7H0z" fill="{col}"/></svg>')
        return f'<div style="{st};border-radius:50%;flex:none"></div>'
    sec = re.sub(r'<x-shape kind="([a-z-]+)" style="([^"]*)"></x-shape>', shape, sec)
    sec = re.sub(r'(<section [^>]*?) hidden( |>)', r'\1\2', sec)
    m = re.search(r'<aside>(.*?)</aside>', sec, re.S)
    notes = html.unescape(m.group(1)).strip() if m else ""
    sec = re.sub(r'<aside>.*?</aside>', '', sec, flags=re.S)
    return sec, notes


def load(d, only_visible):
    deck = json.load(open(os.path.join(d, "deck.json"), encoding="utf-8"))
    out = []
    for sid in deck["order"]:
        raw = open(os.path.join(d, "slides", sid + ".html"), encoding="utf-8").read()
        if only_visible and re.search(r'<section [^>]*\bhidden\b', raw.split('>')[0] + '>'):
            continue
        sec, notes = conv(raw)
        out.append((sid, sec, notes))
    return out


curta = load(CURTA_DIR, True)
full = load(FULL_DIR, False)


def slides_html(items, mode):
    parts = []
    for i, (sid, sec, notes) in enumerate(items):
        parts.append(f'<div class="slide" data-mode="{mode}" data-i="{i}" data-notes="{html.escape(notes, quote=True)}">{sec}</div>')
    return "\n".join(parts)


page = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Building GTM Handbooks &amp; Skills · SCIENT</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=Lexend:wght@500;600&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box}}
  html,body{{margin:0;height:100%;background:#1B1C20;overflow:hidden;font-family:'Sora',Arial,sans-serif}}
  #viewport{{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}}
  #stage{{width:1920px;height:1080px;position:relative;transform-origin:center center;flex:none;box-shadow:0 20px 60px rgba(0,0,0,.4)}}
  .slide{{display:none;position:absolute;inset:0}}
  .slide.on{{display:block}}
  .slide section{{width:1920px;height:1080px;position:relative;overflow:hidden}}
  .slide p,.slide h1,.slide h2,.slide h3,.slide ul,.slide ol{{margin:0}}
  .slide h1,.slide h2,.slide h3{{font-weight:600}}
  .slide table{{border-collapse:collapse}}
  .slide th,.slide td{{padding:.35em .6em;border-bottom:1px solid #E1E4EC;text-align:left;vertical-align:top}}
  .slide th{{font-weight:600}}
  #bar{{position:fixed;left:50%;bottom:14px;transform:translateX(-50%);display:flex;gap:8px;align-items:center;
        background:rgba(17,17,17,.85);color:#fff;font:500 13px 'Sora',Arial,sans-serif;padding:8px 10px;border-radius:4px;
        transition:opacity .3s;z-index:5}}
  #bar button{{background:transparent;color:#fff;border:1px solid #444;border-radius:4px;padding:6px 10px;font:inherit;cursor:pointer}}
  #bar button:hover{{border-color:#A0B0E8}}
  #bar .mode{{color:#A0B0E8}}
  body.idle #bar{{opacity:0}}
  #notes{{position:fixed;right:16px;top:16px;width:min(460px,40vw);max-height:70vh;overflow:auto;background:#fff;color:#111;
          font:400 15px/1.5 'Sora',Arial,sans-serif;padding:16px 18px;border-radius:4px;display:none;z-index:6;box-shadow:0 10px 30px rgba(0,0,0,.3)}}
  #notes b{{display:block;color:#0030E8;font-size:12px;letter-spacing:.08em;margin-bottom:6px}}
  body.notes #notes{{display:block}}
  @media print{{
    html,body{{background:#fff;overflow:visible;height:auto}}
    #bar,#notes{{display:none!important}}
    #viewport{{position:static;display:block}}
    #stage{{transform:none!important;box-shadow:none;width:1920px;height:auto}}
    .slide{{position:relative;display:none;page-break-after:always;height:1080px}}
    .slide.print{{display:block}}
    @page{{size:1920px 1080px;margin:0}}
  }}
</style>
</head>
<body>
<div id="viewport"><div id="stage">
{slides_html(curta, "curta")}
{slides_html(full, "completa")}
</div></div>
<div id="notes"><b>NOTAS DO APRESENTADOR</b><div id="notes-text"></div></div>
<div id="bar">
  <button id="prev" title="Anterior (←)">←</button>
  <span id="count">1 / 1</span>
  <button id="next" title="Próximo (→)">→</button>
  <button id="mode" title="Alternar versão (C)">Versão: <span class="mode" id="mode-label">curta</span></button>
  <button id="notesbtn" title="Notas (N)">Notas</button>
  <button id="fs" title="Tela cheia (F)">Tela cheia</button>
</div>
<script>
(function(){{
  var mode = 'curta', idx = 0;
  var all = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  function list(){{ return all.filter(function(s){{ return s.dataset.mode === mode; }}); }}
  function fit(){{
    var s = Math.min(window.innerWidth/1920, window.innerHeight/1080);
    document.getElementById('stage').style.transform = 'scale(' + s + ')';
  }}
  function show(){{
    var l = list(); idx = Math.max(0, Math.min(idx, l.length-1));
    all.forEach(function(s){{ s.classList.remove('on'); s.classList.remove('print'); }});
    l.forEach(function(s){{ s.classList.add('print'); }});
    l[idx].classList.add('on');
    document.getElementById('count').textContent = (idx+1) + ' / ' + l.length;
    document.getElementById('mode-label').textContent = mode === 'curta' ? 'curta (aula)' : 'completa';
    document.getElementById('notes-text').textContent = l[idx].dataset.notes || '';
    try {{ history.replaceState(null, '', '#' + mode + '-' + (idx+1)); }} catch(e) {{}}
  }}
  function go(d){{ idx += d; show(); }}
  function toggleMode(){{ mode = mode === 'curta' ? 'completa' : 'curta'; idx = 0; show(); }}
  function fs(){{
    if (!document.fullscreenElement) {{ (document.documentElement.requestFullscreen||function(){{}}).call(document.documentElement); }}
    else {{ document.exitFullscreen(); }}
  }}
  var h = (location.hash||'').match(/^#(curta|completa)-(\\d+)$/);
  if (h) {{ mode = h[1]; idx = parseInt(h[2],10)-1; }}
  document.addEventListener('keydown', function(e){{
    var k = e.key;
    if (k==='ArrowRight'||k===' '||k==='PageDown'||k==='Enter') {{ e.preventDefault(); go(1); }}
    else if (k==='ArrowLeft'||k==='PageUp'||k==='Backspace') {{ e.preventDefault(); go(-1); }}
    else if (k==='Home') {{ idx=0; show(); }}
    else if (k==='End') {{ idx=1e9; show(); }}
    else if (k==='f'||k==='F') fs();
    else if (k==='n'||k==='N') document.body.classList.toggle('notes');
    else if (k==='c'||k==='C') toggleMode();
  }});
  document.getElementById('prev').onclick = function(){{ go(-1); }};
  document.getElementById('next').onclick = function(){{ go(1); }};
  document.getElementById('mode').onclick = toggleMode;
  document.getElementById('notesbtn').onclick = function(){{ document.body.classList.toggle('notes'); }};
  document.getElementById('fs').onclick = fs;
  document.getElementById('viewport').addEventListener('click', function(e){{
    if (e.clientX > window.innerWidth/2) go(1); else go(-1);
  }});
  var t; function wake(){{ document.body.classList.remove('idle'); clearTimeout(t); t = setTimeout(function(){{ document.body.classList.add('idle'); }}, 2500); }}
  document.addEventListener('mousemove', wake); wake();
  window.addEventListener('resize', fit); fit(); show();
}})();
</script>
</body>
</html>
'''
open(OUT, "w", encoding="utf-8").write(page)
print(OUT, len(curta), "curta", len(full), "completa", os.path.getsize(OUT) // 1024, "KB")
