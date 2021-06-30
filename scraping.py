# Pacotes
from selenium import webdriver 
import pymysql 
import pandas as pd 
import time 
import configparser

# Raspando os dados 
# Configurando o drive do chrome
drive = webdriver.Chrome(executable_path='chromedriver')

# Criando a estrutura da raspagem 
site = 'https://painelms.saude.gov.br/extensions/Portal_FAF/Portal_FAF.html'
drive.get(site)

# Acessando os Filtros 
time.sleep(40)
filtro = drive.find_element_by_xpath("//div[@class = 'Menu_App']") 
linha = filtro.find_element_by_xpath("//div[@id = 'CurrentSelections01']").find_element_by_xpath("//div[@class= 'buttons-end borderbox border-left']").find_elements_by_xpath("//div[@class='qv-subtoolbar-button toggle-button borderbox']")[1].click()
time.sleep(10)
campo = drive.find_element_by_xpath("//div[@class = 'qv-global-selections ng-scope ng-isolate-scope']").find_element_by_xpath("//section[@class='qv-gs-section']").find_element_by_xpath("//div[@class='qv-gs-scroll-container ng-isolate-scope']").find_elements_by_xpath("//div[@class='qv-listbox-text']")[1]
# Selecionando o Ano 
#box.click()
#search=box.find_element_by_xpath("//div[@class='qv-listbox-search']")
for i in range(2013,2020):
    time.sleep(15)
    box = campo.find_elements_by_xpath("//div[@class='qv-gs-listbox ng-scope']")[1].find_elements_by_xpath("//header[@class='qv-object-header']")[9].find_elements_by_xpath("//a[@class='qv-object-search lui-icon lui-icon--search ng-scope']")[1]
    box.click()
    search=box.find_element_by_xpath("//div[@class='qv-listbox-search']")
    caixa = search.find_elements_by_xpath("//input[@class='lui-search__input ng-pristine ng-valid ng-empty ng-valid-maxlength ng-touched']")[2]
    #caixa.clear()
    caixa.send_keys(str(i))
    time.sleep(3)
    search.find_elements_by_xpath("//div[@class='qv-object-content-container']")[0].find_elements_by_xpath("//ul[@class='qv-listbox ng-scope']")[1].click()


# Selecionando o Estado
campo.find_element_by_xpath("//div[@class='qv-gs-scroll-btn ng-scope']").click()
time.sleep(10)
estados = campo.find_elements_by_xpath("//div[@class='qv-gs-listbox ng-scope']")[24].find_element_by_xpath("//div[@class='qv-object-content ng-isolate-scope']").find_element_by_xpath("//ul[@class='qv-listbox ng-scope']").find_elements_by_xpath("//li[@class='ng-scope serverOptional']")

# Selecionando o Ceará
ceara=campo.find_elements_by_xpath("//div[@class='qv-gs-listbox ng-scope']")[21].find_element_by_xpath("//div[@class='qv-object-content ng-isolate-scope']").find_element_by_xpath("//ul[@class='qv-listbox ng-scope']").find_elements_by_xpath("//li[@class='ng-scope serverOptional']")[7].click()
