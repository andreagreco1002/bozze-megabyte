"""
Genera le due bozze del sito dai contenuti in contenuti.py.

  bozza-a/  ispirata all'impostazione di SoccorsoPc (home piu' d'impatto)
  bozza-b/  la bozza che stavamo facendo, con le pagine di dettaglio
  index.html  pagina di scelta fra le due

Uso:  python strumenti/genera.py
"""
import html
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
from contenuti import (EMAIL, INDIRIZZO, MAPPA, MARCHE, ORARI, PER_SLUG, PROBLEMI, RECENSIONI,  # noqa: E402
                       SCRIVI_RECENSIONE, SERVIZI, TEL_LINK, TELEFONO, WHATSAPP)

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRUMENTI = os.path.join(RADICE, 'strumenti')
A = os.path.join(RADICE, 'bozza-a')
B = os.path.join(RADICE, 'bozza-b')

ICONE = {
    'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    'chat': '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
    'pin': '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    'clock': '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    'mail': '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    'laptop': '<path d="M20 16V7a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9m16 0H4m16 0 1.28 2.55a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45L4 16"/>',
    'smartphone': '<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>',
    'database': '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/>',
    'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/>',
    'building': '<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4"/><path d="M10 10h4"/><path d="M10 14h4"/><path d="M10 18h4"/>',
    'monitor': '<rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/>',
    'bag': '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/>',
    'wifi': '<path d="M5 13a10 10 0 0 1 14 0"/><path d="M8.5 16.5a5 5 0 0 1 7 0"/><path d="M2 8.82a15 15 0 0 1 20 0"/><line x1="12" x2="12.01" y1="20" y2="20"/>',
    'arrow': '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    'menu': '<line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="18" y2="18"/>',
    'layout': '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/>',
    'dashboard': '<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
    'file': '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    'zap': '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    'search': '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    'star': '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    'check': '<path d="M20 6 9 17l-5-5"/>',
    'alert': '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    'chevron': '<path d="m6 9 6 6 6-6"/>',
    'home': '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    'award': '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>',
    'tool': '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
}

# Foto delle pagine (solo bozza A): in img/foto, da Pexels, licenza libera anche
# per uso commerciale. Le sostituiremo con le foto vere del negozio.
FOTO = {
    'riparazione-pc-mac': 'Computer portatile aperto sul banco con i componenti a vista durante la riparazione',
    'riparazione-smartphone-tablet': 'Sostituzione di un componente interno di uno smartphone',
    'recupero-dati': 'Hard disk aperto, con disco e testina in vista',
    'virus-sicurezza': 'Schermo con righe di codice durante un controllo di sicurezza',
    'assistenza-aziende': 'Pannello di rete con i cavi ordinati',
    'assistenza-remota': 'Tecnico al computer durante un collegamento da remoto',
    'vendita': 'Computer portatili esposti in un negozio di informatica',
    'telefonia-internet': 'Router Wi-Fi con le antenne',
    'siti-web': 'Scrivania con computer portatile e tavoletta grafica',
    'gestionali': 'Tablet che mostra un pannello con grafici e statistiche',
    'app': 'Mano che tiene uno smartphone davanti a un computer',
    'automazioni': 'Armadio di rete con le luci accese',
    'documenti-pdf': 'Stampante con i fogli appena stampati',
    'visibilita-google': 'Mano che tiene uno smartphone con una mappa aperta',
}

RIPARAZIONI = [s for s in SERVIZI if s['gruppo'] == 'riparazioni']
# Bozza A: ogni gruppo ha una pagina riassuntiva, cosi' la home non ripete le liste del menu
PANORAMICA_A = {'riparazioni': 'riparazioni.html', 'su-misura': 'siti-e-gestionali.html'}
SU_MISURA = [s for s in SERVIZI if s['gruppo'] == 'su-misura']
FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Poppins:wght@600;700&amp;display=swap" rel="stylesheet">')


# ---------------------------------------------------------------- utilita'
def t(testo):
    """Testo sicuro per l'HTML, con le parti [[da confermare]] evidenziate."""
    sicuro = html.escape(testo, quote=False)
    return re.sub(r'\[\[(.+?)\]\]', r'<mark class="da-confermare">\1</mark>', sicuro)


def pulito(testo):
    return re.sub(r'\[\[(.+?)\]\]', r'\1', testo)


def ic(nome, classe='ic'):
    return f'<svg class="{classe}" aria-hidden="true"><use href="#i-{nome}"/></svg>'


def sprite():
    simboli = '\n'.join(f'    <symbol id="i-{n}" viewBox="0 0 24 24">{p}</symbol>' for n, p in ICONE.items())
    return ('<!-- Icone (Lucide): un solo blocco, richiamato con <use> -->\n'
            '<svg width="0" height="0" style="position:absolute" aria-hidden="true">\n  <defs>\n'
            f'{simboli}\n  </defs>\n</svg>')


def whatsapp(messaggio=None):
    if not messaggio:
        return WHATSAPP
    from urllib.parse import quote
    return f'{WHATSAPP}?text={quote(messaggio)}'


def stelle():
    return '<span class="stelle" aria-hidden="true">' + ic('star') * 5 + '</span>'


def orari_dl():
    righe = ''.join(
        f'<dt>{g}</dt><dd>{"".join(f"<span>{o}</span> " for o in ore).strip()}</dd>' for g, ore in ORARI)
    return f'<dl class="orari">{righe}</dl>'


