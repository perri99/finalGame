from tommaso import Tommaso
from final_boss import PaoloCasciato

#primo livello
Tom = Tommaso()
while Tom.get_punteggio() < 2:
    Tom.prima_domanda()
    Tom.seconda_domanda()
    Tom.terza_domanda()
    Tom.vittoria()

#livello finale
        
paolo=PaoloCasciato()
vittoria= paolo.vittoria()
if vittoria == True:
    print('Hai vinto il gioco')
else:
    print('Sei caduto miseramente, game over')