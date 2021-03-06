# cs-project-covid

CS5010 Final Project: Data Exploration of the COVID-19 Pandemic

Project Group 1 (Spring 2020 Cohort): Akeem Wells (ajw3rg), Sam Tyree (jst6jz), Michael Davies (mld92)

April 28, 2020

Abstract:

This project aims to describe the variations in COVID-19 related transmission rates by comparing data and metrics from different countries. We analyzed time-based virus trends through visualizations of rates of transmission by country. We normalized by population and population density, as well as days since 100th case. Rate of death and rate of recovery were examined but we chose to focus for this project on transmission rates. We also “predict” future trends for the United States and China using a time series modeling tool. Importantly, we developed webscraping methods so users view near-real-time updates on countries of interest, and we developed custom functions to clean and plot the data. This is a topic that is rich for data exploration, and our custom functions will be helpful for future data scientists both in terms of accessing near real-time data and cleaning/visualizing the trends.

Our results are not optimistic, predicting continued growth in transmission rates. The data so far reflects the most affected countries are somewhat “developed-countries.” This may reflect a greater degree of international travel in and out of developed countries, or lack of reporting from under-developed countries, or some combination of both. Population density matters, but it is unclear how critical this is. More analysis must be done before we can make definitive conclusions. For instance, we did not have access to (possibly) important variables such as policy differences, levels of urbanization, weather/climate, levels of travel, or population age base. Including variables such as these would likely improve the analysis.

Introduction:

After first emerging in Wuhan, China in December, 2019, the novel coronavirus spread rapidly and took just a few months to become a global pandemic. By April 26, 2020, confirmed cases worldwide have reached 2.9 million and the number of deaths has exceeded 200,000 - a death rate of 7%. Rates of infection and death vary from country to country, sometimes significantly so. Europe has been hard hit, with several countries having far higher rates of death than other parts of the world. The United States has the highest overall number of confirmed cases.

This project aims to describe the variations in infection rates by comparing data and metrics from different countries. When we began, COVID-19 was still emerging and was largely considered a problem for China, though it was starting to spread to other countries. We were curious to know more about the disease and wanted to answer questions like these: How quickly do new cases appear? Does geography contribute to disease spread? Why do some countries have higher rates of death from the disease than others? How long would it take to see the number of new cases stop growing?

The Data:

Data for the 2019 Novel Coronavirus COVID-19 (2019-nCoV) is obtained and regularly updated from the Data Repository by Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE). The JHU CSSE collects real-time publicly available data from multiple sources from across the globe. Although these sources do not always agree, the data is robust. JHU CSSE maintains and updates a GitHub repo and its contents for educational and academic research purposes. Not surprisingly, since we first began this project in late February, data on 2019-nCoV has expanded considerably and there are now many more data sources available. Even so, the JHU CSSE data set remains a go-to source for 2019-nCoV data.

For this project, each time the code is run, it scrapes the most current data available on the number of confirmed cases of infection, deaths, and recoveries from the JHU CSSE GitHub repo. We knew that COVID-19 is highly contagious and therefore the data on new cases would be constantly changing. By using web scraping techniques rather than manually loading updated .csv files every day, we created a more useful and lightweight tool. It also ensures that we are always using the latest data that is available.

CONCLUSIONS:

COVID-19 is a disease that has no regard for geography, and spreadly globally so fast that creating case-number thresholds for cross-country comparison became unnecessary. Many countries that are typically considered "developed" have the highest rates of infection in the world--possibly due to large rates of international travellers. It was somewhat surprising to see China's infection rate so low, though there is speculation that intentionally reporting may be at play there.

When we consider the physical geography of Europe, with many countries sharing borders, it may not be too surprising that infection rates are high. However, varying government responses around the world have clearly had an impact. In countries that responded early and aggressively to the pandemic, the rates of growth were shorter and the number of infections lower (South Korea for example). Countries that waited longer to close businesses and encourage social distancing, like Britain and the U.S., show a faster rate of growth and higher total infections.

This program is fairly simple compared to others that have been developed since the COVID-19 crisis began. However, it is a useful tool that provides insight into infection rates for all countries, with a focus on those that have the largest number of infections. The data visualizations are easy to read and understand, and they provide the user with both raw and normalized figures in context of population. The program updates with the latest data automatically each time the code is run, so requires no additional user input. Our program is written to automatically display plots only for countries with more than 100,000 infections.

With additional time to work on this project, we would focus on a few things. First would be to bring in other types of data to be able to look at things like infection and death rates relative to GDP, median age, median income, and forms of government. We would be interested to see if there is any relationship between these variables and COVID-19 spread and lethality. Second, we would add more interactivity to give users the ability to retrieve data and create visualizations based on their inputs. Third, we would add more visualizations of the data, such as a map-based view of infection and death rates. Last, further research could introduce predictive modeling to explore which country characteristics explain the variation in infection rates.
