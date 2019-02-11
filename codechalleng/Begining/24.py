def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""

    return set(my_cities).symmetric_difference(set(other_cities))
    # return len(cities_a)


my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
other_cities = ['Paris', 'Boston', 'Sydney', 'Madrid', 'Moscow', 'Lima']

uncommon_cities(my_cities, other_cities)