def testa(titolo, descrizione, css):
    fogli = '\n'.join(f'  <link rel="stylesheet" href="{c}">' for c in css)
    return f'''<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>{html.escape(titolo)}</title>
  <meta name="description" content="{html.escape(descrizione)}">
  {FONT}
{fogli}
</head>
<body>

{sprite()}

<a class="salta" href="#contenuto">Vai al contenuto</a>

<!-- Solo nella bozza: non va copiato in WordPress -->
<div class="avviso-bozza" role="note">
  <strong>Bozza.</strong> I testi <mark class="da-confermare">evidenziati così</mark> sono da confermare; i riquadri tratteggiati sono foto da scattare.
</div>
'''


CHIUDI_MENU = '''<script>
  // Sul telefono il menu si richiude dopo aver scelto una voce
  document.querySelectorAll('details.menu-mobile a, details.a-menu-mobile a').forEach((a) =>
    a.addEventListener('click', () => a.closest('details.menu-mobile, details.a-menu-mobile').removeAttribute('open'))
  );
  // Bozza A: aprendo il menu (o un suo gruppo) la barra sale in cima, cosi' il pannello ha tutto lo schermo
  const menuA = document.querySelector('details.a-menu-mobile');
  if (menuA) {
    const inCima = (d) => {
      if (!d.open) return;
      const alto = menuA.closest('.a-menu').getBoundingClientRect().top;
      if (alto > 1) window.scrollTo({ top: window.scrollY + alto, behavior: 'instant' });
    };
    [menuA, ...menuA.querySelectorAll('details')].forEach((d) => d.addEventListener('toggle', () => inCima(d)));
  }
</script>'''


# ---------------------------------------------------------------- corpo delle pagine di dettaglio
def corpo_pagina(s, veste):
    gruppo = 'Riparazioni e assistenza' if s['gruppo'] == 'riparazioni' else 'Siti e gestionali'
    ancora = 'servizi' if s['gruppo'] == 'riparazioni' else 'su-misura'
    msg = f"Buongiorno, vi scrivo per: {s['nome']}"
    nota = ('\n      <p class="nota-bozza">Servizio proposto: da confermare prima di pubblicarlo.</p>'
            if s.get('da_confermare') else '')
    if s.get('prezzi'):
        destra = '<div class="prezzi prezzi--pagina">' + ''.join(
            f'<div class="prezzo"><h3>{d}</h3><p class="prezzo__cifra">{t(p)}</p></div>' for d, p in s['prezzi']
        ) + '</div>'
    elif veste == 'a' and s['slug'] in FOTO:
        destra = (f'<figure class="foto foto--pagina"><img src="img/foto/{s["slug"]}.jpg" alt="{FOTO[s["slug"]]}" '
                  f'width="1200" height="800" loading="lazy"></figure>')
    else:
        destra = (f'<div class="foto-da-fare foto-da-fare--pagina" role="img" aria-label="Spazio per una foto">'
                  f'<span>Foto: {html.escape(pulito(s["nome"]))}<br><small>una foto vera del lavoro</small></span></div>')

    avviso = ''
    if s.get('avviso'):
        tit, testo = s['avviso']
        avviso = f'''
  <section class="sezione sezione--avviso" aria-label="Avviso">
    <div class="contenitore">
      <div class="avviso">
        {ic('alert')}
        <div><h2>{t(tit)}</h2><p>{t(testo)}</p></div>
      </div>
    </div>
  </section>
'''
    esempio = ''
    if s.get('esempio'):
        esempio = '''
      <div class="esempio-chiaro">
        <p class="esempio__titolo">Un esempio? Il gestionale del nostro negozio l'abbiamo fatto noi.</p>
        <p>Schede di assistenza numerate con il QR per le recensioni, preventivi, fatture e DDT, scontrini su carta termica e cartellini per la vetrina: tutto nello stesso programma.</p>
      </div>'''

    cosa = ''.join(f'<li>{ic("check")}<span>{t(c)}</span></li>' for c in s['cosa'])
    passi = ''.join(
        f'<li><span class="passi__numero" aria-hidden="true">{i}</span><h3>{t(a)}</h3><p>{t(b)}</p></li>'
        for i, (a, b) in enumerate(s['passi'], 1))
    faq = ''.join(
        f'<details><summary>{t(d)} {ic("chevron")}</summary><p>{t(r)}</p></details>' for d, r in s['faq'])
    correlati = ''.join(scheda_link(PER_SLUG[c], veste) for c in s['correlati'])
    titolo_cosa = 'Cosa facciamo' if s['gruppo'] == 'riparazioni' else 'Cosa possiamo realizzare'
    titolo_invito = 'Hai bisogno di aiuto?' if s['gruppo'] == 'riparazioni' else 'Raccontaci il tuo progetto'

    return f'''
<main id="contenuto">

  <section class="pagina-eroe">
    <div class="contenitore">
      <nav class="briciole" aria-label="Sei qui">
        <ol>
          <li><a href="index.html">Home</a></li>
          <li><a href="{PANORAMICA_A[s['gruppo']] if veste == 'a' else f'index.html#{ancora}'}">{gruppo}</a></li>
          <li aria-current="page">{t(s['nome'])}</li>
        </ol>
      </nav>{nota}
      <div class="pagina-eroe__griglia">
        <div>
          {ic(s['icona'], 'ic pagina-eroe__icona')}
          <h1>{t(s['titolo'])}</h1>
          <p class="pagina-eroe__sotto">{t(s['sotto'])}</p>
          <p class="pagina-eroe__intro">{t(s['intro'])}</p>
          <div class="azioni">
            <a class="bottone bottone--primario bottone--grande" href="{TEL_LINK}">{ic('phone')} Chiama ora</a>
            <a class="bottone bottone--secondario bottone--grande" href="{whatsapp(msg)}" rel="noopener">{ic('chat')} Scrivici su WhatsApp</a>
          </div>
        </div>
        {destra}
      </div>
    </div>
  </section>
{avviso}
  <section class="sezione" aria-labelledby="titolo-cosa">
    <div class="contenitore">
      <h2 id="titolo-cosa">{titolo_cosa}</h2>
      <ul class="lista-spunte">{cosa}</ul>{esempio}
    </div>
  </section>

  <section class="sezione sezione--tinta{' a-passi' if veste == 'a' else ''}" aria-labelledby="titolo-passi">
    <div class="contenitore">
      <h2 id="titolo-passi">Come funziona</h2>
      <ol class="passi">{passi}</ol>
    </div>
  </section>

  <section class="sezione" aria-labelledby="titolo-faq">
    <div class="contenitore">
      <h2 id="titolo-faq">Domande frequenti</h2>
      <div class="faq">{faq}</div>
    </div>
  </section>

  <section class="sezione sezione--tinta" aria-labelledby="titolo-correlati">
    <div class="contenitore">
      <h2 id="titolo-correlati">Ti potrebbe interessare anche</h2>
      <p class="sezione__intro">Altri servizi di Meg@byte Informatica.</p>
      <ul class="correlati">{correlati}</ul>
    </div>
  </section>

  <section class="invito" aria-labelledby="titolo-invito">
    <div class="contenitore">
      <h2 id="titolo-invito">{titolo_invito}</h2>
      <p>Chiamaci o scrivici su WhatsApp: ti rispondiamo noi, non un call center. Oppure passa a trovarci in Via Tripoli 17, a Roma.</p>
      <div class="azioni">
        <a class="bottone bottone--primario bottone--grande" href="{TEL_LINK}">{ic('phone')} {TELEFONO}</a>
        <a class="bottone bottone--secondario bottone--grande" href="{whatsapp(msg)}" rel="noopener">{ic('chat')} WhatsApp</a>
      </div>
      <p class="invito__orari">Lunedì – Venerdì 9:00–13:00 e 15:30–19:30 · Sabato 9:00–13:00</p>
    </div>
  </section>

</main>
'''


