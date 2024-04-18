from selenium import webdriver
import time
import helium as he
import json

# Inicializar el navegador
driver = webdriver.Chrome()

# Navegar a la página de ZonaProp en Rosario
he.start_chrome("https://www.zonaprop.com.ar/inmuebles-venta-rosario.html")

# Esperar un tiempo fijo (por ejemplo, 5 segundos) para que la página cargue
time.sleep(5)

# Encontrar todas las tarjetas de propiedades en la página
properties_price = he.find_all(he.S(".sc-12dh9kl-3"))
properties_price_text = [element.web_element.text.strip() for element in properties_price]
location = he.find_all(he.S(".sc-ge2uzh-0"))
location_text = [element.web_element.text.strip() for element in location]
details = he.find_all(he.S(".sc-1uhtbxc-0"))
details_text = [element.web_element.text.strip() for element in details]

# Reformatear los detalles
formatted_details = []
for detail in details_text:
    formatted_detail = detail.replace("m²", "m2").replace("\n", " ")
    formatted_details.append(formatted_detail)

properties = []

for price, location, details in zip(properties_price_text, location_text, formatted_details):
    property_details = [detail.strip() for detail in details.split(",")]
    property_info = {
        "price": price,
        "location": location,
        "details": property_details
    }
    properties.append(property_info)

# Guardar las propiedades en un archivo JSON
with open("properties.json", "w", encoding="utf-8") as json_file:
    json.dump(properties, json_file, indent=4, ensure_ascii=False)

print("Propiedades guardadas en properties.json")

# Cargar las propiedades desde el archivo JSON con codificación UTF-8
with open("properties.json", "r", encoding="utf-8") as json_file:
    loaded_properties = json.load(json_file)

print(loaded_properties)
