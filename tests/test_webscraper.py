import unittest
import os
import sys
import pandas
import shutil
path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path.split("tests")[0])

import webscraper

class webscraperTest(unittest.TestCase):
    def setUp(self):
        self.datapath = os.getcwd()+"/test_webscrape"
    
    def tearDown(self):
        try:
            shutil.rmtree(self.datapath)
        except:
            pass
        
    def test_webscrape(self):
        '''Test Webscrape pulls correct Files'''
        url = "https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series"
        ext = 'csv'

        webscraper.webscrape(self.datapath,url,ext)
        
        for filename in ['time_series_covid19_confirmed_global.csv',
                         'time_series_covid19_recovered_global.csv',
                         'time_series_covid19_deaths_global.csv']:
            if not os.path.isfile(self.datapath+"/" + filename):
                self.assertTrue(os.path.isfile(self.datapath+"/" + filename),'File: {} does not exist'.format(filename))
                
    def test_webscrape_population_2020(self):
        '''Test Population Frame has needed Columns'''
        df = webscraper.webscrape_population_2020()
        
        for colname in ["population","density(P/Km2)"]:
            if colname not in df.columns:
                self.assertTrue(False,"Missing Column: {}".format(colname))

            
if __name__ == '__main__':
    unittest.main()