def scheda_link(s, veste):
    """Scheda cliccabile di un servizio: nelle home e fra i correlati."""
    if veste == 'a':
        return (f'<li class="a-servizio"><a class="scheda-link" href="{s["slug"]}.html">'
                f'{ic(s["icona"], "ic a-servizio__icona")}<h3>{t(s["nome"])}</h3><p>{t(s["breve"])}</p>'
                f'<span class="scheda-link__altro">Scopri di più {ic("arrow")}</span></a></li>')
    return (f'<li class="scheda-servizio"><a class="scheda-link" href="{s["slug"]}.html">'
            f'{ic(s["icona"], "ic ic--servizio")}<h3>{t(s["nome"])}</h3><p>{t(s["breve"])}</p>'
            f'<span class="scheda-link__altro">Scopri di più {ic("arrow")}</span></a></li>')


# ---------------------------------------------------------------- veste B: testata e piede
def testata_b(home=False):
    p = '' if home else 'index.html'
    voci = [('servizi', 'Servizi'), ('come-funziona', 'Come funziona'), ('remoto', 'Assistenza remota'),
            ('su-misura', 'Siti e gestionali'), ('recensioni', 'Recensioni'), ('contatti', 'Contatti')]
    lista = '\n'.join(f'        <li><a href="{p}#{a}">{n}</a></li>' for a, n in voci)
    return f'''
<div class="barra-offerte">
  Offerte <strong>Iliad</strong> e <strong>Fastweb</strong>: chiedi in negozio
</div>

<header class="testata">
  <div class="contenitore testata__riga">
    <a class="testata__logo" href="index.html" aria-label="Meg@byte Informatica, torna alla home">
      <img src="img/logo.png" alt="Meg@byte Informatica" width="1200" height="294">
    </a>
    <nav class="menu" aria-label="Menu principale">
      <ul>
{lista}
      </ul>
    </nav>
    <a class="bottone bottone--primario testata__chiama" href="{TEL_LINK}">{ic('phone')} {TELEFONO}</a>
    <details class="menu-mobile">
      <summary aria-label="Apri il menu">{ic('menu')}</summary>
      <ul>
{lista}
      </ul>
    </details>
  </div>
</header>
'''


def piede_b():
    return f'''
<footer class="piede">
  <div class="contenitore piede__griglia">
    <div>
      <img class="piede__logo" src="img/logo.png" alt="Meg@byte Informatica" width="1200" height="294" loading="lazy">
      <p>Assistenza specializzata in ambienti Windows, Mac e Linux · Vendita computer e periferiche · Telefonia fissa e mobile · Siti e software su misura</p>
    </div>
    <div class="piede__dati">
      <p><strong>MEG@BYTE INFORMATICA S.R.L.</strong></p>
      <p>{INDIRIZZO}</p>
      <p>Partita IVA 06455961000 · REA RM-969038</p>
      <p><a href="#">Privacy</a> · <a href="#">Cookie</a></p>
    </div>
  </div>
</footer>

<nav class="barra-contatti" aria-label="Contatti rapidi">
  <a href="{TEL_LINK}">{ic('phone')} Chiama</a>
  <a href="{WHATSAPP}" rel="noopener">{ic('chat')} WhatsApp</a>
</nav>

{CHIUDI_MENU}

</body>
</html>
'''


