import requests
from requests.exceptions import HTTPError

#Status code 
response = requests.get('https://api.github.com') 
print(response.status_code)
if response.status_code == 200:
    print('nice')
elif response.status_code == 404:
    print('no encontrado')

#Errors
for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_error:
        print(f'Ocurrio un error de HTTP :( {http_error}')
    except Exception as error:
        print(f'Ocurrio un error desconocido :O {error}')