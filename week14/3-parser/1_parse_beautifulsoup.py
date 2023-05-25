from bs4 import BeautifulSoup

# 從字符串
soup = BeautifulSoup("<html>資料</html>", "html.parser")

# 從檔案
with open("file.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# 獲取標題標籤
title_tag = soup.title
print(title_tag)
# 獲取標題標籤的父標籤（head 標籤）
head_tag = title_tag.parent
print(head_tag)
# 獲取第一個 div 標籤
a_tag = soup.div
print(a_tag)
# 獲取所有的 div 標籤
all_a_tags = soup.find_all('div')
print(all_a_tags)