# ---------------------------------------------------------------- veste A: testata e piede
def testata_a():
    rip = ''.join(f'<li><a href="{s["slug"]}.html">{ic(s["icona"])} {t(s["nome"])}</a></li>' for s in RIPARAZIONI)
    mis = ''.join(f'<li><a href="{s["slug"]}.html">{ic(s["icona"])} {t(s["nome"])}</a></li>' for s in SU_MISURA)
    rip_m = ''.join(f'<li><a href="{s["slug"]}.html">{t(s["nome"])}</a></li>' for s in RIPARAZIONI)
    mis_m = ''.join(f'<li><a href="{s["slug"]}.html">{t(s["nome"])}</a></li>' for s in SU_MISURA)
    return f'''
<div class="a-topbar">
  <div class="contenitore a-topbar__riga">
    <span>{ic('pin')} {INDIRIZZO}</span>
    <span>{ic('clock')} Lun–Ven 9–13 · 15:30–19:30 · Sab 9–13</span>
    <span class="a-topbar__email">{ic('mail')} <a href="mailto:{EMAIL}">{EMAIL}</a></span>
  </div>
</div>

<header class="a-testata">
  <div class="contenitore a-testata__riga">
    <p class="a-slogan">Assistenza informatica a Roma<br><strong>da oltre 20 anni</strong></p>
    <a class="a-logo" href="index.html" aria-label="Meg@byte Informatica, torna alla home">
      <img src="img/logo.png" alt="Meg@byte Informatica" width="1200" height="294">
    </a>
    <div class="a-contatti">
      <a class="bottone bottone--primario" href="{TEL_LINK}">{ic('phone')} {TELEFONO}</a>
      <a class="bottone bottone--whatsapp" href="{WHATSAPP}" rel="noopener">{ic('chat')} WhatsApp</a>
    </div>
  </div>
</header>

<nav class="a-menu" aria-label="Menu principale">
  <div class="contenitore">
    <ul class="a-menu__lista">
      <li><a href="index.html"><span>Home</span><small>Meg@byte Informatica</small></a></li>
      <li class="a-menu__tendina">
        <a href="riparazioni.html"><span>Riparazioni {ic('chevron')}</span><small>PC, Mac, smartphone</small></a>
        <ul class="a-sottomenu">{rip}</ul>
      </li>
      <li class="a-menu__tendina">
        <a href="siti-e-gestionali.html"><span>Siti e gestionali {ic('chevron')}</span><small>su misura per te</small></a>
        <ul class="a-sottomenu">{mis}</ul>
      </li>
      <li><a href="index.html#recensioni"><span>Recensioni</span><small>5 stelle su Google</small></a></li>
      <li><a href="index.html#contatti"><span>Contatti</span><small>orari e dove siamo</small></a></li>
    </ul>
    <details class="a-menu-mobile">
      <summary>{ic('menu')} MENU</summary>
      <ul class="a-menu-mobile__pannello">
        <li><a href="index.html">Home</a></li>
        <li>
          <details class="a-gruppo">
            <summary>Riparazioni e assistenza {ic('chevron')}</summary>
            <ul><li><a href="riparazioni.html">Tutti i servizi</a></li>{rip_m}</ul>
          </details>
        </li>
        <li>
          <details class="a-gruppo">
            <summary>Siti e gestionali {ic('chevron')}</summary>
            <ul><li><a href="siti-e-gestionali.html">Tutti i servizi su misura</a></li>{mis_m}</ul>
          </details>
        </li>
        <li><a href="index.html#recensioni">Recensioni</a></li>
        <li><a href="index.html#contatti">Contatti</a></li>
      </ul>
    </details>
  </div>
</nav>
'''


def piede_a():
    return f'''
<footer class="a-piede">
  <div class="contenitore a-piede__griglia">
    <div>
      <img class="a-piede__logo" src="img/logo.png" alt="Meg@byte Informatica" width="1200" height="294" loading="lazy">
      <p>Assistenza specializzata in ambienti Windows, Mac e Linux, vendita di computer e periferiche, telefonia fissa e mobile, siti e software su misura. A Roma da oltre 20 anni.</p>
    </div>
    <div>
      <h3>Meg@byte</h3>
      <ul>
        <li><a href="riparazioni.html">Riparazioni e assistenza</a></li>
        <li><a href="siti-e-gestionali.html">Siti e gestionali</a></li>
        <li><a href="index.html#recensioni">Recensioni</a></li>
        <li><a href="index.html#contatti">Dove siamo</a></li>
      </ul>
    </div>
    <div>
      <h3>Orari</h3>
      <ul>
        <li>Lunedì – Venerdì<br>9:00–13:00 · 15:30–19:30</li>
        <li>Sabato 9:00–13:00</li>
        <li>Domenica chiuso</li>
      </ul>
    </div>
    <div>
      <h3>Contatti</h3>
      <ul>
        <li>{INDIRIZZO}</li>
        <li><a href="{TEL_LINK}">{TELEFONO}</a> (anche WhatsApp)</li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      </ul>
    </div>
  </div>
  <div class="contenitore a-piede__fondo">
    <span>MEG@BYTE INFORMATICA S.R.L. · Partita IVA 06455961000 · REA RM-969038</span>
    <span><a href="#">Privacy</a> · <a href="#">Cookie</a></span>
  </div>
</footer>

<a class="a-whatsapp" href="{WHATSAPP}" rel="noopener" aria-label="Scrivici su WhatsApp">{ic('chat')}</a>

{CHIUDI_MENU}

</body>
</html>
'''


