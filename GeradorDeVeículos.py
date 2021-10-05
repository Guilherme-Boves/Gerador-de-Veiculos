from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# driver.execute_script("document.getElementById('"+campo+"').scrollIntoView();") // Comando para subir o Scroll da tela

driver = webdriver.Chrome()

driver.get("https://www.4devs.com.br/gerador_de_veiculos")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='estado']")))
estado = Select(driver.find_element_by_xpath("//select[@id='estado']"))
estado.select_by_visible_text("GO")

driver.find_element_by_xpath("//input[@id='pontuacao_nao']").click()

marca = Select(driver.find_element_by_xpath("//select[@id='fipe_codigo_marca']"))
marca.select_by_visible_text("Audi")

driver.find_element_by_xpath("//input[@id='bt_gerar']").click()

time.sleep(2)
# webdriver(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='marca']")))

marcaCarro = driver.find_element_by_id("marca").get_attribute("value")
modelo = driver.find_element_by_xpath("//input[@id='modelo']").get_attribute("value")
ano = driver.find_element_by_xpath("//input[@id='ano']").get_attribute("value")
renavam = driver.find_element_by_xpath("//input[@id='renavam']").get_attribute("value")
placa = driver.find_element_by_xpath("//input[@id='placa_veiculo']").get_attribute("value")
cor = driver.find_element_by_xpath("//input[@id='cor']").get_attribute("value")

print("Modelo: " + marcaCarro)
print("Ano: " + ano)
print("RENAVAM: " + renavam)
print("Placa: " + placa)
print("Cor: " + cor)

time.sleep(20)


