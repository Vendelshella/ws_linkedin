from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def linkedin_conection (driver):
    try:
        # Navega a la página de inicio de sesión de LinkedIn 
        driver.get('https://www.linkedin.com/login')

        # Espera a que la página cargue completamente
        time.sleep(10)

        # Otra forma de esperar a que la página cargue completamente
        # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'username')))


        # Encuentra los campos de entrada de usuario y contraseña
        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')

        # Introduce tus credenciales
        # Deberían de estar en otro archivo
        username.send_keys('your_username')
        password.send_keys('your_password')
        password.send_keys(Keys.RETURN)  # Envía el formulario

        # Espera a que la página se cargue después del inicio de sesión
        time.sleep(10)

    except NoSuchElementException as e:
        print("Error: No se encontró uno de los elementos en la página.")
        print(f"Detalles del error: {e}")
    except TimeoutException as e:
        print("Error: Se superó el tiempo de espera para cargar la página o encontrar un elemento.")
        print(f"Detalles del error: {e}")
    except WebDriverException as e:
        print("Error relacionado con el WebDriver.")
        print(f"Detalles del error: {e}")
    except Exception as e:
        print("Se produjo un error inesperado.")
        print(f"Detalles del error: {e}")