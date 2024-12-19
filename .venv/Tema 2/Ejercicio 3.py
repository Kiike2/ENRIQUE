import requests
from bs4 import BeautifulSoup

def verificar_correo_leakcheck(email):
    api_key = 'TU_API_KEY'  # Reemplaza con tu clave de API de LeakCheck
    url = f"https://leakcheck.net/api/v1?key={api_key}&check={email}"
    response = requests.get(url)
    data = response.json()
    if data['success']:
        return data['result']
    else:
        return None

def extraer_correos_dominio(dominio):
    correos = set()
    url = f"http://{dominio}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        if 'mailto:' in a['href']:
            correos.add(a['href'].split(':')[1])
    return list(correos)

def main():
    opcion = input("Introduce '1' para correo electrónico o '2' para dominio web: ")
    if opcion == '1':
        email = input("Introduce la dirección de correo electrónico: ")
        resultado = verificar_correo_leakcheck(email)
        if resultado:
            print(f"El correo {email} aparece en {len(resultado)} filtraciones.")
            for filtracion in resultado:
                print(f"Origen: {filtracion['source']}")
        else:
            print("No se encontraron filtraciones para este correo.")
    elif opcion == '2':
        dominio = input("Introduce el dominio web: ")
        correos = extraer_correos_dominio(dominio)
        if correos:
            print(f"Correos encontrados en {dominio}: {', '.join(correos)}")
            for correo in correos:
                resultado = verificar_correo_leakcheck(correo)
                if resultado:
                    print(f"El correo {correo} aparece en {len(resultado)} filtraciones.")
                    for filtracion in resultado:
                        print(f"Origen: {filtracion['source']}")
                else:
                    print(f"No se encontraron filtraciones para el correo {correo}.")
        else:
            print("No se encontraron correos en el dominio.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