GIOSTRA = """
<script>
  // Recensioni a 5 stelle che scorrono da sole. In WordPress i dati arrivano dal
  // riquadro Google (le nuove si aggiungono da sole); qui da recensioni.json.
  (async () => {
    const giostra = document.getElementById('giostra-recensioni');
    if (!giostra) return;
    const nastro = giostra.querySelector('.giostra__nastro');
    let recensioni = [];
    try {
      const risposta = await fetch(giostra.dataset.sorgente);
      recensioni = (await risposta.json()).filter((r) => r.stelle === 5);
    } catch {
      return; // aperta da file senza server: si resta senza recensioni
    }
    if (!recensioni.length) return;

    const scheda = (r) => {
      const el = document.createElement('article');
      el.className = 'recensione';
      el.setAttribute('role', 'listitem');
      el.innerHTML =
        '<div class="recensione__testa"><span class="recensione__iniziale"></span>' +
        '<div><strong></strong><span class="recensione__quando"></span></div></div>' +
        '<div class="stelle" aria-label="5 stelle su 5">' + '\u2605'.repeat(5) + '</div><p></p>';
      el.querySelector('.recensione__iniziale').textContent = r.nome.trim().charAt(0).toUpperCase();
      el.querySelector('strong').textContent = r.nome;
      el.querySelector('.recensione__quando').textContent = r.quando;
      el.querySelector('p').textContent = r.testo;
      return el;
    };

    // Doppia copia: quando la prima finisce, la seconda e' gia' al suo posto
    for (let giro = 0; giro < 2; giro++) recensioni.forEach((r) => nastro.appendChild(scheda(r)));
    nastro.style.setProperty('--quante', recensioni.length);
    giostra.classList.add('giostra--pronta');
  })();
</script>
"""


