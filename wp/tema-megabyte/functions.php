<?php
/** Il tema serve solo a vestire le pagine: niente fronzoli. */

add_action('wp_enqueue_scripts', function () {
    wp_enqueue_style('megabyte-font', 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@600;700&display=swap', [], null);
    wp_enqueue_style('megabyte', get_stylesheet_uri(), ['megabyte-font'], '1.0');
    // I fogli di stile dei blocchi non servono: il vestito e' tutto qui
    wp_dequeue_style('wp-block-library');
    wp_dequeue_style('global-styles');
}, 20);

/** WordPress aggiunge <p> e <br> dove capita: sul nostro HTML fa solo danni. */
remove_filter('the_content', 'wpautop');
remove_filter('the_excerpt', 'wpautop');

/** Le nostre visite non finiscono nelle statistiche: chi e' collegato non viene contato. */
add_action('wp_enqueue_scripts', function () {
    if (!is_user_logged_in()) {
        return;
    }
    foreach (['burst', 'burst-timeme', 'burst-goals'] as $pezzo) {
        wp_dequeue_script($pezzo);
        wp_deregister_script($pezzo);
    }
}, 100);

/** Gli indirizzi vecchi portano alla pagina nuova che li sostituisce. */
add_action('template_redirect', function () {
    $vecchi = [
        'home' => '/',
        'chi-siamo' => '/',
        'servizi' => '/#servizi',
        'contattaci' => '/#contatti',
        'assistenza-informatica-per-i-privati' => '/riparazioni/',
        'assistenza-informatica-per-le-aziende' => '/assistenza-aziende/',
        'assistenza-e-consulenza-informatica-per-i-professionisti' => '/assistenza-aziende/',
        'assistenza-informatica-remota' => '/assistenza-remota/',
    ];
    $via = trim((string) parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH), '/');
    if (isset($vecchi[$via])) {
        wp_redirect(home_url($vecchi[$via]), 301);
        exit;
    }
});

/** Yoast: se non c'e' una descrizione scritta a mano, usa il riassunto della pagina. */
add_filter('wpseo_metadesc', function ($descrizione) {
    if ($descrizione) {
        return $descrizione;
    }
    $pagina = get_queried_object();
    return ($pagina instanceof WP_Post && $pagina->post_excerpt) ? $pagina->post_excerpt : $descrizione;
});

/** Su Google il titolo della home dice cosa facciamo e dove, non solo "Home". */
add_filter('wpseo_title', function ($titolo) {
    return is_front_page() ? 'Assistenza e riparazione computer a Roma - Meg@byte Informatica' : $titolo;
});

add_theme_support('title-tag');
add_theme_support('post-thumbnails');
add_theme_support('html5', ['style', 'script']);

/** Niente barra di amministrazione davanti al sito: sporca l'impaginazione. */
add_filter('show_admin_bar', '__return_false');
