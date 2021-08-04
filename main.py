from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os


mensagem = """Sua mensagem em uma unica linha"""

imagem = 'C:\\Paluch_Python\\dia_dos_pais.jpg'
contatos = ['554899766001','554891454301' ]
contador = 0
mensagem_enviada = 0
erro_mensagem = 0
for i in contatos:
    try:
        cliente = contatos[contador]
        contador = contador +1
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profile", "wpp")
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir={}".format(profile))
        driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
        driver.get(f'https://web.whatsapp.com/send?phone={cliente}&text&app_absent=1')
        time.sleep(5)
        #envia a imagem
        driver.find_element_by_css_selector("span[data-icon='clip']").click()
        attach = driver.find_element_by_css_selector("input[type='file']")
        attach.send_keys(imagem)
        time.sleep(2)
        #envia o texto dentro do input de texto da imagem, para enviar somente texto pegar outro xpath
        msg_box = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]')
        msg_box.send_keys(mensagem, Keys.ENTER)
        time.sleep(2)
        driver.stop_client()
        driver.close()
        mensagem_enviada = mensagem_enviada +1
    except Exception as erro:
        print(f'Erro: {erro}')
        time.sleep(4)
        erro_mensagem = erro_mensagem +1

print(f'Mensagens Enviadas: {mensagem_enviada}')
print(f'Mensagens com erro: {erro_mensagem}')

