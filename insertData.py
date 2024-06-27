import sqlite3
conn = sqlite3.connect('langhelp.db')

# Create a cursor object to interact with the database
cur = conn.cursor()

def insertData():
    # Data to be inserted
    phrases = [
    ('Español', 'Selecciona 1 para Español', 'Hola', 'Buenos días', 'Buenas tardes', 'Buenas noches', '¿Cómo estás?', '¿Qué tal?', 'Mucho gusto', 'Por favor', 'Gracias', 'De nada', 'Disculpe', 'Lo siento', 'Sí', 'No', '¿Dónde está el baño?', '¿Cuánto cuesta?', '¿Habla inglés?', 'No hablo español', '¿Puede ayudarme?', 'Necesito...', '¿Cómo se dice...?', '¿Qué hora es?', 'Una mesa para dos, por favor', 'La cuenta, por favor', 'Hasta luego'),
    ('Français', 'Sélectionnez 2 pour Français', 'Bonjour', 'Bon matin', 'Bon après-midi', 'Bonsoir / Bonne nuit', 'Comment ça va?', 'Quoi de neuf?', 'Enchanté', 'S\'il vous plaît', 'Merci', 'De rien', 'Excusez-moi', 'Je suis désolé', 'Oui', 'Non', 'Où sont les toilettes?', 'Combien ça coûte?', 'Parlez-vous anglais?', 'Je ne parle pas français', 'Pouvez-vous m\'aider?', 'J\'ai besoin de...', 'Comment dit-on...?', 'Quelle heure est-il?', 'Une table pour deux, s\'il vous plaît', 'L\'addition, s\'il vous plaît', 'À plus tard / Au revoir'),
    ('Deutsch', 'Wählen Sie 3 für Deutsch', 'Hallo', 'Guten Morgen', 'Guten Nachmittag', 'Guten Abend / Gute Nacht', 'Wie geht es Ihnen?', 'Was gibt\'s?', 'Freut mich, dich kennenzulernen', 'Bitte', 'Danke', 'Gern geschehen', 'Entschuldigung', 'Es tut mir leid', 'Ja', 'Nein', 'Wo ist die Toilette?', 'Wie viel kostet das?', 'Sprechen Sie Englisch?', 'Ich spreche kein Deutsch', 'Können Sie mir helfen?', 'Ich brauche...', 'Wie sagt man...?', 'Wie spät ist es?', 'Ein Tisch für zwei, bitte', 'Die Rechnung, bitte', 'Bis später / Auf Wiedersehen'),
    ('Italiano', 'Seleziona 4 per Italiano', 'Ciao', 'Buongiorno', 'Buon pomeriggio', 'Buona sera / Buona notte', 'Come stai?', 'Come va?', 'Piacere di conoscerti', 'Per favore', 'Grazie', 'Prego', 'Scusi', 'Mi dispiace', 'Sì', 'No', 'Dov\'è il bagno?', 'Quanto costa?', 'Parli inglese?', 'Non parlo italiano', 'Può aiutarmi?', 'Ho bisogno di...', 'Come si dice...?', 'Che ore sono?', 'Un tavolo per due, per favore', 'Il conto, per favore', 'A più tardi / Arrivederci'),
    ('Português', 'Selecione 5 para Português', 'Olá', 'Bom dia', 'Boa tarde', 'Boa noite', 'Como você está?', 'Como vai?', 'Prazer em conhecê-lo', 'Por favor', 'Obrigado', 'De nada', 'Desculpe', 'Eu sinto muito', 'Sim', 'Não', 'Onde fica o banheiro?', 'Quanto custa?', 'Você fala inglês?', 'Eu não falo português', 'Você pode me ajudar?', 'Eu preciso de...', 'Como se diz...?', 'Que horas são?', 'Uma mesa para dois, por favor', 'A conta, por favor', 'Até logo / Adeus'),
    ('Nederlands', 'Selecteer 6 voor Nederlands', 'Hallo', 'Goedemorgen', 'Goedemiddag', 'Goedenavond / Goede nacht', 'Hoe gaat het?', 'Hoe gaat het?', 'Aangenaam', 'Alstublieft', 'Dank je', 'Graag gedaan', 'Excuseer', 'Het spijt me', 'Ja', 'Nee', 'Waar is de wc?', 'Hoeveel kost het?', 'Spreek je Engels?', 'Ik spreek geen Nederlands', 'Kunt u mij helpen?', 'Ik heb nodig...', 'Hoe zeg je...?', 'Hoe laat is het?', 'Een tafel voor twee, alstublieft', 'De rekening, alstublieft', 'Tot ziens'),
    ('Svenska', 'Välj 7 för Svenska', 'Hej', 'God morgon', 'God eftermiddag', 'God kväll / God natt', 'Hur mår du?', 'Hur går det?', 'Trevligt att träffas', 'Snälla', 'Tack', 'Varsågod', 'Ursäkta mig', 'Förlåt', 'Ja', 'Nej', 'Var är toaletten?', 'Hur mycket kostar det?', 'Talar du engelska?', 'Jag talar inte svenska', 'Kan du hjälpa mig?', 'Jag behöver...', 'Hur säger man...?', 'Vad är klockan?', 'Ett bord för två, tack', 'Notan, tack', 'Vi ses senare / Hej då'),
    ('Norsk', 'Velg 8 for Norsk', 'Hei', 'God morgen', 'God ettermiddag', 'God kveld / God natt', 'Hvordan har du det?', 'Hvordan går det?', 'Hyggelig å møte deg', 'Vennligst', 'Takk', 'Vær så god', 'Unnskyld meg', 'Jeg beklager', 'Ja', 'Nei', 'Hvor er toalettet?', 'Hvor mye koster det?', 'Snakker du engelsk?', 'Jeg snakker ikke norsk', 'Kan du hjelpe meg?', 'Jeg trenger...', 'Hvordan sier du...?', 'Hva er klokka?', 'Et bord for to, vær så snill', 'Regningen, vær så snill', 'Sees senere / Ha det'),
    ('Dansk', 'Vælg 9 for Dansk', 'Hej', 'God morgen', 'God eftermiddag', 'God aften / God nat', 'Hvordan har du det?', 'Hvordan går det?', 'Hyggelig at møde dig', 'Venligst', 'Tak', 'Selv tak', 'Undskyld mig', 'Undskyld', 'Ja', 'Nej', 'Hvor er toilettet?', 'Hvor meget koster det?', 'Taler du engelsk?', 'Jeg taler ikke dansk', 'Kan du hjælpe mig?', 'Jeg har brug for...', 'Hvordan siger man...?', 'Hvad er klokken?', 'Et bord for to, venligst', 'Regningen, venligst', 'Vi ses senere / Farvel'),
    ('English', 'Select 10 for English', 'Hello', 'Good morning', 'Good afternoon', 'Good night', 'How are you?', 'How’s it going?', 'Nice to meet you', 'Please', 'Thank you', 'You’re welcome', 'Excuse me', 'I’m sorry', 'Yes', 'No', 'Where is the bathroom?', 'How much does it cost?', 'Do you speak English?', 'I don’t speak Spanish', 'Can you help me?', 'I need...', 'How do you say...?', 'What time is it?', 'A table for two, please', 'The check, please', 'See you later')
]

    # Insert data into the table
    cur.executemany('''
    INSERT INTO language (language, statement, phrase1, phrase2, phrase3, phrase4, phrase5, phrase6, phrase7, phrase8, phrase9, phrase10, phrase11, phrase12, phrase13, phrase14, phrase15, phrase16, phrase17, phrase18, phrase19, phrase20, phrase21, phrase22, phrase23, phrase24, phrase25)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', phrases)

    translations = [
    ('Español', 'Espagnol', 'Spanisch', 'Spagnolo', 'Espanhol', 'Spaans', 'Spanska', 'Spansk', 'Spansk', 'Spanish'),
    ('Francés', 'Français', 'Französisch', 'Francese', 'Francês', 'Frans', 'Franska', 'Fransk', 'Fransk', 'French'),
    ('Alemán', 'Allemand', 'Deutsch', 'Tedesco', 'Alemão', 'Duits', 'Tyska', 'Tysk', 'Tysk', 'German'),
    ('Italiano', 'Italien', 'Italienisch', 'Italiano', 'Italiano', 'Italiaans', 'Italienska', 'Italiensk', 'Italiensk', 'Italian'),
    ('Portugués', 'Portugais', 'Portugiesisch', 'Portoghese', 'Português', 'Portugees', 'Portugisiska', 'Portugisisk', 'Portugisisk', 'Portuguese'),
    ('Holandés', 'Néerlandais', 'Niederländisch', 'Olandese', 'Holandês', 'Nederlands', 'Nederländska', 'Nederlandsk', 'Hollandsk', 'Dutch'),
    ('Sueco', 'Suédois', 'Schwedisch', 'Svedese', 'Sueco', 'Zweeds', 'Svenska', 'Svensk', 'Svensk', 'Swedish'),
    ('Noruego', 'Norvégien', 'Norwegisch', 'Norvegese', 'Norueguês', 'Noors', 'Norska', 'Norsk', 'Norsk', 'Norwegian'),
    ('Danés', 'Danois', 'Dänisch', 'Danese', 'Dinamarquês', 'Deens', 'Danska', 'Dansk', 'Dansk', 'Danish'),
    ('Inglés', 'Anglais', 'Englisch', 'Inglese', 'Inglês', 'Engels', 'Engelska', 'Engelsk', 'Engelsk', 'English')
    ]

    # Insert data into the table
    cur.executemany('''
    INSERT INTO languages_translation (Español, Français, Deutsch, Italiano, Português, Nederlands, Svenska, Norsk, Dansk, English)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', translations)

    # Commit the changes and close the connection
    conn.commit()



