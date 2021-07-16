from selenium import webdriver
import re

driver=webdriver.Remote(
        command_executor="http://localhost:4444",
        desired_capabilities={
                "browserName": "firefox",
                "browserVersion": "90.0",
                "platformName": "Linux",
                "se:vncEnabled": True        
        }
    )

driver.implictly_wait(5)            # Timeout de cada operacion

driver.get("http://itnow.es/")

# Buscar un elemento dentro de la web.....                      Y hacemos algo en el
driver.find_element_by_xpath("//input[@id='txtBuscar']")                            .send_keys("servicios")
driver.find_element_by_xpath("//input[@id='ctl00_BuscadorMenu1_bt_search']")        .click()
#try:
#    driver.find_element_by_xpath("//h2[contains(text(),'Error')]") 
#except: # Se produce si el elemento no existe
texto_del_h2=driver.find_element_by_xpath("//h2[contains(@class,'ms-search-header')]") .text

if re.match(".*error",texto_del_h2.lower()):
    print("La busqueda de la web no esta funcionando")
else:
    print("la busqueda de la web si que funciona")

print(driver.title)
driver.quit()
