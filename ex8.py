import requests
import json
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response_1 = requests.get(url)
json_text = response_1.text
obj_1 = json.loads(json_text)
token = obj_1["token"]
time_S = obj_1["seconds"]

payload = {"token": f"{token}"}
response_2 = requests.get(url, params=payload)
obj_2 = json.loads(response_2.text)
status = obj_2["status"]

if status == "Job is NOT ready":
    print("Статус корректный:", status)

time.sleep(int(time_S))

response_3 = requests.get(url, params=payload)

obj_3 = json.loads(response_3.text)
status_ready = obj_3["status"]
result = obj_3["result"]

if status_ready == "Job is ready":
    print("Статус корректный:", status_ready)
if result is not None:
    print("Result присутствует и равен: ", result)
