#!/bin/python3
from Algorithms import MultilevelACO
from DataFetcher import WorldCitiesDataFetcher
from WorldCitiesDatabase.database_parser import DatabaseParser

if __name__ == '__main__':
    # Ensure that the data is in place
    WorldCitiesDataFetcher().ensure_assets_file_in_place()

    # Create the database
    database = DatabaseParser().create_database()

    # Get two random cities
    city_x, city_y = database.get_two_random_cities()

    MultilevelACO(database).find_shortest_path_between(city_x, city_y, 5)

