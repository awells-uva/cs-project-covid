from bs4 import BeautifulSoup
import requests
import os

def listFD(url, ext=''):
    page = requests.get(url).text
    print("Fetching Data From: {}".format(url))
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

def webscrape(datapath,url,ext, verbose=False):
    for filename in listFD(url, ext):
        if filename.endswith(".csv"):

            csvfile = filename.split("/")[-1]
            rawurl = url.replace("https://github.com/CSSEGISandData/COVID-19/tree", "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/")
            if verbose:
                print("Downloading: {}".format(csvfile))
            if not os.path.isdir(datapath):
                os.makedirs(datapath)
            response = requests.get(rawurl+'/'+csvfile)
            open(datapath + "/" + csvfile, 'wb').write(response.content)

    print("Data is Stored in: {}".format(datapath + "/"))

