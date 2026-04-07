from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

#Abre o navegador automaticamente
driver = webdriver.Chrome()

# Link da pesquisa de lotes em Eusébio
url = "https://www.zapimoveis.com.br/aluguel/imoveis/ce+fortaleza/?onde=%2CCear%C3%A1%2CFortaleza%2C%2C%2C%2C%2Ccity%2CBR%3ECeara%3ENULL%3EFortaleza%2C-3.73272%2C-38.527013%2C"
driver.get(url)

# Espera a página carregar
time.sleep(5)

# Coleta os dados dos imóveis
imoveis = []

# Encontrar os elementos de cada propriedade
cards = cards = driver.find_elements(By.CSS_SELECTOR, '[data-cy="rp-property-cd"]')

#Função para pegar o texto de um elemento ou retornar "Não informado" caso o elemento não exista
def pegar_texto(card, seletor, primeira_linha=False):
    try:
        texto = card.find_element(By.CSS_SELECTOR, f'[data-cy="{seletor}"]').text
        if primeira_linha:
            return texto.split('\n')[0]
        return texto.split('\n')[-1]
    except:
        return "Não informado"
    
#Coletar as informações de cada imóvel
for card in cards:
    imoveis.append({
    'preco':     pegar_texto(card, 'rp-cardProperty-price-txt', primeira_linha=True),
    'bairro':    pegar_texto(card, 'rp-cardProperty-location-txt'),
    'area':      pegar_texto(card, 'rp-cardProperty-propertyArea-txt'),
    'quartos':   pegar_texto(card, 'rp-cardProperty-bedroomQuantity-txt'),
    'banheiros': pegar_texto(card, 'rp-cardProperty-bathroomQuantity-txt'),
    'vagas':     pegar_texto(card, 'rp-cardProperty-parkingSpacesQuantity-txt'),
})
#Salva os dados em um arquivo CSV
tabela = pd.DataFrame(imoveis)
tabela.to_csv('imoveis.csv', index=False, encoding='utf-8-sig')
print(f"Dados salvos! Total de imóveis: {len(tabela)}")

#Fecha o navegador  
driver.quit()
