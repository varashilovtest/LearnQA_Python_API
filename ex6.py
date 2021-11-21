import requests

responce = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
first_responce = responce.history[0]
second_responce = responce
number_of_redirects = len(responce.history)

print(number_of_redirects)
print(second_responce.url)
