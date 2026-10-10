"""Impacchetta la bozza come tema WordPress, identico all'originale.

Invece di rifare il vestito con i blocchi di WordPress, porta dentro gli stessi
file della bozza: lo stesso foglio di stile, la stessa intestazione, lo stesso
piè di pagina. Le pagine di WordPress contengono solo quello che nella bozza sta
dentro <main>, così il risultato è identico a quello che ha visto il padre.

Produce:
  wp/tema-megabyte/        il tema, pronto da caricare dal pannello
  wp/tema-megabyte.zip     lo stesso, zippato
  wp/contenuti.json        il contenuto di ogni pagina, da mettere nelle pagine
"""
import json
import os
import re
import shutil

RADICE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOZZA = os.path.join(RADICE, 'bozza-a')
USCITA = os.path.join(RADICE, 'wp')
NOME_TEMA = 'tema-megabyte'
SITO = 'https://www.megabyteinformatica.it'
ASSETS = f'{SITO}/wp/wp-content/themes/{NOME_TEMA}/assets'

# Lo shortcode del plugin già installato: recensioni vere, aggiornate da sole
RECENSIONI_VERE = '[trustindex no-registration=google]'


def leggi(nome):
    return open(os.path.join(BOZZA, nome), encoding='utf-8').read()


def fra(testo, inizio, fine, compresi=True):
    a = testo.index(inizio)
    b = testo.index(fine, a) + (len(fine) if compresi else 0)
    return testo[a:b]


def collegamenti(testo):
    """I collegamenti della bozza diventano indirizzi di WordPress."""
    testo = testo.replace('href="index.html#', 'href="/#')
    testo = testo.replace('href="index.html"', 'href="/"')
    testo = re.sub(r'href="([a-z0-9-]+)\.html"', r'href="/\1/"', testo)
    testo = re.sub(r'href="([a-z0-9-]+)\.html#', r'href="/\1/#', testo)
    return testo


def immagini(testo, base):
    """Le immagini stanno dentro il tema."""
    return re.sub(r'(src|href)="img/([^"?]+)(\?v=[0-9a-f]+)?"', rf'\1="{base}/img/\2"', testo)


def pulisci(testo):
    """Via l'avviso che è una bozza."""
    return re.sub(r'<div class="avviso-bozza".*?</div>\s*', '', testo, flags=re.S)


