import requests

# Объявляем все используемые переменные
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

correct_requests = ["GET", "POST", "PUT", "DELETE"]

payload = {"method":"HEAD"}


# Пункт 1. Делаем запрос без указания параметра
empty_request = requests.get(url)
print(empty_request.text)

# Пункт 2. Делаем запрос с неверным параметром
uncorrect_request = requests.head(url, data=payload)
print(uncorrect_request)

# Пункт 3. Делаем запрос с верным параметром
payload = {"method":"GET"}
correct_request = requests.get(url, params=payload)
print(correct_request)

# Пункт 4
for i in range(len(correct_requests)):
    methods_requests = correct_requests[i]
    print(methods_requests)
    if correct_requests[i] == "GET":
        for j in range(len(correct_requests)):
            payload = {"method": correct_requests[j]}
            response=requests.get(url, params=payload)
            print(response.text)
    else:
        for j in range(len(correct_requests)):
            payload = {"method": correct_requests[j]}
            response = requests.request(methods_requests, url, data=payload)
            print(response.text)