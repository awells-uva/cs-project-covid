import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy

def plot_country_cases(dataframe,country,state=''):
    dataframe = dataframe.groupby(['Country/Region']).sum().reset_index()
    
    dates = dataframe.columns[4:]
    cases_per_day = dataframe.values[0][4:]
    
    plt.figure()
    x_values = [datetime.datetime.strptime(d,"%m/%d/%y").date() for d in dates]
    ax = plt.gca()

    formatter = mdates.DateFormatter("%Y-%m-%d")

    ax.xaxis.set_major_formatter(formatter)

    locator = mdates.DayLocator()

    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))

    plt.plot(x_values, cases_per_day)

    plt.ylabel('{} {} Cases'.format(country, state))
    plt.xlabel('Date')
    
def plot_country_confirmed_cases_index(dataframe,country, expGraph = False):
    dataframe = dataframe.groupby(['Country/Region']).sum().reset_index()
    dates = dataframe.columns[4:]
    cases_per_day = dataframe.values[0][4:]
    res = next((i for i, j in enumerate(cases_per_day) if j), None) # Finds Where the first day is non-zero
    #cases = cases_per_day[res:]
    #cases = numpy.insert(cases,0,0)
    cases = [i for i in cases_per_day[res:] if i >= 100]
    days_since_outbreak = list(range(0, len(cases)))
    plt.figure()
    plt.plot(days_since_outbreak,cases, label="{}".format(country))
    
    if expGraph:
        n = 0
        while numpy.exp(n) < cases_per_day[-1]:
            n = n + 1
        n = n - 1
        plt.plot( numpy.linspace(0,n,100),numpy.exp(numpy.linspace(0,n,100)), 'k--',label="exp(x)")
    plt.xlabel("Days Since 100th Confirmed Case")
    plt.ylabel('{} Confirmed Cases'.format(country))
    plt.legend()
    
def plot_bar(array,country,ylabel=''): 
    plt.figure()
    array = [i for i in array if i >= 100]
    plt.bar(list(range(len(array))), array,label=country)
    plt.xlabel("Days Since 100th Confirmed Case")
    plt.ylabel(ylabel)
    plt.legend()
    
def plot_bar_active(array,country,ylabel=''): 
    plt.figure()
    plt.bar(list(range(len(array))), array,label=country)
    plt.xlabel("Days")
    plt.ylabel(ylabel)
    plt.legend()

def plot_multi_countries(unique_countries, population, dataframe, yaxis = 'Confirmed', daySince = False):
    data = {}
    can_not_plot = 0
    df_subset = dataframe.groupby(['Country/Region']).sum().reset_index()
    for country in unique_countries:
        try:
            xPopulation = int(population[population['country']==country]['population'])
            xPopDen = int(population[population['country']==country]['density(P/Km2)'])

            dates = df_subset.columns[4:]
            data[country]={}
            for date in dates:
                confirmed_day = int(df_subset[df_subset["Country/Region"] ==country][date])
                confirmed_to_pop_ratio = float(confirmed_day/xPopulation)
                confirmed_to_popDen_ratio = float(confirmed_day/xPopDen)

                data[country][date] = [confirmed_day,
                                   confirmed_to_pop_ratio,
                                   confirmed_to_popDen_ratio]
                                   
        except:
            can_not_plot = can_not_plot + 1
            print("Cannot Process: {}".format(country))
    
    if can_not_plot == len(unique_countries):
        return False
        
    if yaxis.lower() == 'confirmed':
        index = 0
        yaxislabel = "Confirmed"
        
    elif yaxis.lower() == 'population':
        index = 1
        yaxislabel = "Confirmed/Population"

    elif yaxis.lower() == 'density':
        index = 2
        yaxislabel = "Confirmed/Pop. Density"
    else:
        raise ValueError('No Reference for: {}'.format(yaxis))
        
    tmp = {}
    for xCountry in list(data.keys()):
        country_dates = list(data[xCountry].keys())
        x = []
        y = []
        for country_date in country_dates:
            x_value = datetime.datetime.strptime(country_date,"%m/%d/%y").date()
            y_value = data[xCountry][country_date][index]
            x.append(x_value)
            y.append(y_value)
        x, y = (list(t) for t in zip(*sorted(zip(x, y))))
        tmp[xCountry] = [x,y]
    
    if daySince:
        plt.figure()
        if index == 0:
            for key in list(tmp.keys()):
                array = [i for i in tmp[key][1] if i >= 100]
                print(len(array))
                plt.plot(list(range(len(array))), array,label=key)
                
        if index == 1 or index == 2:
            
            for xCountry in list(data.keys()):
                counter = 0
                country_dates = list(data[xCountry].keys())
                for country_date in country_dates:
                    y_value = data[xCountry][country_date][0]
                    if y_value >= 100:
                        counter = counter + 1
                array = tmp[xCountry][1][-counter:]
                print(len(array))
                plt.plot(list(range(len(array))), array,label=xCountry)
                
        plt.xlabel('Days Since 100th Confirmed Case')
        plt.ylabel(yaxislabel)
        plt.title("Days Since 100th Confirmed Case vs {}".format(yaxislabel))
        plt.legend()
        
    if not daySince:
        plt.figure()
        ax = plt.gca()
        formatter = mdates.DateFormatter("%Y-%m-%d")
        ax.xaxis.set_major_formatter(formatter)
        locator = mdates.DayLocator()
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_locator(plt.MaxNLocator(5))
        for key in list(tmp.keys()):
            plt.plot(tmp[key][0], tmp[key][1],label=key)

        plt.xlabel('Date')
        plt.ylabel(yaxislabel)
        plt.title("Date vs {}".format(yaxislabel))
        plt.legend()
        
    plt.show()

