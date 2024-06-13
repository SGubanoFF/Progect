import requests
import pprint
url = f'https://fakestoreapi.com/products/categories'
         
response = requests.get(url).json()
print(response)
category = input('ввидите интересующую вас категорию товара:')
url_1 = f'https://fakestoreapi.com/products/category/{category}'
response_1 = requests.get(url_1).json()
pprint.pprint(response_1)
