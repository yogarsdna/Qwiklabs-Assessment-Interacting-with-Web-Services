import os
import requests

#List all .txt files under /data/feedback directory
dir = "/data/feedback/"

for file in os.listdir("/data/feedback/"):
    #Make a format that keep the title, name, date, and feedback as keys for the content value, respectively
    format = ["title", "name", "date", "feedback"]

    #Make a dictionary with keys and their respective values (content from feedback files)
    content = {}
    
    with open('{}/{}'.format(dir ,file), 'r') as txtfile:
        counter = 0
        for line in txtfile:
            line = line.replace("\n", "")
            content[format[counter]] = line.strip('\n')
            counter += 1

    #Use the Python requests module to post the dictionary to the company's website
    response = requests.post("http://34.136.244.146/feedback/",json = content)

    #Print the status_code and text of the response objects to check out what's going on
    if not response.ok:
        raise Exception("POST failed! | Status code: {} | File: {}".format(response.status_code, file))
    print("Feedback successfully added!")