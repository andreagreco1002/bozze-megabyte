"""Prepara le pagine del sito nuovo per WordPress.

Dai contenuti in `contenuti.py` scrive `wp/pagine.json`: per ogni pagina il
titolo, lo slug, la descrizione per Google e il contenuto già in blocchi
WordPress (solo blocchi di base, così funziona con qualunque tema).

Il file viene pubblicato insieme alle bozze: dal pannello di WordPress un
pezzo di JavaScript lo legge e crea le pagine come bozze.
"""
import html
import json
import os

from contenuti import (INDIRIZZO, PER_SLUG, TEL_LINK, RECENSIONI, SCRIVI_RECENSIONE, SERVIZI, TELEFONO, WHATSAPP)
from genera import GRUPPI, pulito

GRUPPI_NOME = {chiave: nome for chiave, (nome, _) in GRUPPI.items()}

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOTO = 'https://andreagreco1002.github.io/bozze-megabyte/bozza-a/img/foto/'


def e(testo):
    """Testo pronto per l'HTML."""
    return html.escape(pulito(testo), quote=False)


def paragrafo(testo, classe=None):
    c = f' {{"className":"{classe}"}}' if classe else ''
    attr = f' class="{classe}"' if classe else ''
    return f'<!-- wp:paragraph{c} --><p{attr}>{e(testo)}</p><!-- /wp:paragraph -->'


def titolo(testo, livello=2):
    liv = f' {{"level":{livello}}}' if livello != 2 else ''
    return (f'<!-- wp:heading{liv} --><h{livello} class="wp-block-heading">{e(testo)}</h{livello}>'
            f'<!-- /wp:heading -->')


def elenco(voci):
    dentro = ''.join(f'<!-- wp:list-item --><li>{e(v)}</li><!-- /wp:list-item -->' for v in voci)
    return f'<!-- wp:list --><ul class="wp-block-list">{dentro}</ul><!-- /wp:list -->'


def domanda(q, r):
    return ('<!-- wp:details --><details class="wp-block-details">'
            f'<summary>{e(q)}</summary>'
            f'<!-- wp:paragraph --><p>{e(r)}</p><!-- /wp:paragraph -->'
            '</details><!-- /wp:details -->')


def bottoni(voci):
    """voci: [(testo, indirizzo, principale)]"""
    dentro = ''
    for testo, href, principale in voci:
        stile = '' if principale else ' {"className":"is-style-outline"}'
        classe = 'wp-block-button' + ('' if principale else ' is-style-outline')
        dentro += (f'<!-- wp:button{stile} --><div class="{classe}">'
                   f'<a class="wp-block-button__link wp-element-button" href="{href}">{e(testo)}</a>'
                   '</div><!-- /wp:button -->')
    return f'<!-- wp:buttons --><div class="wp-block-buttons">{dentro}</div><!-- /wp:buttons -->'


def separatore():
    return '<!-- wp:separator --><hr class="wp-block-separator has-alpha-channel-opacity"/><!-- /wp:separator -->'


def invito():
    """Chiusura uguale su tutte le pagine: come ci si mette in contatto."""
    return [
        separatore(),
        titolo('Parliamone'),
        paragrafo('Passa in negozio, chiama o scrivici su WhatsApp: ti diciamo subito come possiamo aiutarti.'),
        bottoni([
            (f'Chiama {TELEFONO}', TEL_LINK, True),
            ('Scrivici su WhatsApp', WHATSAPP, False),
        ]),
        paragrafo(f'{INDIRIZZO} · Lunedì-venerdì 9-13 e 15:30-19:30, sabato 9-13.'),
    ]


