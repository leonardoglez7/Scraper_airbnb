from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def paginas(driver, ids):
    lista = ["2", "3", "4", "5", "6", "7","8", "9", "10"]
    if buscar_id(driver, ids):
            return "1" 
    try:
        for pagina in lista:
            time.sleep(10)
            enlace = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, pagina)))
            enlace.click()

            if buscar_id(driver, ids):
                return pagina
    except:
        print(f"Casa no encontrada en la pagina {pagina}")
            
def cerrar_ventana(driver):
    try:           
        cerrar_boton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Cerrar']")))
        cerrar_boton.click()
    except:
        print("Boton no encontrado")

def buscar_id(driver, ids):
    propiedad_id = None
    lista_ids = []
    time.sleep(3)
    enlaces = driver.find_elements(By.TAG_NAME, "a")
    for enlace in enlaces:
        href = enlace.get_attribute("href")
        if href:
            match = re.search(r"/rooms/(\d+)", href)
            if match:
                propiedad_id = match.group(1)
        
                if propiedad_id == ids:
                    screenshot(ids, driver)
                    return True
                elif propiedad_id not in lista_ids:
                    lista_ids.append(propiedad_id)
                    print(propiedad_id)
    return False

def screenshot(ids, driver):
    name_screenshot = f"casa_{ids}"
    driver.get_screenshot_as_file(f"{name_screenshot}.png")
    
def obtener_info(ids):
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.get(f"https://es.airbnb.com/s/Orlando--Florida/homes?&checkin={fecha_llegada}&checkout={fecha_partida}&adults={huespedesa}")
        driver.maximize_window()
        
        cerrar_ventana(driver)
        
        time.sleep(5)
        
        resultado = paginas(driver, ids)
        
        if resultado:
            print(f"La casa de id {ids} fue encontrada en la pagina {resultado}")
        else:
            print("La casa no fue encontrada")
            
        return "Busqueda realizada correctamente"        
    except Exception as e:
        return f"Error: {e}"
    
    finally:
        if driver is not None:
            driver.quit()
        
if __name__ == "__main__":
    ids = "46299822"
    fecha_llegada = "2025-07-01"
    fecha_partida = "2025-07-05"
    huespedes = "2"
    print(obtener_info(ids))