# ---------------------------------------------------------------- home della bozza A
def home_a():
    problemi = ''.join(
        f'<li><a href="{slug}.html">{ic(icona)}<span>{testo}</span><small>Ti aiutiamo noi {ic("arrow")}</small></a></li>'
        for testo, slug, icona in PROBLEMI)
    marche = ''.join(f'<li>{m}</li>' for m in MARCHE)
    perche = ''.join(f'<li>{ic("check")}<span>{x}</span></li>' for x in [
        'Ti spieghiamo il problema con parole semplici, prima di fare qualsiasi cosa',
        'Parti originali per smartphone e tablet',
        'In negozio, a domicilio e da remoto',
        'Un punto di riferimento a Roma da oltre 20 anni',
    ])
    passi = ''.join(
        f'<li><span class="passi__numero" aria-hidden="true">{i}</span><h3>{a}</h3><p>{t(b)}</p></li>'
        for i, (a, b) in enumerate(PER_SLUG['riparazione-pc-mac']['passi'], 1))

    return testa('Riparazione PC, Mac e smartphone a Roma | Meg@byte Informatica',
                 'Riparazione e assistenza PC, Mac, Linux e smartphone a Roma, in Via Tripoli 17. Recupero dati, virus, '
                 'assistenza aziende e da remoto, siti e gestionali su misura. Da oltre 20 anni.',
                 ['stile-a.css']) + testata_a() + f'''
<main id="contenuto">

  <!-- 1. Grande apertura con i problemi piu' comuni, cliccabili -->
  <section class="a-eroe">
    <div class="contenitore">
      <p><a class="a-eroe__occhiello" href="{MAPPA}" rel="noopener" title="Apri in Google Maps">{ic('pin')} Roma, Via Tripoli 17 · il negozio di fiducia sotto casa {ic('arrow', 'ic a-eroe__freccia')}</a></p>
      <h1>Problemi con il PC<br>o lo <em>smartphone</em>?</h1>
      <p class="a-eroe__sotto">Ripariamo computer, Mac, smartphone e tablet di tutte le marche, in negozio, a domicilio o da remoto. Qual è il problema?</p>
      <ul class="a-problemi">{problemi}</ul>
      <div class="azioni">
        <a class="bottone bottone--primario bottone--grande" href="{TEL_LINK}">{ic('phone')} Chiama ora · {TELEFONO}</a>
        <a class="bottone bottone--secondario bottone--grande" href="{WHATSAPP}" rel="noopener">{ic('chat')} Contattaci senza impegno</a>
      </div>
    </div>
  </section>

  <!-- 2. Punti di forza -->
  <section class="a-fiducia" aria-label="Perché fidarti">
    <div class="contenitore">
      <ul>
        <li>{ic('award')}<div><strong>Da oltre 20 anni</strong><span>a Roma, in Via Tripoli</span></div></li>
        <li>{ic('star')}<div><strong>{stelle()}</strong><span>5 stelle su Google · 66 recensioni</span></div></li>
        <li>{ic('laptop')}<div><strong>Windows · Mac · Linux</strong><span>computer e smartphone di tutte le marche</span></div></li>
        <li>{ic('home')}<div><strong>Dove ti serve</strong><span>in negozio, a domicilio e da remoto</span></div></li>
      </ul>
    </div>
  </section>

  <!-- 3. Le due anime del negozio: l'elenco completo sta nel menu e nelle pagine riassuntive -->
  <section class="sezione" id="servizi" aria-labelledby="titolo-servizi">
    <div class="contenitore">
      <h2 id="titolo-servizi">Cosa facciamo</h2>
      <p class="sezione__intro">Due mestieri, una sola squadra: ripariamo i tuoi dispositivi e costruiamo gli strumenti digitali della tua attività.</p>
      <div class="a-mondi">
        <a class="a-mondo" href="riparazioni.html">
          {ic('tool', 'ic a-mondo__icona')}
          <h3>Riparazioni e assistenza</h3>
          <p>Computer, Mac, smartphone e tablet di tutte le marche. In negozio, a domicilio e da remoto, per privati e aziende.</p>
          <span class="a-mondo__altro">Vedi tutti i servizi {ic('arrow')}</span>
        </a>
        <a class="a-mondo a-mondo--scuro" href="siti-e-gestionali.html">
          {ic('dashboard', 'ic a-mondo__icona')}
          <h3>Siti, gestionali e software su misura</h3>
          <p>Pensati per il tuo modo di lavorare. Un esempio? Il gestionale del nostro negozio l'abbiamo fatto noi.</p>
          <span class="a-mondo__altro">Scopri cosa possiamo realizzare {ic('arrow')}</span>
        </a>
      </div>
    </div>
  </section>

  <!-- 4. Perche' sceglierci e marche -->
  <section class="sezione sezione--tinta" aria-labelledby="titolo-perche">
    <div class="contenitore">
      <div class="a-perche">
        <div>
          <h2 id="titolo-perche">Perché sceglierci</h2>
          <ul class="lista-spunte">{perche}</ul>
        </div>
        <figure class="foto foto--perche">
          <img src="img/foto/banco.jpg" alt="Mani al lavoro su un computer portatile aperto, viste dall'alto" width="1200" height="900" loading="lazy">
        </figure>
      </div>
      <div class="a-marche">
        <p>Ripariamo tutte le marche, tra cui</p>
        <ul>{marche}</ul>
      </div>
    </div>
  </section>

  <!-- 5. Come funziona -->
  <section class="sezione a-passi" id="come-funziona" aria-labelledby="titolo-passi">
    <div class="contenitore">
      <h2 id="titolo-passi">Come funziona una riparazione</h2>
      <ol class="passi">{passi}</ol>
    </div>
  </section>

  <!-- 7. Recensioni -->
  <section class="sezione" id="recensioni" aria-labelledby="titolo-recensioni">
    <div class="contenitore">
      <h2 id="titolo-recensioni">Cosa dicono i nostri clienti</h2>
      <p class="sezione__intro">Le recensioni vere, lasciate su Google da chi è passato in negozio.</p>
      <div class="a-recensioni">
        <div class="a-voto">
          {stelle()}
          <strong>5 stelle</strong>
          <span>66 recensioni su Google</span>
          <a class="bottone bottone--primario" href="{RECENSIONI}" rel="noopener">Leggile tutte {ic('arrow')}</a>
          <a class="bottone bottone--su-scuro" href="{SCRIVI_RECENSIONE}" rel="noopener">Lascia una recensione</a>
        </div>
        <!-- Scorrono da sole; si fermano passandoci sopra o toccandole -->
        <div class="giostra" id="giostra-recensioni" data-sorgente="recensioni.json">
          <div class="giostra__nastro" role="list"></div>
        </div>
      </div>
      <p class="nota-bozza">Qui sono esempi: in WordPress scorrono le recensioni vere da Google, solo quelle da 5 stelle, e quelle nuove si aggiungono da sole.</p>
    </div>
  </section>

  <!-- 8. Invito e contatti -->
  <section class="a-banda-cta" aria-labelledby="titolo-cta">
    <div class="contenitore a-banda-cta__riga">
      <div>
        <h2 id="titolo-cta">Hai un problema adesso?</h2>
        <p>Chiamaci o scrivici: ti diciamo subito se e come possiamo aiutarti.</p>
      </div>
      <div class="azioni">
        <a class="bottone bottone--chiaro bottone--grande" href="{TEL_LINK}">{ic('phone')} {TELEFONO}</a>
        <a class="bottone bottone--su-arancio bottone--grande" href="{WHATSAPP}" rel="noopener">{ic('chat')} WhatsApp</a>
      </div>
    </div>
  </section>

  <section class="sezione" id="contatti" aria-labelledby="titolo-contatti">
    <div class="contenitore contatti">
      <div>
        <h2 id="titolo-contatti">Vieni a trovarci</h2>
        <ul class="contatti__lista">
          <li>{ic('pin')}<span>{INDIRIZZO}</span></li>
          <li>{ic('clock')}{orari_dl()}</li>
          <li>{ic('phone')}<a href="{TEL_LINK}">{TELEFONO}</a> <span class="piccolo">(anche WhatsApp)</span></li>
          <li>{ic('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
        <div class="azioni">
          <a class="bottone bottone--primario" href="{MAPPA}" rel="noopener">{ic('pin')} Apri in Google Maps</a>
        </div>
      </div>
      <div class="foto-da-fare foto-da-fare--contatti" role="img" aria-label="Spazio per la foto dell'ingresso">
        <span>Foto dell'ingresso dalla strada<br><small>così ci si riconosce arrivando</small></span>
      </div>
    </div>
  </section>

</main>
''' + piede_a()