def pagina_servizio(s):
    blocchi = [paragrafo(s['sotto'], 'lead'), '%%FOTO%%', paragrafo(s['intro'])]

    blocchi += [titolo('Cosa facciamo'), elenco(s['cosa'])]

    if s.get('passi'):
        blocchi.append(titolo('Come funziona'))
        for i, (nome, testo) in enumerate(s['passi'], 1):
            blocchi.append(titolo(f'{i}. {nome}', 3))
            blocchi.append(paragrafo(testo))

    if s.get('prezzi'):
        blocchi.append(titolo('Quanto costa'))
        blocchi.append(elenco([f'{q}: {p}' for q, p in s['prezzi']]))

    if s.get('faq'):
        blocchi.append(titolo('Domande frequenti'))
        blocchi += [domanda(q, r) for q, r in s['faq']]

    correlati = [PER_SLUG[c] for c in s.get('correlati', []) if c in PER_SLUG]
    if correlati:
        blocchi.append(titolo('Vedi anche'))
        blocchi.append(elenco([f'{c["nome"]}: {c["breve"]}' for c in correlati]))

    blocchi += invito()
    return {
        'slug': s['slug'],
        'titolo': pulito(s['nome']),
        'descrizione': pulito(s['breve'])[:155],
        'foto': s['slug'] + '.jpg',
        'blocchi': '\n\n'.join(blocchi),
    }


def pagina_gruppo(chiave):
    servizi = [s for s in SERVIZI if s['gruppo'] == chiave]
    nome = GRUPPI_NOME[chiave]
    blocchi = [paragrafo(f'Tutto quello che facciamo in {nome.lower()}.', 'lead')]
    for s in servizi:
        blocchi.append(titolo(pulito(s['nome']), 3))
        blocchi.append(paragrafo(s['breve']))
    blocchi += invito()
    return {
        'slug': {'riparazioni': 'riparazioni', 'vendita': 'vendita-e-assemblaggio',
                 'su-misura': 'siti-e-gestionali'}[chiave],
        'titolo': nome,
        'descrizione': f'{nome}: tutti i servizi di Meg@byte Informatica a Roma.'[:155],
        'foto': None,
        'blocchi': '\n\n'.join(blocchi),
    }


def pagina_home():
    blocchi = [
        paragrafo('Il negozio di informatica di fiducia a Roma, in via Tripoli 17: riparazioni, vendita, '
                  'telefonia e software su misura.', 'lead'),
        titolo('Problemi con il computer?'),
        elenco([
            'Non si accende o è lentissimo',
            'Schermo rotto o batteria che non tiene',
            'Virus, pubblicità e finestre che si aprono da sole',
            'Hai perso i tuoi file',
            'Stampante o Wi-Fi che non vanno',
        ]),
        paragrafo('Portacelo: la diagnosi e il preventivo sono gratuiti e senza impegno.'),
    ]

    for chiave in ('riparazioni', 'vendita', 'su-misura'):
        blocchi.append(titolo(GRUPPI_NOME[chiave]))
        for s in [x for x in SERVIZI if x['gruppo'] == chiave]:
            blocchi.append(titolo(pulito(s['nome']), 3))
            blocchi.append(paragrafo(s['breve']))

    blocchi += [
        titolo('Perché sceglierci'),
        elenco([
            'Dal 1998 nello stesso negozio, in via Tripoli 17',
            'Diagnosi e preventivo gratuiti: paghi solo se accetti',
            'Ti spieghiamo tutto con parole semplici',
            'Assistenza su Windows, Mac e Linux',
            '66 recensioni da 5 stelle su Google',
        ]),
        bottoni([('Leggi le recensioni', RECENSIONI, True), ('Lasciane una', SCRIVI_RECENSIONE, False)]),
    ]
    blocchi += invito()
    return {
        'slug': 'home-nuova',
        'titolo': 'Home',
        'descrizione': 'Assistenza, riparazione e vendita computer a Roma. Diagnosi gratuita, '
                       'preventivo prima di procedere.'[:155],
        'foto': 'negozio.jpg',
        'blocchi': '\n\n'.join(blocchi),
    }


def costruisci():
    pagine = [pagina_home()]
    pagine += [pagina_gruppo(g) for g in ('riparazioni', 'vendita', 'su-misura')]
    pagine += [pagina_servizio(s) for s in SERVIZI]
    return {'base_foto': FOTO, 'pagine': pagine}


if __name__ == '__main__':
    dati = costruisci()
    cartella = os.path.join(RADICE, 'wp')
    os.makedirs(cartella, exist_ok=True)
    percorso = os.path.join(cartella, 'pagine.json')
    with open(percorso, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(dati, f, ensure_ascii=False, indent=1)
    print(f'{len(dati["pagine"])} pagine in {percorso}')
    for p in dati['pagine']:
        print(f'  {p["slug"]:32} {len(p["blocchi"]):6} caratteri  foto: {p["foto"] or "—"}')
