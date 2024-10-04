
class Tommaso:

    def __init__(self):
        print('Hai incontrato Tommaso Muraca, Web developer e formatore IT')
        print('''Benvenuto nel regno dei dati strutturati, per battermi dovrai rispondere correttamente almeno a 2 domande''')
        #self.mod = input("Scegli l'arma che vuoi utilizzare:\n 1. SQL 2.Liste 3.Dizionari")
        self.punteggio = 0

    def prima_domanda(self):
        risposta = input('Quale linguaggio è maggiormente utilizzato per interagire con Database Relazionali?')
        if risposta.lower() == 'sql':
            print('Risposta corretta!!')
            self.punteggio += 1
        else:
            print('Risposta errata!!')
            

    def seconda_domanda(self):
        risposta = input('Quale tipo di dato in Python è il migliore per tutto?')
        if risposta.lower() == 'dizionario' or risposta.lower() == 'dizionari':
            print('Risposta corretta!!')
            self.punteggio += 1
        else:
            print('Risposta errata!!')
            return False

    def terza_domanda(self):
        risposta = input('Qual è la mia libreria Python preferita?')
        if risposta.lower() == 'pandas':
            print('Risposta corretta!!')
            self.punteggio += 1
        else:
            print('Risposta errata!!')
        if risposta.lower() == 'numpy':
            print('NO! non è numpy!!')
    def vittoria(self):
        if self.punteggio > 1:
            print('Complimenti, mi hai sconfitto!! Non montarti la testa, troverai altri nemici!!')
            return True
        else:
            print('Non sei riuscito a battermi ahahahah, dovrai ripetere')
            return False

    def get_punteggio(self):
        return self.punteggio

if __name__ == '__main__':
    Tom = Tommaso()
    while Tom.get_punteggio() < 2:
        Tom.prima_domanda()
        Tom.seconda_domanda()
        Tom.terza_domanda()
        Tom.vittoria()