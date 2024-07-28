from webdriver_manager.chrome import ChromeDriverManager # Instalar automáticamente chromedriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def chrome_config():
    # Configura las opciones del navegador
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-runing-insecure-content") # Desactiva el aviso de contenido no seguro
    options.add_argument("--no-default-browser-check") # Evita el aviso de que chrome no es el navegador por defecto
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server") # Usaremos conexiones directas
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--headless")  # Opcional: Ejecutar en modo headless (sin abrir la ventana de chrome)
    options.add_argument("--no-sandbox") # El modo sandbox en Google Chrome es una característica de seguridad que aísla el navegador y sus procesos para proteger el sistema operativo y otras aplicaciones de posibles amenazas. En otras palabras, actúa como una capa adicional de seguridad que restringe el acceso del navegador a los recursos del sistema y a otros procesos.
    options.add_argument("--disable-dev-shm-usage") # Desactiva el uso de dev/shm
    # Parámetros a omitir en el inicio de chrome:
    exp_opt = ['enable-automation', 'ignore-certificate-errors', 'enable-logging']
    options.add_experimental_option("excludeSwitches", exp_opt)
    # Parámetros que definen preferencias en chromedriver
    prefs ={
        'profile.default_content_setting_values.notifications' : 2, # notificaciones: 0=preguntar | 1=permitir | 2=no permitir
        'intl.accept.languages' : ['es-ES', 'es'], # Definir el idioma del navegador
        'credentials_enable_service' : False # Omitir el aviso de guardar las contraseñas cuando nos logeamos
    }
    options.add_experimental_option("prefs", prefs)

    # Configurar el servicio de ChromeDriver
    # service = Service('C:/Users/hecho/OneDrive/Escritorio/Teoria_python/web_scraping/chromedriver.exe')  # Verifica esta ruta

    service = Service(ChromeDriverManager().install())  # Esta función descarga la versión adecuada del chromedriver para tu versión de Google Chrome y devuelve la ruta al archivo chromedriver.exe.
    driver = webdriver.Chrome(service=service, options=options)

    return driver