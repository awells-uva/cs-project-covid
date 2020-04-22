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

def webscrape_population_2020():
    from bs4 import BeautifulSoup
    import requests
    import pandas
    url = "https://www.worldometers.info/world-population/population-by-country/"
    print("Fetching Data From: {}".format(url))
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    headers = ["country", "population", "yearlyChange","netChange","density(P/Km2)","landArea(km2)", "migrants", "fertRate","medAge", "urbanPop","worldShare"]
    table = soup.find('table')
    table_rows = table.find_all('tr')
    frame = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if len(row) == 0:
            continue
        ## Clean Data
        entry = row[1:]
        entry[1] = entry[1].replace(',', '')
        entry[3] = entry[3].replace(',', '')
        entry[4] = entry[4].replace(',', '')
        entry[5] = entry[5].replace(',', '')
        entry[6] = entry[6].replace(',', '')

        frame.append(entry)

    df = pandas.DataFrame(frame, columns = headers) 
    return df 