# ---------------------------------------------------------------- bozza A: pagine riassuntive
def panoramica_a(gruppo):
    if gruppo == 'riparazioni':
        servizi, titolo, sotto = RIPARAZIONI, 'Riparazioni e assistenza a Roma', 'Tutti i servizi del negozio'
        intro = ("Ripariamo computer, Mac, smartphone e tablet di tutte le marche, per privati e aziende: "
                 "nel nostro negozio di Via Tripoli 17, a domicilio o da remoto.")
        icona, passi, titolo_passi = 'tool', PER_SLUG['riparazione-pc-mac']['passi'], 'Come funziona una riparazione'
        chiusura = ''
    else:
        servizi, titolo, sotto = SU_MISURA, 'Siti, gestionali e software su misura', 'Gli strumenti digitali della tua attività'
        intro = ("Progettiamo e sviluppiamo siti, gestionali e app partendo da come lavori tu, "
                 "e restiamo il tuo punto di riferimento anche dopo.")
        icona, passi, titolo_passi = 'dashboard', PER_SLUG['gestionali']['passi'], 'Come lavoriamo'
        chiusura = '''
      <div class="esempio-chiaro">
        <p class="esempio__titolo">Un esempio? Il gestionale del nostro negozio l'abbiamo fatto noi.</p>
        <p>Schede di assistenza numerate con il QR per le recensioni, preventivi, fatture e DDT, scontrini su carta termica e cartellini per la vetrina: tutto nello stesso programma.</p>
      </div>'''
    schede = ''.join(scheda_link(s, 'a') for s in servizi)
    elenco_passi = ''.join(
        f'<li><span class="passi__numero" aria-hidden="true">{i}</span><h3>{t(a)}</h3><p>{t(b)}</p></li>'
        for i, (a, b) in enumerate(passi, 1))
    return testa(f'{titolo} | Meg@byte Informatica', pulito(intro)[:155], ['stile-a.css']).replace(
        '<body>', '<body class="a-pagina">') + testata_a() + f'''
<main id="contenuto">

  <section class="pagina-eroe pagina-eroe--panoramica">
    <div class="contenitore">
      <nav class="briciole" aria-label="Sei qui">
        <ol>
          <li><a href="index.html">Home</a></li>
          <li aria-current="page">{titolo}</li>
        </ol>
      </nav>
      {ic(icona, 'ic pagina-eroe__icona')}
      <h1>{titolo}</h1>
      <p class="pagina-eroe__sotto">{sotto}</p>
      <p class="pagina-eroe__intro">{t(intro)}</p>
    </div>
  </section>

  <section class="sezione" aria-label="Servizi">
    <div class="contenitore">
      <ul class="a-griglia-servizi a-griglia-servizi--completa">{schede}</ul>{chiusura}
    </div>
  </section>

  <section class="sezione sezione--tinta a-passi" aria-labelledby="titolo-passi">
    <div class="contenitore">
      <h2 id="titolo-passi">{titolo_passi}</h2>
      <ol class="passi">{elenco_passi}</ol>
    </div>
  </section>

  <section class="invito" aria-labelledby="titolo-invito">
    <div class="contenitore">
      <h2 id="titolo-invito">Non trovi quello che cerchi?</h2>
      <p>Chiamaci o scrivici su WhatsApp: ti diciamo subito se e come possiamo aiutarti.</p>
      <div class="azioni">
        <a class="bottone bottone--primario bottone--grande" href="{TEL_LINK}">{ic('phone')} {TELEFONO}</a>
        <a class="bottone bottone--secondario bottone--grande" href="{WHATSAPP}" rel="noopener">{ic('chat')} WhatsApp</a>
      </div>
    </div>
  </section>

</main>
''' + piede_a()


# ---------------------------------------------------------------- home della bozza B: schede cliccabili
def aggiorna_home_b():
    percorso = os.path.join(B, 'index.html')
    pagina = open(percorso, encoding='utf-8').read()
    if 'pagina.css' not in pagina:
        pagina = pagina.replace('<link rel="stylesheet" href="style.css">',
                                '<link rel="stylesheet" href="style.css">\n  <link rel="stylesheet" href="pagina.css">')
    if 'name="robots"' not in pagina:
        # Bozza online solo per farla vedere: fuori da Google
        pagina = pagina.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n  <meta name="robots" content="noindex">', 1)
    per_nome = {pulito(s['nome']): s for s in SERVIZI}

    def collega(m):
        classe, dentro = m.group(1), m.group(2)
        if 'scheda-link' in dentro:
            return m.group(0)
        nome = re.sub(r'<[^>]+>', '', re.search(r'<h3>(.*?)</h3>', dentro, re.S).group(1)).strip()
        s = per_nome[nome]
        return (f'<li class="{classe}"><a class="scheda-link" href="{s["slug"]}.html">{dentro.strip()}'
                f'<span class="scheda-link__altro">Scopri di più {ic("arrow")}</span></a></li>')

    pagina = re.sub(r'<li class="(scheda-servizio|scheda-su-misura)">(.*?)</li>', collega, pagina, flags=re.S)
    if 'i-check' not in pagina:
        # la home B ha il suo blocco di icone: aggiungo quelle che mancano
        mancanti = ''.join(f'    <symbol id="i-{n}" viewBox="0 0 24 24">{ICONE[n]}</symbol>\n'
                           for n in ICONE if f'id="i-{n}"' not in pagina)
        pagina = pagina.replace('  </defs>\n</svg>', mancanti + '  </defs>\n</svg>', 1)
    open(percorso, 'w', encoding='utf-8', newline='\n').write(pagina)


