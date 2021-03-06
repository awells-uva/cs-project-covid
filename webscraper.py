## Awells Apr 24 2020
from bs4 import BeautifulSoup
import requests
import os

def listFD(url, ext=''):
    page = requests.get(url).text
    print("Fetching Data From: {}".format(url))
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

def webscrape(datapath,url,ext, verbose=False):
    """
    Inputs
        datapath: location on disk to store downloaded data
        url: url to github page
        ext: file extension of files on github to download
        
    Summary
        Fetches datafiles from github
    
    Returns
        None
    """
    for filename in listFD(url, ext):
        if filename.endswith(".csv"):

            csvfile = filename.split("/")[-1]
            rawurl = url.replace("https://github.com/CSSEGISandData/COVID-19/tree", "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/")
            if verbose:
                print("Downloading: {}".format(csvfile))
            if not os.path.isdir(datapath):
                os.makedirs(datapath)
            ### This produces a ResourceWarning: unclosed file <_io.BufferedWriter Warning. should be corrected but it's just a warning
            response = requests.get(rawurl+'/'+csvfile)
            open(datapath + "/" + csvfile, 'wb').write(response.content)
            
    print("Data is Stored in: {}".format(datapath + "/"))

def webscrape_population_2020():
    """
    Inputs
        None
        
    Summary
        Webscrapes a table of 2020 Country level population Data
        
    Returns
        pandas dataframe
    """
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
        # Remove commas from numerical columns
        entry = row[1:]
        entry[1] = entry[1].replace(',', '')
        entry[3] = entry[3].replace(',', '')
        entry[4] = entry[4].replace(',', '')
        entry[5] = entry[5].replace(',', '')
        entry[6] = entry[6].replace(',', '')

        frame.append(entry)

    # Update frame to match country names
    df = pandas.DataFrame(frame, columns = headers)
    df.country[df.country == 'United States']  = 'US'
    df.country[df.country == 'Taiwan']  = 'Taiwan*'
    df.country[df.country == 'South Korea']  = 'Korea, South'
    df.country[df.country == "Côte d'Ivoire"]  = "Cote d'Ivoire"
    df.country[df.country == "Czech Republic (Czechia)"]  = "Czechia"
    df.country[df.country == 'St. Vincent & Grenadines']  = 'Saint Vincent and the Grenadines'
    df.country[df.country == 'Saint Kitts & Nevis']  = 'Saint Kitts and Nevis'
    df.country[df.country == 'Sao Tome & Principe']  = 'Sao Tome and Principe'
    
    # Return Pandas dataframe
    return df 
