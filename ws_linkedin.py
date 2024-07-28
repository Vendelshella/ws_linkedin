# Librerías
from chrome_config import chrome_config
from linkedin_conection import linkedin_conection
from wait_random import wait_random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import csv
import time


if __name__ == "__main__":

    # Configura las opciones del navegador y el servicio de Chromedriver
    driver = chrome_config()

    # Acceso a linkedin
    linkedin_conection(driver)

    # Guardar la información obtenida
    companies_dict = {}

    # Recorrer los resultados filtrados mediante url
    for pagina in range(1, 67):  # Páginas de 1 a 66
        # Página filtrada en linkedin por empresas y por ubicación:
        driver.get(f'https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B"101598293"%5D&keywords=Toledo&origin=FACETED_SEARCH&page={pagina}')
        
        # Esperar hasta que el elemento a scrapear sea visible:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.entity-result__title-text')))
        # Esperamos que se cargue la etiqueta body para hacer scrolldown:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        
        # Ejecuta el scroll down
        for _ in range(3):  # Hacer scroll 3 veces
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)  # Esperar un poco para que el contenido se cargue

        # Extraer el contenido del enlace y el enlace de las empresas <a>:
        a_elements = driver.find_elements(By.CSS_SELECTOR, 'span.entity-result__title-text.t-16 > a') # devuelve una lista de objetos (los enlaces encontrados)

        # Iterar sobre la lista de enlaces obtenidos
        for element in a_elements:
            name_company = element.text
            link_company = element.get_attribute('href')

            # Recopilar la data en el diccionario
            companies_dict[name_company] = link_company

        wait_random() # Esperar unos segundos aleatorios entre peticiones


    # Escribir datos del diccionario en un archivo CSV
    with open('companies.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Company Name', 'Link'])  # Encabezado
        for name, link in companies_dict.items():
            writer.writerow([name, link])


    # Cerrar el navegador
    driver.quit()

# Toledo (651 resultados):
# https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B"101598293"%5D&keywords=Toledo&origin=FACETED_SEARCH&page={pagina}
# Toledo y alrededores (6700 resultados):
# https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22101598293%22%5D&origin=FACETED_SEARCH&page={pagina}
