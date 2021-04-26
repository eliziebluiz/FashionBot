from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
import random

class InstagramBot:
    def __init__(self, username, password, mensagem, contatos):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) # Coloque o caminho para o seu geckodriver aqui
        self.mensagem = mensagem
        self.contatos = contatos
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            # print('já estamos na página de login')
            pass
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(4, 6))
        user_element.send_keys(self.username)
        time.sleep(random.randint(4, 6))
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(random.randint(4, 6))
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(4, 6))
        driver.get("https://www.instagram.com/"+self.username+"/")
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        # print(pic_hrefs)

        for link in pic_hrefs:
           # print(link)
           if("https://www.instagram.com/p/" in link):
               self.mensagem = "Acesse o link para seguir e ficar por dentro de todas as novidades da loja: "+link
        print(self.mensagem)
        # if "/p/" in pic_hrefs:
        #     i=pic_hrefs.index()
        #     print(pic_hrefs[i])
        # for pic_href in pic_hrefs:
        #   pic_href.index("https://www.instagram.com/p")

    def buscar_contato(self, contato):
      driver = self.driver
      driver.get('https://web.whatsapp.com/')
      time.sleep(30)
      campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
      time.sleep(3)
      campo_pesquisa.click()
      campo_pesquisa.send_keys(contato)
      campo_pesquisa.send_keys(Keys.ENTER)

    def enviar_mensagem(self, mensagem):
      driver = self.driver
      campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
      campo_mensagem[1].click()
      time.sleep(3)
      campo_mensagem[1].send_keys(mensagem)
      time.sleep(10)
      campo_mensagem[1].send_keys(Keys.ENTER)

    def buscar_contatoTelegram(self, contato):
      driver = self.driver
      driver.get('https://web.telegram.org/#/im')
      time.sleep(60)
      campo_pesquisa = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[1]/div[1]/div/input')

      time.sleep(3)
      campo_pesquisa.click()
      campo_pesquisa.send_keys(contato)
      campo_pesquisa.send_keys(Keys.ENTER)

    def enviar_mensagemTelegram(self, mensagem):
      driver = self.driver
      campo_mensagem = driver.find_elements_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]')
      campo_mensagem[0].click()
      time.sleep(3)
      campo_mensagem[0].send_keys(mensagem)
      time.sleep(10)
      campo_mensagem[0].send_keys(Keys.ENTER)



#https://web.telegram.org/

fashionBot = InstagramBot(
    "elizieb.pereira", "ebeye2313", "", ['Notas']
)  # Entre com o usuário e senha aqui

condiction=int(input("Digite (1)-Para digitar sua mensagem (2)-Para o sistema logar no instagram e gerar automatica: "))

if condiction == 1:
  fashionBot.mensagem = input("Digite sua mensagem:")
else: fashionBot.login()

conduct=int(input("Digite (1)-Whatsapp (2)- Telegram: "))

if conduct == 1:
    for contato in fashionBot.contatos:
        fashionBot.buscar_contato(contato)
        fashionBot.enviar_mensagem(fashionBot.mensagem)
else:
    for contato in fashionBot.contatos:
        fashionBot.buscar_contatoTelegram(contato)
        fashionBot.enviar_mensagemTelegram(fashionBot.mensagem)