from bs4 import BeautifulSoup
# 從檔案
with open("file.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# 找到所有的 'b' 標籤
div_tags = soup.find_all('div')
print(div_tags)
# 找到第一個 'p' 標籤
h1_tag = soup.find('h1')
print(h1_tag)