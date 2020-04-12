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
    plt.xlabel("Days Since 100th Confirmed Case")
    plt.ylabel(ylabel)
    plt.legend()