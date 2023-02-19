# Python Tool Scrape and Convert Website Content language to Hindi

Steps involved in ##Development .

- Download entire website and then copy to local dir
- Scrap the website read the text and convert to Hindi
- ✨Upload the website to any live server ✨


## Step 1. Downloading all the website files

Tool Used   [  wget](https://www.javatpoint.com/linux-wget#:~:text=Command%20wget%20stands%20for%20web,while%20wget%20finish%20its%20work.)  

Install the dependencies and devDependencies and start the server.

```sh
wget --user-agent="Mozilla"  https://www.classcentral.com
```
** Reason for not using HTTrack {My internet connection is not stable so HTTrck will crash most of the time }  **

## Step 2. Converting Text to Hindi

Algorithm ---
- Identify the index.html file 
-  create a list of all the links(path) that involved in the index.html 
-  Travel through all the path and open each html file one by one 
-  Scrape using Beautifull soup read the tags that has text only 
-  use google translator library and then convert the text and update the file
-  create a json dictonary that store the translated text so next time if the same text apprears there is no need to translate it .
- save the file after convertion.

## Step 3. Uploading File to live a server 

- change all the url that contains "https://www.classcentral.com/" to  your domain name 
- deploy all the files to firebase database 

-Issues:
    Unable to download the Navigation Js script from the host becuase of that navigation bar javascript not working . Tried to inject it seperately but failed .apart from that all the JS script are indeed in place .
    The Image files are not compressed and source code is not optimized because of that the convertion takes too much time and image loading time is to high . 
-- future improvment 
-will focus on reducing the convertion time .









