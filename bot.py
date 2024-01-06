from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get('https://www.playscores.com/scanner-futebol-online/ao-vivo')


sleep(5)
jogos = driver.find_elements(By.TAG_NAME,'app-fixture-list-line')

for jogo in jogos:
    lista_inf = jogo.text.split('\n')[1:-1]
    print([lista_inf[i:i+2] for i in range(0,len(lista_inf),2)])
