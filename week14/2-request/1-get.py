import requests

response = requests.get('https://chwuuu.github.io/demopage/')
print(response.status_code)  # 印出回應狀態碼
print(response.text)  # 印出回應內容
