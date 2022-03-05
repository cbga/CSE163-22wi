"""
Bingan Chen (AA)
Implements all functions required for hw5. In this file,
the client can merge two dataset by their tract codes;
get the percentage of data we have for the state;
plot a state map;
plot shapes of all census tracts;
plot the previous by county;
plot the food access through income levels;
plot all low access tracts.
"""
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


def load_in_data(shp_file_name, csv_file_name):
    """
    Takes two parameters, the filename for the census dataset
    and the filename for the food access dataset. load_in_data
    should merge the two datasets on CTIDFP00 / CensusTract and
    return the result as a GeoDataFrame.
    """
    census = gpd.read_file(shp_file_name)
    food_access = pd.read_csv(csv_file_name)
    result = census.merge(food_access, left_on='CTIDFP00', right_on='CensusTract', how='left')
    return result


def percentage_food_data(state_data):
    """
    Takes the merged data and returns the percentage of census
    tracts in Washington for which we have food access data. 
    """
    have_data = state_data.dropna()
    size_wa = len(have_data)
    return 100 * size_wa / len(state_data)


def plot_map(state_data):
    """
    Takes the merged data and plots the shapes of all the census
    tracts in Washington in a file map.png
    """
    state_data.plot()
    plt.title('Washington State')
    plt.savefig('map.png')


def plot_population_map(state_data):
    """
    Takes the merged data and plots the shapes of all the census
    tracts in Washington in a file population_map.png where each
    census tract is colored according to population.
    """
    fig, ax = plt.subplots()
    state_data.plot(ax=ax, color='#EEEEEE')
    wa_data = state_data[state_data['State'] == 'WA']
    wa_data.plot(ax=ax, column='POP2010', legend=True)
    plt.title('Washington Census Tract Populations')
    plt.savefig('population_map.png')


def plot_population_county_map(state_data):
    """
    Takes the merged data and plots the shapes of all the census
    tracts in Washington in a file county_population_map.png where
    each county is colored according to population.
    """
    fig, ax = plt.subplots()
    state_data.plot(ax=ax, color='#EEEEEE')
    wa_data = state_data[state_data['State'] == 'WA']
    wa_data = wa_data.dissolve(by='County', aggfunc='sum')
    wa_data.plot(ax=ax, column='POP2010', legend=True)
    plt.title('Washington County Populations')
    plt.savefig('county_population_map.png')


def plot_food_access_by_county(state_data):
    """
    Takes the merged data and produces 4 plots on the same
    figure showing information about food access across income
    level.
    """
    slice_data = state_data[['County', 'geometry', 'POP2010', 'lapophalf', 'lapop10', 'lalowihalf', 'lalowi10']]
    agg_county = slice_data.dissolve(by='County', aggfunc = 'sum')
    agg_county['lapophalf_ratio'] = agg_county['lapophalf'] / agg_county['POP2010']
    agg_county['lapop10_ratio'] = agg_county['lapop10'] / agg_county['POP2010']
    agg_county['lalowihalf_ratio'] = agg_county['lalowihalf'] / agg_county['POP2010']
    agg_county['lalowi10_ratio'] = agg_county['lalowi10'] / agg_county['POP2010']
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))

    state_data.plot(ax=ax1, color='#EEEEEE')
    agg_county.plot(ax=ax1, column='lapophalf_ratio', legend=True, vmin=0, vmax=1)
    ax1.set_title('Low Access: Half')

    state_data.plot(ax=ax2, color='#EEEEEE')
    agg_county.plot(ax=ax2, column='lalowihalf_ratio', legend=True, vmin=0, vmax=1)
    ax2.set_title('Low Access: Half')
    
    state_data.plot(ax=ax3, color='#EEEEEE')
    agg_county.plot(ax=ax3, column='lapop10_ratio', legend=True, vmin=0, vmax=1)
    ax3.set_title('Low Access: 10')

    state_data.plot(ax=ax4, color='#EEEEEE')
    agg_county.plot(ax=ax4, column='lalowi10_ratio', legend=True, vmin=0, vmax=1)
    ax4.set_title('Low Access + Low Income: 10')
    plt.savefig('county_food_access.png')


def plot_low_access_tracts(state_data):
    """
    Takes the merged data and plots all census tracts
    considered “low access” in a file low_access.png.
    """
    rural = state_data['Rural'] == 1
    urban = state_data['Urban'] == 1
    rural_pl = state_data[rural]
    urban_pl = state_data[urban]
    tot_rr = rural_pl['POP2010']
    tot_ub = urban_pl['POP2010']
    wa_data = state_data.dropna()
    r_low_1 = rural_pl['lapop10'] >= 500
    r_low_2 = (rural_pl['lapop10'] / tot_rr) >= 0.33
    u_low_1 = urban_pl['lapophalf'] >= 500
    u_low_2 = (urban_pl['lapophalf'] / tot_ub) >= 0.33
    fig, ax = plt.subplots(1)
    state_data.plot(ax=ax, color='#EEEEEE')
    wa_data.plot(ax=ax, color='#AAAAAA')
    rural_pl[r_low_1 | r_low_2].plot(ax=ax)
    urban_pl[u_low_1 | u_low_2].plot(ax=ax)
    plt.title('Low Access Census Tracts')
    plt.savefig('low_access.png')


def main():
    state_data = load_in_data(
        'food_access/tl_2010_53_tract00/tl_2010_53_tract00.shp',
        'food_access/food_access.csv'
    )
    print(percentage_food_data(state_data))
    plot_map(state_data)
    plot_population_map(state_data)
    plot_population_county_map(state_data)
    plot_food_access_by_county(state_data)
    plot_low_access_tracts(state_data)


if __name__ == '__main__':
    main()
