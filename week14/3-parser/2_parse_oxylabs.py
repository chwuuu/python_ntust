import requests
from bs4 import BeautifulSoup

# 發送 GET 請求
url = 'https://www.ptt.cc/bbs/Tech_Job/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
}

response = requests.get(url, headers=headers)

# 檢查是否成功取得回應
if response.status_code == 200:
    # 取得回應內容
    content = response.text
    
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(content, 'html.parser')
    print(content)
    # 在這裡可以使用適當的 CSS 選擇器來獲取你所需的資訊
    # 以下僅是一個示例

    """title_elements = soup.find_all('div', class_='title')
    titles = [title.a.text for title in title_elements]"""
    names = soup.select('div.component-inner-container span.name')

    for name in names:
        print(name.get_text())
else:
    print('請求失敗')