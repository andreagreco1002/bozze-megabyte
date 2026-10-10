</main>
<footer class="a-piede">
  <div class="contenitore a-piede__griglia">
    <div>
      <img class="a-piede__logo" src="<?php echo esc_url(get_template_directory_uri()); ?>/assets/img/logo.png" alt="Meg@byte Informatica" width="1200" height="294" loading="lazy">
      <p>Assistenza specializzata in ambienti Windows, Mac e Linux, vendita di computer e periferiche, telefonia fissa e mobile, siti e software su misura. A Roma da oltre 20 anni.</p>
    </div>
    <div>
      <h3>Meg@byte</h3>
      <ul>
        <li><a href="/riparazioni/">Riparazioni e assistenza</a></li>
        <li><a href="/vendita-e-assemblaggio/">Vendita e PC assemblati</a></li>
        <li><a href="/siti-e-gestionali/">Siti e gestionali</a></li>
        <li><a href="/#recensioni">Recensioni</a></li>
        <li><a href="/#contatti">Dove siamo</a></li>
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
        <li>Via Tripoli 17, 00199 Roma (RM)</li>
        <li><a href="tel:+390686399483">06 8639 9483</a> (anche WhatsApp)</li>
        <li><a href="mailto:info@mbyte.it">info@mbyte.it</a></li>
      </ul>
    </div>
  </div>
  <div class="contenitore a-piede__fondo">
    <span>MEG@BYTE INFORMATICA S.R.L. · Partita IVA 06455961000 · REA RM-969038</span>
    <span><a href="#">Privacy</a> · <a href="#">Cookie</a></span>
  </div>
</footer>
<a class="a-whatsapp" href="https://wa.me/390686399483" rel="noopener" aria-label="Scrivici su WhatsApp"><svg class="ic" aria-hidden="true"><use href="#i-chat"/></svg></a>
<script>
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
</script>
<?php wp_footer(); ?>
</body>
</html>
