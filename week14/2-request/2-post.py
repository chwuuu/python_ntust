import requests

# 設定 POST 請求的資料
payload = {'username': 'example', 'password': 'secret1'}

# 發送 POST 請求
response = requests.post('http://127.0.0.1:5000/login', data=payload)

# 印出回應的狀態碼
print(response.status_code)

# 印出回應內容
print(response.text)
