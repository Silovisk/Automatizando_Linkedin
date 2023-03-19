import random

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

servico = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=servico)

nav.get("https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in/")

email = "email@email.com"
senha = "senha"
profissao = "Engenheiro de Software"

time.sleep(3)
nav.find_element(By.ID, 'username').send_keys(email)
time.sleep(3)
nav.find_element(By.ID, 'password').send_keys(senha)
time.sleep(3)
nav.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

time.sleep(5)
nav.find_element(By.XPATH, '//*[@id="global-nav-search"]/div').click()
time.sleep(3)
nav.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input').send_keys(profissao + Keys.ENTER)
time.sleep(3)
nav.find_element(By.XPATH, '//button[text()="Pessoas"]').click()
time.sleep(3)

all_buttons = nav.find_elements(By.TAG_NAME, 'button')
all_pages = nav.find_elements(By.TAG_NAME, 'a')


conect_buttons = [btn for btn in all_buttons if btn.text == "Conectar"]

for btn in conect_buttons:
    nav.execute_script("arguments[0].click();", btn)
    time.sleep(5)

    adicionar_nota = nav.find_element(By.XPATH, "//button[@aria-label='Adicionar nota']")
    nav.execute_script("arguments[0].click();", adicionar_nota)
    time.sleep(2)
    frase = "Olá, Engenheiro de Software do LinkedIn! Sou um estudante dedicado em busca de um estágio na área de " \
            "tecnologia. Animado para aplicar minhas habilidades e aprender com os melhores, gostaria de fazer parte " \
            "do seu network para expandir minha rede e aumentar minhas chances de sucesso nesta jornada!"

    for letra in frase:
        nav.find_element(By.XPATH, '//*[@id="custom-message"]').send_keys(letra)
        time.sleep(random.randint(1, 10) / 60)

    time.sleep(5)
    send = nav.find_element(By.XPATH, "//button[@aria-label='Enviar agora']")
    nav.execute_script("arguments[0].click();", send)
    time.sleep(2)

    pags = 2
    while True:
        try:
            pag = nav.find_element(By.XPATH, f"//button[@aria-label='Página {pags}']")
            nav.execute_script("arguments[0].click();", pag)
            pags += 1
            time.sleep(10)
        except:
            break

time.sleep(9600)
