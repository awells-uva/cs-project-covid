def subset_country(dataframe, country):

    outframe = dataframe[dataframe['Country/Region'] == country]
    return outframe

def get_cases_confirmed_as_lists(dataframe):
    dataframe = dataframe.groupby(['Country/Region']).sum().reset_index()
    local_dates = []
    cases_per_day = []
    new_cases_per_day = []
    local_dates = dataframe.columns[4:]
    cases_per_day = dataframe.values[0][4:]
    new_cases_per_day = [cases_per_day[i] - cases_per_day[i-1] for i in range(1,len(cases_per_day))]
    new_cases_per_day.insert(0,cases_per_day[0]) #Add how many it was on day 1
    
    return local_dates, cases_per_day, new_cases_per_day