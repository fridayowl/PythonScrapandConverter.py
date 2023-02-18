
from bs4 import BeautifulSoup
from googletrans import Translator
import os
from bs4 import Comment
import json

with open("classcentral_links.txt") as f:
    lines = f.readlines()

data = [line.strip().replace("https://www.classcentral.com/report/", "") for line in lines]

for item in data:
    folder_path = item
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Check if the file is an HTML file
        if file_name.endswith(".html") or file_name.endswith(".htm"):
            html_file_name=file_name
            html_file_path = file_path
            print(html_file_path)
            # Read the contents of the HTML file
            with open(html_file_path, 'r', encoding="utf8") as html_file:
                html_contents = html_file.read()

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(html_contents, 'html.parser')

            # Translate all the text elements to Hindi
            translator = Translator()
            for elem in soup.find_all(string=True):
                if elem.parent.name not in ['script', 'style','html','!DOCTYPE','[document]','meta'] and  not  isinstance(elem, (Comment)) :
                    with open('data.json', 'r') as f:
                        data = json.load(f)
                        if elem.strip() in data :
                            elem.replace_with(data[elem.strip()])
                            #print("text already found")
                        else:
                            translated_text = translator.translate(elem.strip(), dest='hi').text
                            elem.replace_with(translated_text)
                            data[elem.strip()] = str(translated_text)
                            print("added new text")
                            with open('data.json', 'w') as f:
                                json.dump(data, f)
            # Save the translated HTML to a new file
            with open(html_file_path, 'w', encoding='utf-8') as translated_file:
                translated_file.write(str(soup))
            print('Translation complete. Hindi HTML file saved!')


