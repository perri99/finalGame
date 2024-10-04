from PIL import Image


class PaoloCasciato:
    def __init__(self):
        print("E' stato stupido da parte tua affrontarmi, io sono Paolo Casciato, imperatore di tutte le Russie!\nOra affronta queste domande!")
        self.punteggio_paolo=0
        colore=input("Di che colore sono le persone peggiori che tu possa incontrare?")
        if colore.lower()=='rosso':
            print('Hai ragione, diffida sempre dalle persone rosse!')
        else:
            print('Errore da principiante! Questo ti costerà uno 0 nella tua valutazione!')
            self.punteggio_paolo+=1
        img = Image.open('cane.jfif')
        img.show()
        emozione=input('Sai dirmi l\'emozione di questo cagnolino?')
        if emozione.lower()=='felice' or emozione.lower()=='felicità':
            print('Bravo, vedo che il mio corso è stato utile!')
        else:
            print('No, hai sbagliato! Per te 24 ore ulteriori di SoftSkills!')
            self.punteggio_paolo+=1 
        libro=input('Comprerai il mio libro sulla comunicazione? (s/n)')
        if libro.lower()=='s':
            print('Scelta saggia, ragazzo, sentirmi parlare per 24 ore non è stato abbastanza!')
        else:
            print('Cosa? Ti sbagli  questo non è un conflitto di interessi!')
            self.punteggio_paolo+=1
    def vittoria(self):
        if self.punteggio_paolo>=2:
            print('Oh no, conosci tutte le mie debolezze, mi hai battuto!')
            return True
        else:
            print('Sei il perfetto schiavo delle SoftSkills, entreari a far parte della mia schiera di HR! ')
            return False
        
if __name__ == '__main__':
    vittoria=False
    while vittoria==False:        
        paolo=PaoloCasciato()
        vittoria= paolo.vittoria()
