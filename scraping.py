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
time.sleep(20)
filtro = drive.find_element_by_xpath("//div[@class = 'Menu_App']") 
linha = filtro.find_element_by_xpath("//div[@id = 'CurrentSelections01']").find_element_by_xpath("//div[@class= 'buttons-end borderbox border-left']").find_elements_by_xpath("//div[@class='qv-subtoolbar-button toggle-button borderbox']")[1].click()
campo = drive.find_element_by_xpath("//div[@class = 'qv-global-selections ng-scope ng-isolate-scope']").find_element_by_xpath("//section[@class='qv-gs-section']").find_element_by_xpath("//div[@class='qv-gs-scroll-container ng-isolate-scope']")#.find_elements_by_xpath("//div[@class='qv-gs-listbox ng-scope']")

# Selecionando o Ano 
time.sleep(10)
campo.find_element_by_xpath("//div[@class='qv-gs-listbox ng-scope']")[1]

# Selecionando o Estado
campo.find_element_by_xpath("//div[@class='qv-gs-scroll-btn ng-scope']").click()
time.sleep(10)
estados = campo.find_elements_by_xpath("//div[@class='qv-gs-listbox ng-scope']")[24].find_element_by_xpath("//div[@class='qv-object-content ng-isolate-scope']").find_element_by_xpath("//ul[@class='qv-listbox ng-scope']").find_elements_by_xpath("//li[@class='ng-scope serverOptional']")

# Selecionando o Ceará
ceara=campo.find_elements_by_xpath("//div[@class='qv-gs-listbox ng-scope']")[21].find_element_by_xpath("//div[@class='qv-object-content ng-isolate-scope']").find_element_by_xpath("//ul[@class='qv-listbox ng-scope']").find_elements_by_xpath("//li[@class='ng-scope serverOptional']")[7].click()
