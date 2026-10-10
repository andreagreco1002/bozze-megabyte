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

add_theme_support('title-tag');
add_theme_support('post-thumbnails');
add_theme_support('html5', ['style', 'script']);

/** Niente barra di amministrazione davanti al sito: sporca l'impaginazione. */
add_filter('show_admin_bar', '__return_false');
