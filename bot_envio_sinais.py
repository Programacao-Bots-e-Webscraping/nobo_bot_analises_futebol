from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import requests

mensagens_enviadas = []
service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get('https://www.playscores.com/scanner-futebol-online/ao-vivo')

def enviar_mensagem(mensagem):
    
    chat_id = '-1002112763550'
    token = '6956796797:AAG7dXDItCrva1SUjiMxzaTVolaJPcjx9B4'
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={mensagem}'
    response = requests.post(url)


while True:
    sleep(5)
    jogos = driver.find_elements(By.TAG_NAME,'app-fixture-list-line')

    for jogo in jogos:
        lista = jogo.text.split('\n')
        try:
            tempo = int(lista[0].replace("'",''))
            if (35 <= tempo <= 40) or (75 <= tempo <= 85):
                if tempo < 45:
                    t = '1'
                else:
                    t = '2'
                lista_inf = lista[1:-1]
                inf = [lista_inf[i:i+2] for i in range(0,len(lista_inf),2)]
                controle_mensagens = f'{inf[0][0]} x {inf[0][1]}{t}'
                if (float(inf[5][0]) >= 0.0 or float(inf[5][1]) >= 0.0) and controle_mensagens not in mensagens_enviadas:
            
            
                    mensagem = f'''
    Jogo: {inf[0][0]} x {inf[0][1]}
    Tempo: {tempo} min
    Placar: {inf[1][0]} - {inf[1][1]}
    Escanteios: {inf[10][0]} - {inf[10][1]}
    Cartão Amarelo: {inf[15][0]} - {inf[15][1]}
    Cartão Vermelho: {inf[14][0]} - {inf[14][1]}
    Appm ult. 10 min: {inf[6][0]} - {inf[6][1]}
    Appm Jogo: {inf[5][0]} - {inf[5][1]}
    '''
                    enviar_mensagem(mensagem)
                    mensagens_enviadas.append(controle_mensagens)
            

        except Exception as e:
            print(e)
            pass
    sleep(25)
