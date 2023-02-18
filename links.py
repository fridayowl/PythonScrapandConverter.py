from bs4 import BeautifulSoup
import requests

# Load the HTML file
with open("index.html",'r',encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# Find all links in the HTML file
links = soup.find_all("a")

# Create a list of links that contain "https://www.classcentral.com"
classcentral_links = [link.get("href") for link in links if link.get("href") and "https://www.classcentral.com" in link.get("href")]

# Write the links to a text file
with open("classcentral_links.txt", "w") as f:
    f.write("\n".join(classcentral_links))
