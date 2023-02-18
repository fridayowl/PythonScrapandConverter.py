from bs4 import BeautifulSoup

# Read the HTML file and create BeautifulSoup object
with open('index.html', 'r',encoding="utf8") as file:
    html = file.read()
    soup = BeautifulSoup(html, 'html.parser')

# Find all href tags in the HTML
href_tags = soup.find_all('a')
print(href_tags)
# Loop through all href tags and modify the URLs
for tag in href_tags:
    if tag.get('href') and 'https://www.classcentral.com' in tag['href']:
        url = tag['href']
        if url.endswith('/'):
            url += 'index.html'
            print(url)
        else:
            url += '.html'
        tag['href'] = url.replace('https://www.classcentral.com', 'https://test-d401e.web.app')

# Save the modified HTML as new.html
with open('index.html', 'w',encoding='utf-8') as file:
    file.write(str(soup))