def costruisci_tema():
    casa = leggi('index.html')
    cartella = os.path.join(USCITA, NOME_TEMA)
    shutil.rmtree(cartella, ignore_errors=True)
    os.makedirs(os.path.join(cartella, 'assets'), exist_ok=True)

    # foglio di stile: quello della bozza, con l'intestazione che WordPress richiede
    stile = leggi('stile-a.css')
    intestazione_css = (
        '/*\n'
        'Theme Name: Meg@byte Informatica\n'
        'Description: Il sito di Meg@byte Informatica: stessi file della bozza approvata.\n'
        'Version: 1.0\n'
        'Requires at least: 6.0\n'
        'Text Domain: megabyte\n'
        '*/\n\n'
    )
    with open(os.path.join(cartella, 'style.css'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(intestazione_css + immagini(stile, '../assets'))

    shutil.copytree(os.path.join(BOZZA, 'img'), os.path.join(cartella, 'assets', 'img'))

    # pezzi della pagina presi dalla casa
    sprite = fra(casa, '<svg width="0" height="0"', '</svg>')
    # dalla barra in cima fino alla fine del menu: tutto quello che sta sopra il contenuto
    barra_e_testata = fra(casa, '<div class="a-topbar">', '</nav>')
    piede = fra(casa, '<footer class="a-piede">', '</footer>')
    whatsapp = fra(casa, '<a class="a-whatsapp"', '</a>')
    script_menu = fra(casa, '<script>', '</script>')  # il primo: chiusura del menu sul telefono

    def pronto(pezzo):
        return immagini(collegamenti(pulisci(pezzo)), "<?php echo esc_url(get_template_directory_uri()); ?>/assets")

    with open(os.path.join(cartella, 'header.php'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('<!doctype html>\n<html <?php language_attributes(); ?>>\n<head>\n'
                '<meta charset="<?php bloginfo(\'charset\'); ?>">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
                '<?php wp_head(); ?>\n</head>\n'
                '<body <?php body_class(); ?>>\n'
                '<?php wp_body_open(); ?>\n'
                '<a class="salta" href="#contenuto">Vai al contenuto</a>\n'
                + sprite + '\n'
                + pronto(barra_e_testata) + '\n'
                '<main id="contenuto">\n')

    with open(os.path.join(cartella, 'footer.php'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('</main>\n'
                + pronto(piede) + '\n'
                + pronto(whatsapp) + '\n'
                + script_menu + '\n'
                '<?php wp_footer(); ?>\n</body>\n</html>\n')

    with open(os.path.join(cartella, 'index.php'), 'w', encoding='utf-8', newline='\n') as f:
        f.write("<?php get_header(); ?>\n"
                "<?php while (have_posts()) : the_post(); the_content(); endwhile; ?>\n"
                "<?php get_footer(); ?>\n")
    shutil.copy(os.path.join(cartella, 'index.php'), os.path.join(cartella, 'page.php'))

    with open(os.path.join(cartella, 'functions.php'), 'w', encoding='utf-8', newline='\n') as f:
        f.write("""<?php
/** Il tema serve solo a vestire le pagine: niente fronzoli. */

add_action('wp_enqueue_scripts', function () {
    wp_enqueue_style('megabyte-font', 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@600;700&display=swap', [], null);
    wp_enqueue_style('megabyte', get_stylesheet_uri(), ['megabyte-font'], '1.0');
    // I fogli di stile dei blocchi non servono: il vestito e' tutto qui
    wp_dequeue_style('wp-block-library');
    wp_dequeue_style('global-styles');
}, 20);

add_theme_support('title-tag');
add_theme_support('post-thumbnails');
add_theme_support('html5', ['style', 'script']);

/** Niente barra di amministrazione davanti al sito: sporca l'impaginazione. */
add_filter('show_admin_bar', '__return_false');
""")

    scorciatoia = os.path.join(USCITA, NOME_TEMA + '.zip')
    if os.path.exists(scorciatoia):
        os.remove(scorciatoia)
    shutil.make_archive(os.path.join(USCITA, NOME_TEMA), 'zip', USCITA, NOME_TEMA)
    return cartella


def contenuti_pagine():
    """Il contenuto di ogni pagina: quello che nella bozza sta dentro <main>."""
    pagine = {}
    for file in sorted(os.listdir(BOZZA)):
        if not file.endswith('.html'):
            continue
        slug = 'home-nuova' if file == 'index.html' else file[:-5]
        corpo = fra(leggi(file), '<main id="contenuto">', '</main>', compresi=False)
        corpo = corpo[corpo.index('>') + 1:]
        corpo = immagini(collegamenti(pulisci(corpo)), ASSETS)
        # le recensioni finte lasciano il posto a quelle vere di Google
        corpo = re.sub(r'<div class="giostra".*?</div>\s*</div>', RECENSIONI_VERE, corpo, flags=re.S)
        corpo = re.sub(r'<p class="nota-bozza">.*?</p>\s*', '', corpo, flags=re.S)
        pagine[slug] = corpo
    return pagine


if __name__ == '__main__':
    cartella = costruisci_tema()
    pagine = contenuti_pagine()
    with open(os.path.join(USCITA, 'contenuti.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(pagine, f, ensure_ascii=False, indent=1)
    print('tema in', cartella)
    print('zip  in', os.path.join(USCITA, NOME_TEMA + '.zip'))
    for slug, corpo in pagine.items():
        print(f'  {slug:32} {len(corpo):7} caratteri')
