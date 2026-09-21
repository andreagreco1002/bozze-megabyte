"""
Contenuti delle pagine di dettaglio, uguali per le due bozze.

Il testo fra [[doppie quadre]] e' da confermare: nelle bozze esce evidenziato in giallo.
Dove possibile i contenuti vengono dal sito attuale di Meg@byte (servizi, parti
originali, rimozione manuale dei virus, contratti per aziende, TeamViewer...).
"""

TELEFONO = '06 8639 9483'
TEL_LINK = 'tel:+390686399483'
WHATSAPP = 'https://wa.me/390686399483'
EMAIL = 'info@mbyte.it'
INDIRIZZO = 'Via Tripoli 17, 00199 Roma (RM)'
PLACE_ID = 'ChIJ9YvTWFlhLxMRx3CmYad9d9Q'
MAPPA = ('https://www.google.com/maps/search/?api=1&amp;query=Meg%40byte%20Informatica%20Via%20Tripoli%2017%20Roma'
         f'&amp;query_place_id={PLACE_ID}')
RECENSIONI = f'https://search.google.com/local/reviews?placeid={PLACE_ID}'
SCRIVI_RECENSIONE = f'https://search.google.com/local/writereview?placeid={PLACE_ID}'
ORARI = [('Lunedì – Venerdì', ['9:00–13:00', '15:30–19:30']), ('Sabato', ['9:00–13:00']), ('Domenica', ['chiuso'])]

PASSI_RIPARAZIONE = [
    ('Porti il dispositivo', 'Ti diamo subito la scheda di accettazione con il numero della riparazione.'),
    ('Diagnosi e preventivo', '[[Ti contattiamo con il preventivo prima di procedere]]: nessuna sorpresa.'),
    ('Ritiro', 'Quando è pronto ti avvisiamo: passi in negozio con la scheda e lo ritiri.'),
]
PASSI_SU_MISURA = [
    ('Ci racconti come lavori', 'Una chiacchierata, in negozio o in videochiamata, per capire cosa ti serve davvero.'),
    ('Bozza da provare', 'Prepariamo una prima versione che vedi e correggi insieme a noi, prima di andare avanti.'),
    ('Consegna e assistenza', 'Lo mettiamo in funzione, ti spieghiamo come usarlo e restiamo il tuo punto di riferimento.'),
]
FAQ_SU_MISURA = [
    ('Quanto costa?', "Dipende da quello che serve: dopo una prima chiacchierata ti facciamo un preventivo chiaro, senza impegno."),
    ('Quanto tempo serve?', "Per una pagina bastano pochi giorni, per un gestionale qualche settimana: ti diamo i tempi insieme al preventivo."),
]

