class Mirko:
    def __init__(self):
        self.punteggio = 0
        print("MUAHAHAHA sono Mirko, OOP Senior programmer, Game director e docente IT")
        print("Per battermi dovrai affrontare la mia armata di domande sull'OOP. Al mio segnale scatenate l'Astrazionee!\n")


    def prima_domanda(self):
        print("Il Mago dell'OOP ti chiede: cosa succede quando un giovane apprendista eredita i poteri di un mago più anziano?")
        print("Contempla le risposte:\na) L'apprendista può usare gli stessi incantesimi del mago \nb) L'apprendista perde tutti i suoi incantesimi originali \nc) L'apprendista può creare nuovi incantesimi dal nulla")
        risposta = input("La tua risposta: ")
        if risposta.lower() == "a":
            print("Bene! Hai superato la prima prova!\n")
            self.punteggio += 1
        else:
            print("Prima prova fallita!\n")
    
    def seconda_domanda(self):
        print("Il Guardiano delle Classi ti sfida: ogni volta che crei una nuova creatura magica, quale incantesimo lancia il costruttore?")
        print("Possibili risposte:\na) Evoca nuovi metodi magici \nb) Inizializza i suoi attributi, preparandola all'azione \nc) Distrugge tutti i nemici nel raggio di 10 metri")
        risposta = input("La tua risposta: ")
        if risposta.lower() == "b":
            print("Bene! Hai superato la seconda prova!\n")
            self.punteggio += 1
        else:
            print("Seconda prova fallita!\n")

    def terza_domanda(self):
        print("Il Saggio delle Tre Regole ti guarda con occhi penetranti e domanda:\nQuali sono le tre regole fondamentali che ogni apprendista del codice deve rispettare per padroneggiare la magia dell'OOP?")

        risposte = ["polimorfismo", "incapsulamento", "ereditarietà"]

        count = 0
        while True:
            uno = input("Prima risposta: ")
            if uno.lower() in risposte:
                print("Bene! Ne serve un'altra!")
                count +=1
            else:
                print("Male! Hai altri due tentativi!")

            due = input("Seconda risposta: ")
            if due.lower() in risposte and count == 1:
                print("Bene! Sei un degno avversario!")
                self.punteggio += 1
                break
            elif due.lower() not in risposte and count == 1:
                print("Hai la tua ultima possibilità!")
            elif due.lower() in risposte and count == 0:
                print("Bene! Ne serve un'altra!")
                count+=1
            

            tre = input("Terza risposta: ")
            if tre.lower() in risposte and count == 1:
                print("Bene! Sei un degno avversario!")
                self.punteggio += 1
                break
            else:
                print("Terza sfida fallita! L'astrazione vince sempre!")
                break


    def risultato(self):
        print()
        if self.punteggio == 3:
            print("Hai superato tutte le sfide! Sei un vero mago dell'OOP!")
            x = input("Domanda bonus:\nQual è la caratteristica migliore dell'OOP? ")
            if x.lower() == 'astrazione':
                print("Ah, l'Astrazione! Il potere più arcano dell'OOP. Solo i programmatori più saggi comprendono il suo vero significato. Come un antico incantatore che cela il complesso dietro veli invisibili, così l'astrazione nasconde i dettagli del codice, mostrando solo ciò che è necessario. Ricorda, giovane apprendista: la chiave per dominare l'OOP è vedere oltre il codice, rendendo semplici anche i meccanismi più intricati. Al mio segnale... SCATENATE L'ASTRAZIONE!\n")
                print("Hai guadagnato un consiglio per la prossima sfida: le risposte giuste sono sbagliate!")
            else:
                print("Hai fallito la domanda bonus! Non ti sarà concesso alcun consiglio!")
            return True
        elif self.punteggio == 2:
            print("Hai superato due sfide, me la accollo!")
            return True
        elif self.punteggio == 1:
            print("Hai superato una sola sfida..!")
            return False
        else:
            print("Hai fallito tutte le sfide! Non sei degno dell'astrazione!")
            return False

mirko = Mirko()
mirko.prima_domanda()
mirko.seconda_domanda()
mirko.terza_domanda()
mirko.risultato()
        
        
        