# ---------------------------------------------------------------- pagina di scelta
def scelta():
    return '''<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>Bozze del sito Meg@byte</title>
  ''' + FONT + '''
  <style>
    body { margin: 0; font-family: Inter, system-ui, sans-serif; background: #f4f7fa; color: #1e293b; }
    main { width: min(100% - 32px, 980px); margin: 48px auto; }
    img { width: 220px; display: block; margin: 0 auto 20px; }
    h1 { font-family: Poppins, sans-serif; color: #123f57; text-align: center; margin: 0 0 8px; }
    p.intro { text-align: center; color: #475569; margin: 0 0 32px; }
    .scelte { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
    a.bozza { display: block; background: #fff; border: 1px solid #dbe3ea; border-radius: 16px; padding: 28px; color: inherit; text-decoration: none; transition: box-shadow .15s, transform .15s; }
    a.bozza:hover { box-shadow: 0 12px 32px rgb(15 23 42 / .1); transform: translateY(-3px); }
    a.bozza:focus-visible { outline: 3px solid #e07c2c; outline-offset: 3px; }
    .lettera { display: inline-grid; place-items: center; width: 44px; height: 44px; border-radius: 12px; color: #fff; font: 700 1.3rem Poppins, sans-serif; background: #1c5b7c; margin-bottom: 14px; }
    .bozza--a .lettera { background: #b85a12; }
    h2 { font-family: Poppins, sans-serif; color: #123f57; margin: 0 0 8px; font-size: 1.3rem; }
    ul { margin: 12px 0 18px; padding-left: 20px; color: #475569; }
    li { margin-bottom: 4px; }
    .apri { font-weight: 600; color: #1c5b7c; }
    @media (max-width: 720px) { .scelte { grid-template-columns: 1fr; } main { margin: 28px auto; } }
  </style>
</head>
<body>
<main>
  <img src="bozza-b/img/logo.png" alt="Meg@byte Informatica">
  <h1>Due bozze del nuovo sito</h1>
  <p class="intro">Stessi contenuti, due impostazioni diverse. In entrambe ogni servizio ha la sua pagina con tutti i dettagli.</p>
  <div class="scelte">
    <a class="bozza bozza--a" href="bozza-a/index.html">
      <span class="lettera">A</span>
      <h2>Più d'impatto, stile SoccorsoPc</h2>
      <ul>
        <li>Logo al centro con telefono e WhatsApp sempre in vista</li>
        <li>Barra del menu colorata con i sottomenu dei servizi</li>
        <li>Grande apertura "Problemi con il PC?" con i problemi cliccabili</li>
        <li>Home snella: l'elenco dei servizi sta nel menu e in due pagine riassuntive</li>
        <li>Punti di forza, marche, recensioni in evidenza</li>
        <li>Pulsante WhatsApp sempre visibile</li>
      </ul>
      <span class="apri">Apri la bozza A →</span>
    </a>
    <a class="bozza bozza--b" href="bozza-b/index.html">
      <span class="lettera">B</span>
      <h2>Pulita ed essenziale</h2>
      <ul>
        <li>La bozza che abbiamo costruito finora</li>
        <li>Menu che scorre alle sezioni della home</li>
        <li>Grafica più sobria, tanto bianco</li>
        <li>Barra Chiama | WhatsApp in basso sul telefono</li>
        <li>Ogni riquadro dei servizi apre la sua pagina</li>
      </ul>
      <span class="apri">Apri la bozza B →</span>
    </a>
  </div>
</main>
</body>
</html>
'''


# ---------------------------------------------------------------- costruzione
def scrivi(percorso, testo):
    open(percorso, 'w', encoding='utf-8', newline='\n').write(testo)


def main():
    os.makedirs(A, exist_ok=True)
    os.makedirs(B, exist_ok=True)
    # La prima volta la bozza di prima diventa la bozza B
    for nome in ('index.html', 'style.css'):
        vecchio = os.path.join(RADICE, nome)
        if os.path.exists(vecchio) and not os.path.exists(os.path.join(B, nome)):
            shutil.move(vecchio, os.path.join(B, nome))
    for cartella in (A, B):
        shutil.copytree(os.path.join(RADICE, 'img'), os.path.join(cartella, 'img'), dirs_exist_ok=True)

    base = open(os.path.join(B, 'style.css'), encoding='utf-8').read()
    pagina = open(os.path.join(STRUMENTI, 'pagina.css'), encoding='utf-8').read()
    extra = open(os.path.join(STRUMENTI, 'stile-a-extra.css'), encoding='utf-8').read()
    scrivi(os.path.join(B, 'pagina.css'), pagina)
    scrivi(os.path.join(A, 'stile-a.css'),
           '/* Generato da strumenti/genera.py: style.css + pagina.css + stile-a-extra.css */\n\n'
           + base + '\n\n' + pagina + '\n\n' + extra)

    aggiorna_home_b()
    scrivi(os.path.join(A, 'index.html'), home_a().replace('</body>', GIOSTRA + '\n</body>'))
    for gruppo, file in PANORAMICA_A.items():
        scrivi(os.path.join(A, file), panoramica_a(gruppo))

    for s in SERVIZI:
        titolo = f"{pulito(s['titolo'])} | Meg@byte Informatica"
        descr = pulito(s['intro'])[:155]
        scrivi(os.path.join(B, f"{s['slug']}.html"),
               testa(titolo, descr, ['style.css', 'pagina.css']) + testata_b() + corpo_pagina(s, 'b') + piede_b())
        scrivi(os.path.join(A, f"{s['slug']}.html"),
               testa(titolo, descr, ['stile-a.css']).replace('<body>', '<body class="a-pagina">')
               + testata_a() + corpo_pagina(s, 'a') + piede_a())

    scrivi(os.path.join(RADICE, 'index.html'), scelta())
    print(f'Fatto: {len(SERVIZI)} pagine di dettaglio per bozza, home A e B, pagina di scelta.')


if __name__ == '__main__':
    main()