# Ogni servizio: pagina (slug), gruppo, icona, testo breve per le schede della home, pagina di dettaglio
SERVIZI = [
    # ------------------------------------------------------------------ riparazioni
    dict(
        slug='riparazione-pc-mac', gruppo='riparazioni', icona='laptop',
        nome='Riparazione PC e Mac',
        breve='Computer fissi e portatili: schermi, tastiere, batterie, dischi, lentezza e problemi di avvio.',
        titolo='Riparazione PC, notebook e Mac a Roma',
        sotto='Computer fissi e portatili di tutte le marche, Windows, Mac e Linux. Anche se acquistati altrove.',
        intro=("Il computer non si accende, è diventato lentissimo, lo schermo è rotto o fa rumori strani? "
               "Portalo in Via Tripoli 17: facciamo la diagnosi, ti spieghiamo il problema con parole semplici "
               "e ripariamo sia l'hardware sia il software."),
        cosa=[
            'Computer che non si accende o si spegne da solo',
            'Sostituzione di schermi, tastiere, batterie e cerniere',
            'Sostituzione e aggiornamento di dischi e memoria RAM',
            'Pulizia interna, ventole e surriscaldamento',
            'Installazione e aggiornamento di Windows, macOS e Linux',
            'Installazione di stampanti, scanner e periferiche',
            'Assemblaggio di PC e server su misura',
            'Assistenza anche su computer acquistati altrove',
        ],
        passi=PASSI_RIPARAZIONE,
        faq=[
            ('Quanto costa la diagnosi?', '[[Ti facciamo un preventivo prima di procedere: se non lo accetti, non paghi la riparazione.]]'),
            ('In quanto tempo è pronto?', "Dipende dal guasto e dai ricambi: all'accettazione ti diamo una stima e ti avvisiamo appena è pronto."),
            ('Riparate anche i Mac?', 'Sì: lavoriamo su Windows, Mac e Linux.'),
            ('I miei dati sono al sicuro?', "Li trattiamo solo per la riparazione, come scritto sulla scheda di accettazione. [[Se temi di perderli, possiamo farne prima una copia.]]"),
        ],
        correlati=['recupero-dati', 'virus-sicurezza', 'vendita'],
    ),
    dict(
        slug='riparazione-smartphone-tablet', gruppo='riparazioni', icona='smartphone',
        nome='Smartphone e tablet',
        breve='Sostituzione di schermi, batterie e componenti, per tutte le marche.',
        titolo='Riparazione smartphone e tablet a Roma',
        sotto='Schermi, batterie e componenti di tutte le marche, con parti originali.',
        intro=("Vetro rotto, batteria che dura poche ore, il telefono non si ricarica più? Ripariamo smartphone "
               "e tablet di tutte le marche sostituendo schermi, batterie e componenti interni con parti originali."),
        cosa=[
            'Sostituzione di schermi e vetri rotti',
            'Sostituzione della batteria',
            'Connettore di ricarica, microfono, altoparlante e fotocamere',
            '[[Telefoni caduti in acqua: verifica e recupero]]',
            'Trasferimento di dati, contatti e foto sul nuovo telefono',
            'Configurazione di email, WhatsApp e backup',
        ],
        passi=PASSI_RIPARAZIONE,
        faq=[
            ('Usate ricambi originali?', 'Sì: sostituiamo schermi, batterie e componenti interni con parti originali.'),
            ('Perdo i miei dati?', "Di solito una riparazione non cancella i dati, ma è sempre meglio fare un backup prima di consegnarci il telefono. Se non sai come si fa, ti aiutiamo noi."),
            ('Quanto costa cambiare lo schermo?', "Dipende da marca e modello: chiamaci o scrivici su WhatsApp il modello esatto e ti diciamo prezzo e tempi."),
        ],
        correlati=['riparazione-pc-mac', 'recupero-dati', 'telefonia-internet'],
    ),
    dict(
        slug='recupero-dati', gruppo='riparazioni', icona='database',
        nome='Recupero dati',
        breve='Da dischi, chiavette, cellulari e fotocamere che non si leggono più.',
        titolo='Recupero dati a Roma',
        sotto='Foto, documenti e lavoro da dischi, chiavette, cellulari e fotocamere danneggiati.',
        intro=("Foto, documenti, anni di lavoro su un disco che non si legge più? Proviamo a recuperare i dati da "
               "dischi, chiavette, schede di memoria, cellulari e fotocamere, anche danneggiati o infettati da virus."),
        avviso=('Cosa fare subito', "Se il disco fa rumori strani o non viene riconosciuto, smetti di usarlo: ogni "
                "tentativo può peggiorare la situazione. Spegnilo e portacelo così com'è."),
        cosa=[
            'Hard disk e SSD che non vengono più riconosciuti',
            'Chiavette USB e schede di memoria',
            'Cellulari e fotocamere',
            'File cancellati per errore',
            'Dischi danneggiati da virus',
            'Backup su misura per non perdere più nulla (NAS, dischi esterni)',
        ],
        passi=PASSI_RIPARAZIONE,
        faq=[
            ('Riuscite sempre a recuperare tutto?', "Non sempre: dipende dal danno. [[Dopo la diagnosi ti diciamo cosa si può recuperare, e solo allora decidi se procedere.]]"),
            ('Quanto costa?', "[[Dipende dal tipo di danno: la diagnosi ci dice cosa è recuperabile e ti facciamo un preventivo.]]"),
            ('Come evito che succeda di nuovo?', "Con un backup automatico: ti consigliamo la soluzione adatta, su NAS o dischi esterni, e la configuriamo noi."),
        ],
        correlati=['riparazione-pc-mac', 'virus-sicurezza', 'assistenza-aziende'],
    ),
    dict(
        slug='virus-sicurezza', gruppo='riparazioni', icona='shield',
        nome='Virus e sicurezza',
        breve='Rimozione di virus e malware, anche nei casi più difficili, e protezione dei tuoi dati.',
        titolo='Rimozione virus e sicurezza informatica',
        sotto='Virus, malware, spyware e trojan rimossi a mano, anche nei casi più difficili.',
        intro=("Pubblicità che si aprono da sole, computer lentissimo, programmi mai installati, email strane "
               "inviate a tuo nome? Rimuoviamo a mano virus, malware, spyware e trojan, anche nei casi più "
               "difficili, e mettiamo in sicurezza il computer."),
        avviso=('Ti chiedono di pagare per sbloccare il PC?', "Non pagare e non chiamare i numeri indicati nel messaggio. "
                "Spegni il computer e contattaci."),
        cosa=[
            'Rimozione di virus, malware, spyware, adware e trojan',
            'Pulizia di browser e programmi indesiderati',
            "Installazione e configurazione dell'antivirus",
            'Aggiornamenti di sicurezza del sistema',
            "Protezione della rete di casa o dell'ufficio (router, firewall, Wi-Fi)",
            'Sicurezza della rete aziendale e adempimenti privacy',
        ],
        passi=PASSI_RIPARAZIONE,
        faq=[
            ('Perdo i miei file?', "Nella maggior parte dei casi no: rimuoviamo il virus lasciando i tuoi documenti al loro posto. [[Se serve, prima ne facciamo una copia.]]"),
            ('Si può fare da remoto?', "Spesso sì, se il computer si accende e si collega a internet. Altrimenti è meglio portarlo in negozio."),
        ],
        correlati=['assistenza-remota', 'recupero-dati', 'assistenza-aziende'],
    ),
    dict(
        slug='assistenza-aziende', gruppo='riparazioni', icona='building',
        nome='Assistenza per aziende',
        breve='Reti cablate e wireless, server, backup e contratti di assistenza continuativa.',
        titolo='Assistenza informatica per aziende e uffici',
        sotto='Computer, server, reti e backup, con un punto di riferimento sempre disponibile.',
        intro=("Seguiamo l'informatica di studi, uffici e negozi: computer, server, reti, stampanti e backup, "
               "con contratti di assistenza e manutenzione preventiva per lavorare senza interruzioni."),
        cosa=[
            'Contratti di assistenza con manutenzione preventiva',
            'Progettazione e realizzazione di reti cablate e wireless',
            'Server, NAS e backup automatici',
            'Router, firewall, access point e stampanti di rete',
            'Sicurezza della rete e misure per la privacy',
            'Fornitura di computer, accessori e materiali di consumo',
            'Connettività business [[MCLINK e Fastweb]]',
            'Siti e gestionali su misura per la tua azienda',
        ],
        passi=[
            ('Sopralluogo', "Vediamo com'è organizzata l'informatica dell'ufficio e cosa non funziona."),
            ('Proposta', '[[Ti proponiamo gli interventi e, se ti serve, un contratto di assistenza su misura.]]'),
            ('Assistenza continua', 'Interveniamo in sede o da remoto, e teniamo tutto in ordine nel tempo.'),
        ],
        faq=[
            ('Intervenite in sede?', 'Sì: interveniamo in sede e, quando basta, da remoto.'),
            ('Come funziona un contratto di assistenza?', "[[Si concorda un pacchetto di ore o un canone con tempi di intervento definiti, costruito sulle esigenze dell'azienda.]]"),
        ],
        correlati=['gestionali', 'virus-sicurezza', 'telefonia-internet'],
    ),
    dict(
        slug='assistenza-remota', gruppo='riparazioni', icona='monitor',
        nome='Assistenza da remoto',
        breve='Risolviamo i problemi software collegandoci al tuo computer, senza che tu debba venire.',
        titolo='Assistenza informatica da remoto',
        sotto='Ci colleghiamo al tuo computer in sicurezza e risolviamo mentre guardi.',
        intro=("Molti problemi si risolvono senza muoverti da casa o dall'ufficio: con il tuo permesso ci colleghiamo "
               "al computer tramite TeamViewer e lo sistemiamo mentre guardi."),
        prezzi=[('30 minuti', '[[30 €]]'), ('60 minuti', '[[60 €]]')],
        cosa=[
            'Programmi che non funzionano o non si installano',
            'Configurazione della posta elettronica',
            'Stampanti e periferiche',
            'Computer lento: pulizia e ottimizzazione',
            'Rimozione di programmi indesiderati',
            'Consulenza e piccoli lavori guidati',
        ],
        passi=[
            ('Ci contatti', 'Chiamaci o scrivici su WhatsApp e raccontaci il problema.'),
            ('Ti colleghi', 'Ti diciamo come avviare TeamViewer: bastano un paio di clic.'),
            ('Risolviamo', 'Lavoriamo mentre guardi. Il collegamento lo chiudi tu quando vuoi.'),
        ],
        faq=[
            ('È sicuro?', 'Sì: il collegamento lo avvii tu, vedi tutto quello che facciamo e puoi chiuderlo in qualsiasi momento.'),
            ('Cosa non si può fare da remoto?', "I guasti fisici: schermo rotto, batteria, computer che non si accende. In quel caso serve portarlo in negozio."),
        ],
        correlati=['virus-sicurezza', 'riparazione-pc-mac', 'assistenza-aziende'],
    ),
    dict(
        slug='vendita', gruppo='riparazioni', icona='bag',
        nome='Vendita',
        breve='Computer, portatili, smartphone e accessori delle migliori marche, consigliati su misura.',
        titolo='Vendita computer, notebook e accessori',
        sotto='Le migliori marche, consigliate su come userai il dispositivo.',
        intro=("Computer, portatili, smartphone e accessori delle migliori marche. Ti aiutiamo a scegliere quello "
               "giusto per come lo userai, [[e te lo consegniamo già pronto e configurato]]."),
        cosa=[
            'Computer fissi e portatili',
            'PC assemblati su misura',
            'Smartphone e tablet',
            'Monitor, stampanti e periferiche',
            'Materiali di consumo: toner, cartucce, cavi',
            'Trasferimento dei dati dal vecchio al nuovo dispositivo',
        ],
        passi=[
            ('Ci dici cosa ti serve', 'Lavoro, scuola, grafica, gioco: partiamo da come lo userai.'),
            ('Ti consigliamo', 'Ti proponiamo le soluzioni giuste per il tuo budget, spiegando le differenze.'),
            ('Pronto da usare', '[[Configuriamo il dispositivo e ci trasferiamo i tuoi dati.]]'),
        ],
        faq=[
            ('Mi aiutate a scegliere?', 'Certo: ti spieghiamo le differenze con parole semplici e ti consigliamo solo quello che ti serve.'),
            ('Posso portare il vecchio computer?', '[[Sì: trasferiamo dati e programmi sul nuovo.]]'),
        ],
        correlati=['riparazione-pc-mac', 'telefonia-internet', 'assistenza-aziende'],
    ),
    dict(
        slug='telefonia-internet', gruppo='riparazioni', icona='wifi',
        nome='Telefonia e internet',
        breve='Offerte [[Iliad e Fastweb]] per privati e aziende, attivabili in negozio.',
        titolo='Telefonia e internet: offerte in negozio',
        sotto='Cellulare, fibra e linee per ufficio, con qualcuno che ti spiega tutto.',
        intro=("Attivi in negozio la tua offerta per casa, ufficio o cellulare, con qualcuno che ti spiega "
               "le condizioni e ti aiuta a configurare tutto."),
        cosa=[
            'Offerte [[Iliad]] per cellulare',
            'Fibra e telefonia [[Fastweb]] per casa e ufficio',
            'Connettività business [[MCLINK]]',
            'Configurazione di router e rete Wi-Fi',
            'Portabilità del numero',
        ],
        passi=[
            ('Passi in negozio', 'Porta un documento e, se cambi operatore, i dati della linea attuale.'),
            ('Scegli l’offerta', 'Ti spieghiamo costi e condizioni senza giri di parole.'),
            ('Attivazione', 'Seguiamo noi la pratica e ti aiutiamo a configurare router e telefono.'),
        ],
        faq=[
            ('Posso tenere il mio numero?', 'Sì, con la portabilità del numero.'),
            ('Mi aiutate anche con il router?', 'Sì: configuriamo router e rete Wi-Fi di casa o dell’ufficio.'),
        ],
        correlati=['vendita', 'assistenza-aziende', 'riparazione-smartphone-tablet'],
    ),
    # ------------------------------------------------------------------ su misura
    dict(
        slug='siti-web', gruppo='su-misura', icona='layout',
        nome='Landing page e siti web',
        breve="Pagine veloci e curate per presentare un'attività o un'offerta, pensate prima per il telefono e per farsi trovare su Google.",
        titolo='Landing page e siti web',
        sotto='Siti veloci e chiari, pensati prima per il telefono e per farsi trovare su Google.',
        intro=("Un sito che faccia capire in pochi secondi cosa fai e porti le persone a chiamarti, scriverti o "
               "venire da te. Veloce, chiaro, pensato prima per il telefono."),
        cosa=[
            'Landing page per un servizio, un evento o una campagna',
            'Siti vetrina per attività e professionisti',
            'Testi e struttura pensati per Google',
            'Pulsanti per chiamare, WhatsApp, mappa e orari',
            'Collegamento con la scheda Google e le recensioni',
            'Rifacimento di siti esistenti, anche WordPress',
        ],
        passi=PASSI_SU_MISURA,
        faq=[('Posso cambiare i testi da solo?', 'Sì: se lo vuoi, lo realizziamo in modo che testi, foto e prezzi si cambino facilmente.')] + FAQ_SU_MISURA,
        correlati=['visibilita-google', 'gestionali', 'app'],
    ),
    dict(
        slug='gestionali', gruppo='su-misura', icona='dashboard',
        nome='Gestionali su misura',
        breve='Clienti, preventivi, fatture, magazzino, appuntamenti: un programma costruito sul tuo modo di lavorare, non il contrario.',
        titolo='Gestionali su misura',
        sotto='Un programma costruito su come lavori tu, dal computer, dal tablet o dal telefono.',
        intro=("Invece di adattarti a un software pensato per tutti, un gestionale fatto sul tuo modo di lavorare. "
               "Si usa dal browser, su computer, tablet e telefono, senza installare niente."),
        cosa=[
            'Clienti, fornitori e anagrafiche',
            'Preventivi, fatture, DDT, ricevute e scontrini',
            'Magazzino e listini',
            'Schede di lavoro e di riparazione numerate',
            'Appuntamenti e promemoria',
            'Incassi e statistiche per periodo',
            'Sezioni protette da password',
            'Stampe e PDF con il tuo logo',
        ],
        esempio=True,
        passi=PASSI_SU_MISURA,
        faq=[
            ('Serve installare qualcosa?', 'No: si usa dal browser, anche da telefono. [[I dati sono salvati in modo sicuro, con copie di backup.]]'),
            ('Posso partire dai dati che ho già?', '[[Sì: possiamo importare clienti e articoli da Excel o dal vecchio programma.]]'),
        ] + FAQ_SU_MISURA,
        correlati=['documenti-pdf', 'automazioni', 'app'],
    ),
    dict(
        slug='app', gruppo='su-misura', icona='smartphone', da_confermare=True,
        nome='App per telefono e computer',
        breve='App che funzionano dal browser e si installano sul telefono con un tocco, senza passare dagli store.',
        titolo='App per telefono e computer',
        sotto='Si aprono dal browser e si installano sul telefono con un tocco, senza store.',
        intro=("App che si installano sulla schermata del telefono con un tocco, senza passare da App Store o "
               "Google Play. Un solo progetto che funziona su telefono, tablet e computer."),
        cosa=[
            'App per i clienti: prenotazioni, cataloghi, tessere fedeltà',
            'App interne per il personale',
            'Funzionano anche con una connessione debole',
            'Aggiornamenti immediati, senza reinstallare',
            'Accesso con password e profili diversi',
        ],
        passi=PASSI_SU_MISURA,
        faq=FAQ_SU_MISURA,
        correlati=['gestionali', 'siti-web', 'automazioni'],
    ),
    dict(
        slug='automazioni', gruppo='su-misura', icona='zap', da_confermare=True,
        nome='Automazioni',
        breve="I lavori ripetitivi fatti da soli: promemoria ai clienti, email, report, dati che passano da un programma all'altro.",
        titolo='Automazioni per la tua attività',
        sotto='I lavori ripetitivi fatti da soli, mentre tu pensi al resto.',
        intro=("Le attività ripetitive che ti rubano tempo possono farsi da sole: promemoria, email, report, "
               "dati copiati da un programma all'altro."),
        cosa=[
            'Promemoria ai clienti: appuntamenti, ritiri, scadenze',
            'Email e messaggi inviati al momento giusto',
            'Report e riepiloghi periodici',
            'Dati passati tra programmi, fogli Excel e gestionale',
            'Backup automatici',
        ],
        passi=PASSI_SU_MISURA,
        faq=FAQ_SU_MISURA,
        correlati=['gestionali', 'documenti-pdf', 'app'],
    ),
    dict(
        slug='documenti-pdf', gruppo='su-misura', icona='file', da_confermare=True,
        nome='Documenti e stampe automatiche',
        breve='Preventivi, schede, etichette e cartellini generati in PDF con i tuoi dati e il tuo logo, pronti da stampare o inviare.',
        titolo='Documenti e stampe automatiche',
        sotto='PDF con i tuoi dati e il tuo logo, pronti da stampare, inviare o condividere.',
        intro=("Preventivi, schede, etichette, cartellini e ricevute che si compilano da soli con i tuoi dati "
               "e il tuo logo, pronti da stampare, mandare per email o condividere su WhatsApp."),
        cosa=[
            'Documenti PDF impaginati con cura',
            'Stampa su A4, su carta termica per scontrini e su etichette',
            'QR code, per esempio per le recensioni',
            'Invio per email o WhatsApp',
            'Cartellini dei prezzi per la vetrina',
        ],
        esempio=True,
        passi=PASSI_SU_MISURA,
        faq=FAQ_SU_MISURA,
        correlati=['gestionali', 'automazioni', 'visibilita-google'],
    ),
    dict(
        slug='visibilita-google', gruppo='su-misura', icona='search', da_confermare=True,
        nome='Visibilità su Google',
        breve='Scheda Google, recensioni e ottimizzazione per le ricerche in zona: farti trovare da chi cerca vicino a te.',
        titolo='Visibilità su Google',
        sotto='Farti trovare da chi cerca quello che fai, vicino a te.',
        intro=("Scheda Google curata, recensioni e un sito ottimizzato per le ricerche in zona: così ti trova chi "
               "cerca quello che fai, proprio vicino a te."),
        cosa=[
            'Creazione e cura della scheda Google: orari, foto, categorie',
            'Raccolta di recensioni, anche con un QR code',
            'Sito ottimizzato per le ricerche locali',
            'Dati strutturati con orari e indirizzo',
            'Statistiche: visite, chiamate e richieste di indicazioni',
        ],
        passi=PASSI_SU_MISURA,
        faq=FAQ_SU_MISURA,
        correlati=['siti-web', 'documenti-pdf', 'gestionali'],
    ),
]

PER_SLUG = {s['slug']: s for s in SERVIZI}

# Problemi cliccabili della bozza A, come "Problemi con il PC?" di SoccorsoPc
PROBLEMI = [
    ('Il PC non si accende', 'riparazione-pc-mac', 'laptop'),
    ('Schermo rotto', 'riparazione-smartphone-tablet', 'smartphone'),
    ('Virus o computer lento', 'virus-sicurezza', 'shield'),
    ('Ho perso dei dati', 'recupero-dati', 'database'),
]

MARCHE = ['Apple', 'HP', 'Lenovo', 'Asus', 'Acer', 'Dell', 'Microsoft', 'Samsung', 'Huawei', 'Xiaomi']
