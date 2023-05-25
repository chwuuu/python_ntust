from bs4 import BeautifulSoup

# 從字符串
soup = BeautifulSoup("""<!DOCTYPE html>
                            <html>
                            <head>
                                <title>Example HTML with Link</title>
                            </head>
                            <body>
                                <h1>Welcome to My Webpage</h1>
                                <p>Click the link below to visit my favorite website:</p>
                                <a href="https://example.com">Visit Example Website</a>
                            </body>
                            </html>""", "html.parser")

a_tag = soup.a
print(a_tag)

# 獲取 a 標籤的 href 屬性值
href = a_tag.get('href')
print(href)
# 獲取 a 標籤的內容
text = a_tag.string
print(text)