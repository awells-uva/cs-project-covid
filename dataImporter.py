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


def get_latest_subset(dataframe, baseline):
    import datetime
    df  = dataframe.groupby(['Country/Region']).sum().reset_index()
    
    try:
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        yesterday = '{}{}'.format(yesterday.month,yesterday.strftime('/%d/%y'))
        df_subset = df[df[yesterday] > baseline ]

    except:
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=2)
        yesterday = '{}{}'.format(yesterday.month,yesterday.strftime('/%d/%y'))
        df_subset = df[df[yesterday] > baseline ]
      
    return df_subset, yesterday


def kmean_analysis(DataFrame, population, plotAllPop = True, n_clusters = 6 , removeOutliers = False, yaxis='population' ):
    from sklearn.cluster import KMeans
    import pandas

    dataframe = DataFrame.groupby(['Country/Region']).sum().reset_index()
    x = []
    y = []
    labels = []
    for index, row in dataframe.iterrows():
        for index_pop, row_pop in population.iterrows():
            if row_pop['country'] == row['Country/Region']:
                # ToDO:
                if not plotAllPop:
                    if row[-1] < baseline: # If number of Confirmed Cases < baseline
                        continue
                if yaxis.lower() == 'population':
                    x.append(int(row_pop['population']))
                if yaxis.lower() == 'density':
                    x.append(int(row_pop['density(P/Km2)']))
                y.append(int(row[-1]))
                labels.append(row['Country/Region'])
                break
    if yaxis.lower() == 'population':
        outframe = pandas.DataFrame({'population': x, 'confirmed':y},columns=['population','confirmed'])
    if yaxis.lower() == 'density':
        outframe = pandas.DataFrame({'density(P/Km2)': x, 'confirmed':y},columns=['density(P/Km2)','confirmed'])


    kmeans = KMeans(n_clusters=n_clusters).fit(outframe)
    centroids = kmeans.cluster_centers_

    outframe['country'] = labels
    outframe['cluster'] = kmeans.labels_.astype(float)

    return outframe, centroids

