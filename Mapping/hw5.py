def load_in_data(shp_file_name, csv_file_name):
    pass


def percentage_food_data(state_data):
    pass


def plot_map(state_data):
    pass


def plot_population_map(state_data):
    pass


def plot_population_county_map(state_data):
    pass


def plot_food_access_by_county(state_data):
    pass


def plot_low_access_tracts(state_data):
    pass


def main():
    state_data = load_in_data(
        '/course/food_access/tl_2010_53_tract00/tl_2010_53_tract00.shp',
        '/course/food_access/food_access.csv'
    )
    print(percentage_food_data(state_data))
    plot_map(state_data)
    plot_population_map(state_data)
    plot_population_county_map(state_data)
    plot_food_access_by_county(state_data)
    plot_low_access_tracts(state_data)


if __name__ == '__main__':
    main()
