from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from login import Login
import time

# Caminho para o driver do Chrome
#driver_path = 'C:\\chromedriver\\chromedriver.exe'
driver_path = '/Users/raylanaraujo/chromedriver/chromedriver'

# Criação da instância do navegador usando o Service
service = Service(driver_path)
navegador = webdriver.Chrome(service=service)

# Criando uma instância da classe Login
login = Login()  # Instanciando a classe Login para acessar os dados

# Acessando a página de login
navegador.get("https://id.udesc.br/Geral/Login/formLogin/")

# Espera até que o campo de entrada esteja visível
time.sleep(2)

# Localizando o campo de entrada de usuário e enviando dados
entrada1 = navegador.find_element(By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/form/div[2]/input')
entrada1.send_keys(login.usuario)  # Envia o valor do campo 'usuario'

# Localizando o campo de entrada de senha e enviando dados
entrada2 = navegador.find_element(By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/form/div[3]/input')
entrada2.send_keys(login.senha)  # Envia o valor do campo 'senha'

# Espera um pouco para verificar se o dado foi inserido
time.sleep(2)

# Enviar o formulário pressionando ENTER
entrada2.send_keys(Keys.RETURN)

# Loop para manter o navegador aberto
try:
    while True:
        time.sleep(1)  # Mantém o loop ativo
except KeyboardInterrupt:
    print("Fechando o navegador...")
    navegador.quit()
