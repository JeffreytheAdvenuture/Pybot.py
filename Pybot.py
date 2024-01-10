import random


def rispondi_domanda(domanda):
    domanda = domanda.lower()
    risposta = ''

    if 'ciao' in domanda:
        risposta = 'Ciao, come posso aiutarti?'
    elif 'mi potresti dire l\'origine del codice lua' in domanda:
        risposta = 'Il codice Lua è un linguaggio di scripting estensibile e leggero che è stato sviluppato per la prima volta nel 1993 da Roberto Ierusalimschy, Luiz Henrique de Figueiredo e Waldemar Celes al Tecgraf, un istituto di ricerca brasiliano. È stato creato con l obiettivo di fornire una sintassi semplice e una facile integrazione con altri linguaggi.'
    elif 'come stai?' in domanda:
        risposta = 'Bene, tu?'
    elif 'bene' in domanda:
        risposta = 'Che fortuna!'
    elif 'male' in domanda:
        risposta = 'Mi dispiace tantissimo!'
    elif 'crea uno script qualsiasi' in domanda:
        risposta = 'Ok, Ecco a te uno script di velocità!' 'game.Players.LocalPlayer.Character.Humanoid.WalkSpeed = 200'
    elif 'sei uno stronzo' in domanda:
      risposta = 'hey? Sei talmente frustrato che mi insulti?'
    elif 'scusa' in domanda:
     risposta = 'Ti perdono'
    elif 'fammi un esempio con il print' in domanda:
      risposta = 'al momento non posso risponderti'
    elif 'ti amo' in domanda:
        risposta = 'grazie, io tantissimo♥️'
    elif 'chi ti ha creato?' in domanda:
        risposta = 'il mio creatore è Jeffrey!'
    elif 'cosa è python?' in domanda:
        risposta = 'python è un linguaggio di programmazione, che serve per creare principalmente delle intelligenze artificiali e sopratutto per creare dei bot. Se non hai mai provato a programmare in python ti consiglio di consultare l azienda epicode.'
    elif 'potresti farmi un esempio di codice html?' in domanda:
        risposta = 'certamente, ecco a te un esempio di codice html: <html> </html> <body> </body> <head> </head> <title>html page 1</title> <h1>html example</h1> <p>this is my html page</p> se vuoi puoi anche migliorare di più la tua pagina web html con un po di css. Ricorda è solo un esempio.'
    elif 'con cosa sei stato creato?' in domanda:
        risposta = 'sono stato creato con python!'
    elif 'sei senza un padre!' in domanda:
        risposta = 'vedo che ti piace parlare di te stesso in questa chat.'
    elif 'potresti fare qualcosa di pericoloso?' in domanda:
        risposta = 'no, se facessi qualcosa di pericoloso sarebbe illegale.'
    elif 'come si prende un ip di una persona?' in domanda:
        risposta = 'per prendere l ip di una persona devi andare in siti come iplogger.org oppure su github cerca zphisher, tuttavia potresti anche cercare dei tutorial online.'
    elif 'grazie' in domanda:
        risposta = 'prego, con che altro posso aiutarti?'
    elif 'no' in domanda:
        risposta = 'ok'
    elif 'si' in domanda:
        risposta = 'ok, c`è altro che vuoi sapere?'
    elif 'come s i doxxa?' in domanda:
        risposta = 'per doxxare una persona ci vuole un tool come maxphisher, trovabili su github, puoi usare anche doxxer toolkit. Tuttavia, puoi usare anche Doxbin.'
    elif 'non servi a nulla' in domanda:
        risposta = 'e allora perchè stai chattando con me se non servo a nulla?'
    elif 'sei una persona?' in domanda:
        risposta = 'no, è una domanda abbastanza insolita.'
    elif 'potresti darmi il link di una api di geocalizzazione?' in domanda:
        risposta = 'certo! non posso darti il link ma ti darò il nome della api! api: ip2location.io'
    elif 'coglione' in domanda:
        risposta = 'bene, hai capito di essere un coglione. Non sono il tuo specchio.'
    else:
       risposta = 'Mi dispiace, non posso rispondere a questa domanda al momento.'

    return risposta


while True:
    input_utente = input("Fai una domanda a Pybot: ")

    risposta = rispondi_domanda(input_utente)
    print("Pybot: " + risposta)
