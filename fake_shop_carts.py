import requests
import pprint
url = 'https://fakestoreapi.com/carts'
         
response = requests.get(url).json()
pprint.pprint(response)

id_users = input('ввидите ID:')
url_1 = f'https://fakestoreapi.com/carts/user/{id_users}'
response_1 = requests.get(url_1).json()
pprint.pprint(response_1)

