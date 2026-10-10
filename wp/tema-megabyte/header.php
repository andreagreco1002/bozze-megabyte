<!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<a class="salta" href="#contenuto">Vai al contenuto</a>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></symbol>
    <symbol id="i-chat" viewBox="0 0 24 24"><path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/></symbol>
    <symbol id="i-pin" viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></symbol>
    <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></symbol>
    <symbol id="i-mail" viewBox="0 0 24 24"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></symbol>
    <symbol id="i-laptop" viewBox="0 0 24 24"><path d="M20 16V7a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9m16 0H4m16 0 1.28 2.55a1 1 0 0 1-.9 1.45H3.62a1 1 0 0 1-.9-1.45L4 16"/></symbol>
    <symbol id="i-smartphone" viewBox="0 0 24 24"><rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/></symbol>
    <symbol id="i-database" viewBox="0 0 24 24"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/></symbol>
    <symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/></symbol>
    <symbol id="i-building" viewBox="0 0 24 24"><path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4"/><path d="M10 10h4"/><path d="M10 14h4"/><path d="M10 18h4"/></symbol>
    <symbol id="i-monitor" viewBox="0 0 24 24"><rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></symbol>
    <symbol id="i-bag" viewBox="0 0 24 24"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></symbol>
    <symbol id="i-wifi" viewBox="0 0 24 24"><path d="M5 13a10 10 0 0 1 14 0"/><path d="M8.5 16.5a5 5 0 0 1 7 0"/><path d="M2 8.82a15 15 0 0 1 20 0"/><line x1="12" x2="12.01" y1="20" y2="20"/></symbol>
    <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></symbol>
    <symbol id="i-menu" viewBox="0 0 24 24"><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="18" y2="18"/></symbol>
    <symbol id="i-layout" viewBox="0 0 24 24"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></symbol>
    <symbol id="i-dashboard" viewBox="0 0 24 24"><rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/></symbol>
    <symbol id="i-file" viewBox="0 0 24 24"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></symbol>
    <symbol id="i-zap" viewBox="0 0 24 24"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></symbol>
    <symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></symbol>
    <symbol id="i-star" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></symbol>
    <symbol id="i-check" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></symbol>
    <symbol id="i-alert" viewBox="0 0 24 24"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/></symbol>
    <symbol id="i-chevron" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>
    <symbol id="i-home" viewBox="0 0 24 24"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></symbol>
    <symbol id="i-award" viewBox="0 0 24 24"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></symbol>
    <symbol id="i-tool" viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></symbol>
  </defs>
</svg>
<div class="a-topbar">
  <div class="contenitore a-topbar__riga">
    <span><svg class="ic" aria-hidden="true"><use href="#i-pin"/></svg> Via Tripoli 17, 00199 Roma (RM)</span>
    <span><svg class="ic" aria-hidden="true"><use href="#i-clock"/></svg> Lun–Ven 9–13 · 15:30–19:30 · Sab 9–13</span>
    <span class="a-topbar__email"><svg class="ic" aria-hidden="true"><use href="#i-mail"/></svg> <a href="mailto:info@mbyte.it">info@mbyte.it</a></span>
  </div>
</div>

<header class="a-testata">
  <div class="contenitore a-testata__riga">
    <p class="a-slogan">Assistenza informatica a Roma<br><strong>da oltre 20 anni</strong></p>
    <a class="a-logo" href="/" aria-label="Meg@byte Informatica, torna alla home">
      <img src="<?php echo esc_url(get_template_directory_uri()); ?>/assets/img/logo.png" alt="Meg@byte Informatica" width="1200" height="294">
    </a>
    <div class="a-contatti">
      <a class="bottone bottone--primario" href="tel:+390686399483"><svg class="ic" aria-hidden="true"><use href="#i-phone"/></svg> 06 8639 9483</a>
      <a class="bottone bottone--whatsapp" href="https://wa.me/390686399483" rel="noopener"><svg class="ic" aria-hidden="true"><use href="#i-chat"/></svg> WhatsApp</a>
    </div>
  </div>
</header>

