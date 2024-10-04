from tommaso import Tommaso
from final_boss import PaoloCasciato

vite = 3

while vite > 0:
    #primo livello
    Tom = Tommaso()
    while Tom.get_punteggio() < 2:
        Tom.prima_domanda()
        Tom.seconda_domanda()
        Tom.terza_domanda()
        if Tom.vittoria() == False: 
            vite -=1
            if vite == 0: break  

    #livello finale
    if vite == 0: break        
    paolo = PaoloCasciato()
    vittoria = paolo.vittoria()
    if vittoria == True:
        #print('Hai vinto il gioco')
        vite = -1
    else:
        print('Sei caduto miseramente, hai perso una vita')
        vite -= 1

if vite == -1:
    print('Gioco finito, hai vinto!!')
else:
    print('Game Over, hai perso tutto')