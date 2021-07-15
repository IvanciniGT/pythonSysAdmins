import yaml
# Fabrik, Selenium, Pandas, Numpy, YAML

with open ("ejemplo.yaml","r") as fichero_yaml:
    contenido_del_fichero=yaml.load(fichero_yaml, Loader=yaml.FullLoader)
    print(contenido_del_fichero)
    
    for elemento in contenido_del_fichero:
        print("- " + str(elemento))
        
