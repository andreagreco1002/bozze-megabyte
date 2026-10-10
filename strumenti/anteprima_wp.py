"""Anteprima locale del sito nuovo come verrà su WordPress.

Mette insieme intestazione, contenuto di una pagina (gli stessi blocchi che
stanno su WordPress) e piè di pagina, con il foglio di stile nuovo. Serve a
vedere il vestito prima di toccare il sito vero: i blocchi sono commenti HTML,
quindi il browser mostra esattamente quello che mostrerà WordPress.
"""
import json
import os
import re

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WP = os.path.join(RADICE, 'wp')

MENU = [
    ('Riparazioni e assistenza', 'riparazioni', [
        ('Riparazione PC e Mac', 'riparazione-pc-mac'), ('Smartphone e tablet', 'riparazione-smartphone-tablet'),
        ('Recupero dati', 'recupero-dati'), ('Virus e sicurezza', 'virus-sicurezza'),
        ('Assistenza per aziende', 'assistenza-aziende'), ('Assistenza da remoto', 'assistenza-remota')]),
    ('Vendita', 'vendita-e-assemblaggio', [
        ('Computer e accessori', 'vendita'), ('PC assemblati e da gaming', 'pc-gaming'),
        ('Telefonia e internet', 'telefonia-internet')]),
    ('Siti e gestionali', 'siti-e-gestionali', [
        ('Landing page e siti web', 'siti-web'), ('Gestionali su misura', 'gestionali')]),
]


def menu_html():
    voci = ['<li><a href="home-nuova.html">Home</a></li>']
    for nome, pagina, figli in MENU:
        sotto = ''.join(f'<li><a href="{s}.html">{n}</a></li>' for n, s in figli)
        voci.append(f'<li class="ha-sotto"><a href="{pagina}.html">{nome}</a><ul class="sotto">{sotto}</ul></li>')
    voci.append('<li><a href="#recensioni">Recensioni</a></li>')
    voci.append('<li><a href="#contatti">Contatti</a></li>')
    return '<nav class="menu-anteprima"><ul>' + ''.join(voci) + '</ul></nav>'


def parte(nome, sostituzioni):
    testo = open(os.path.join(WP, 'tema', nome), encoding='utf-8').read()
    for cerca, metti in sostituzioni.items():
        testo = testo.replace(cerca, metti)
    return testo


CSS_ANTEPRIMA = """
/* solo per l'anteprima: il menu e il logo che su WordPress mette il tema */
.menu-anteprima ul { list-style: none; display: flex; gap: 22px; margin: 0; padding: 0; justify-content: center; flex-wrap: wrap; }
.menu-anteprima a { color: #fff; font-weight: 600; text-decoration: none; }
.menu-anteprima .ha-sotto { position: relative; }
.menu-anteprima .sotto { display: none; position: absolute; left: 0; top: 100%; background: #fff; border: 1px solid var(--bordo);
  border-radius: 10px; box-shadow: var(--ombra); padding: 6px; min-width: 260px; flex-direction: column; gap: 0; z-index: 10; }
.menu-anteprima .ha-sotto:hover .sotto, .menu-anteprima .ha-sotto:focus-within .sotto { display: flex; }
.menu-anteprima .sotto a { color: var(--testo); display: block; padding: 9px 12px; border-radius: 7px; font-weight: 500; }
.menu-anteprima .sotto a:hover { background: var(--blu-chiaro); }
.logo-anteprima { max-width: 260px; height: auto; display: block; }
.wp-block-group { display: block; }
.barra-contatti .wp-block-group, .intestazione-sito .wp-block-group {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px;
  width: min(100% - 32px, 1140px); margin-inline: auto;
}
.barra-contatti p, .intestazione-sito p { margin: 0; }
.wp-block-buttons { display: flex; gap: 10px; flex-wrap: wrap; }
.pie-sito .wp-block-columns { display: flex; gap: 32px; flex-wrap: wrap; width: min(100% - 32px, 1140px); margin-inline: auto; }
.pie-sito .wp-block-column { flex: 1 1 260px; }
.pie-sito > p { width: min(100% - 32px, 1140px); margin-inline: auto; }
"""


def costruisci(pagina):
    testata = parte('intestazione.html', {
        '<!-- wp:site-logo {"width":260} /-->': '<img class="logo-anteprima" src="../../bozza-a/img/logo.png" alt="Meg@byte Informatica">',
        '<!-- wp:navigation {"ref":0,"overlayMenu":"mobile","layout":{"type":"flex","justifyContent":"center","flexWrap":"wrap"}} /-->': menu_html(),
    })
    piede = parte('pie.html', {})
    stile = open(os.path.join(WP, 'tema', 'stile.css'), encoding='utf-8').read()
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{pagina['titolo']} — anteprima del sito nuovo</title>
<style>
{stile}
{CSS_ANTEPRIMA}
</style>
</head>
<body>
{testata}
<main class="pagina-contenuto">
<h1>{pagina['titolo']}</h1>
{pagina['blocchi'].replace('%%FOTO%%', '')}
</main>
{piede}
</body>
</html>
"""


if __name__ == '__main__':
    dati = json.load(open(os.path.join(WP, 'pagine.json'), encoding='utf-8'))
    cartella = os.path.join(WP, 'anteprima')
    os.makedirs(cartella, exist_ok=True)
    for p in dati['pagine']:
        html = costruisci(p)
        # nell'anteprima le foto stanno accanto alle bozze
        html = html.replace('src="https://andreagreco1002.github.io/bozze-megabyte/bozza-a/img/foto/',
                            'src="../../bozza-a/img/foto/')
        with open(os.path.join(cartella, p['slug'] + '.html'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(html)
    print(f"{len(dati['pagine'])} anteprime in {cartella}")
