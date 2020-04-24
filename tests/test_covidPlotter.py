import unittest
import os
import sys
import pandas
path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path.split("tests")[0])

import covidPlotter
import webscraper

class covidPlotterTest(unittest.TestCase):
    def setUp(self):
        self.testFrame = pandas.read_csv('datatest.csv')
        self.testPopFrame = webscraper.webscrape_population_2020()
    
    def test_plot_multi_countries_fake_countries(self):
        '''Test Plotting will return false if no avaliable countries'''
        unique_countries = ["Some","Fake","Country"]
        val = covidPlotter.plot_multi_countries(unique_countries, self.testPopFrame, self.testFrame, yaxis = 'FAKE')
        self.assertFalse(val)

    def test_plot_multi_countries(self):
        '''Test Plotting will return error if incorrect option of yaxis is given'''

        unique_countries = ["US","China","Spain"]

        try:
            covidPlotter.plot_multi_countries(unique_countries, self.testPopFrame, self.testFrame, yaxis = 'FAKE')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        
if __name__ == '__main__':
    unittest.main()
