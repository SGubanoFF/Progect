import requests
import pprint
id_user = input('id user:')
url = f'https://api.vk.com/method/friends.get?user_id={id_user}&order=name&access_token=vk1.a.JWKNdqZcu7PpvZgohDQyGj0RJEbsMTxMJoZF0sjUE5zCSQ__7mrvFju4wxLfQmrgz7b81qdIX1RUEfpDt4V4Q5h6pbVnYOTrmdBbFcPgLBWAGJfv-9Geg3JwC9Xp5NhXwwubtZJG-rmyHAi0mKmxJtOD_9ILsXpu2kkNTeBkz8s0zdoutDLF0K8d-ZqDreOD&v=5.199 HTTP/1.1'
response = requests.get(url).json()
friends = response['response']['items']
print(f'у этого пользователя {len(friends)} друг')