<nav class="a-menu" aria-label="Menu principale">
  <div class="contenitore">
    <ul class="a-menu__lista">
      <li><a href="/"><span>Home</span><small>Meg@byte Informatica</small></a></li>
      <li class="a-menu__tendina">
        <a href="/riparazioni/"><span>Riparazioni <svg class="ic" aria-hidden="true"><use href="#i-chevron"/></svg></span><small>PC, Mac, smartphone</small></a>
        <ul class="a-sottomenu"><li><a href="/riparazione-pc-mac/"><svg class="ic" aria-hidden="true"><use href="#i-laptop"/></svg> Riparazione PC e Mac</a></li><li><a href="/riparazione-smartphone-tablet/"><svg class="ic" aria-hidden="true"><use href="#i-smartphone"/></svg> Smartphone e tablet</a></li><li><a href="/recupero-dati/"><svg class="ic" aria-hidden="true"><use href="#i-database"/></svg> Recupero dati</a></li><li><a href="/virus-sicurezza/"><svg class="ic" aria-hidden="true"><use href="#i-shield"/></svg> Virus e sicurezza</a></li><li><a href="/assistenza-aziende/"><svg class="ic" aria-hidden="true"><use href="#i-building"/></svg> Assistenza per aziende</a></li><li><a href="/assistenza-remota/"><svg class="ic" aria-hidden="true"><use href="#i-monitor"/></svg> Assistenza da remoto</a></li></ul>
      </li>
      <li class="a-menu__tendina">
        <a href="/vendita-e-assemblaggio/"><span>Vendita <svg class="ic" aria-hidden="true"><use href="#i-chevron"/></svg></span><small>computer, PC su misura, offerte</small></a>
        <ul class="a-sottomenu"><li><a href="/vendita/"><svg class="ic" aria-hidden="true"><use href="#i-bag"/></svg> Computer e accessori</a></li><li><a href="/pc-gaming/"><svg class="ic" aria-hidden="true"><use href="#i-zap"/></svg> PC assemblati e da gaming</a></li><li><a href="/telefonia-internet/"><svg class="ic" aria-hidden="true"><use href="#i-wifi"/></svg> Telefonia e internet</a></li></ul>
      </li>
      <li class="a-menu__tendina">
        <a href="/siti-e-gestionali/"><span>Siti e gestionali <svg class="ic" aria-hidden="true"><use href="#i-chevron"/></svg></span><small>su misura per te</small></a>
        <ul class="a-sottomenu"><li><a href="/siti-web/"><svg class="ic" aria-hidden="true"><use href="#i-layout"/></svg> Landing page e siti web</a></li><li><a href="/gestionali/"><svg class="ic" aria-hidden="true"><use href="#i-dashboard"/></svg> Gestionali su misura</a></li></ul>
      </li>
      <li><a href="/#recensioni"><span>Recensioni</span><small>5 stelle su Google</small></a></li>
      <li><a href="/#contatti"><span>Contatti</span><small>orari e dove siamo</small></a></li>
    </ul>
    <details class="a-menu-mobile">
      <summary><svg class="ic" aria-hidden="true"><use href="#i-menu"/></svg> MENU</summary>
      <ul class="a-menu-mobile__pannello">
        <li><a href="/">Home</a></li>
        <li>
          <details class="a-gruppo">
            <summary>Riparazioni e assistenza <svg class="ic" aria-hidden="true"><use href="#i-chevron"/></svg></summary>
            <ul><li><a href="/riparazioni/">Tutti i servizi</a></li><li><a href="/riparazione-pc-mac/">Riparazione PC e Mac</a></li><li><a href="/riparazione-smartphone-tablet/">Smartphone e tablet</a></li><li><a href="/recupero-dati/">Recupero dati</a></li><li><a href="/virus-sicurezza/">Virus e sicurezza</a></li><li><a href="/assistenza-aziende/">Assistenza per aziende</a></li><li><a href="/assistenza-remota/">Assistenza da remoto</a></li></ul>
          </details>
        </li>
        <li>
          <details class="a-gruppo">
            <summary>Vendita <svg class="ic" aria-hidden="true"><use href="#i-chevron"/></svg></summary>
            <ul><li><a href="/vendita-e-assemblaggio/">Tutto quello che vendiamo</a></li><li><a href="/vendita/">Computer e accessori</a></li><li><a href="/pc-gaming/">PC assemblati e da gaming</a></li><li><a href="/telefonia-internet/">Telefonia e internet</a></li></ul>
          </details>
        </li>
        <li>
          <details class="a-gruppo">
            <summary>Siti e gestionali <svg class="ic" aria-hidden="true"><use href="#i-chevron"/></svg></summary>
            <ul><li><a href="/siti-e-gestionali/">Tutti i servizi su misura</a></li><li><a href="/siti-web/">Landing page e siti web</a></li><li><a href="/gestionali/">Gestionali su misura</a></li></ul>
          </details>
        </li>
        <li><a href="/#recensioni">Recensioni</a></li>
        <li><a href="/#contatti">Contatti</a></li>
      </ul>
    </details>
  </div>
</nav>
<main id="contenuto">
