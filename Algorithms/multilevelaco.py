import math
import random
import time

import WorldCitiesDatabase
from Ants import Ant
from WorldCitiesDatabase import City, Region, Country


class MultilevelACO(object):
    """
    Multilevel ACO implementation for solving travel salesman problem
    """

    __database: WorldCitiesDatabase.Database = None
    """ The database that is used """

    __traverse_levels = [WorldCitiesDatabase.Country, WorldCitiesDatabase.Region, WorldCitiesDatabase.City]
    """ The levels to do traversing on """

    __runs_without_improvement = 0
    """ The amount of runs without any improvement """

    __converge_threshold: int = 100000
    """ The amount of runs to do before it is considered converged """

    __best_ant: Ant = None
    """ The ant with the best score """

    __cities_to_visit: int = None
    """ The amount of cities to visit before going to the destination """

    __country_sequence: list = None
    """ The best discovered sequence of countries """

    __region_sequence: list = None
    """ The best discovered sequence of regions """

    def __init__(self, database: WorldCitiesDatabase.Database):
        self.__traverse_level = None
        self.__database = database

    def find_shortest_path_between(self, origin: City, destination: City, visiting_cities: int) -> list:
        """
        Finds one of the shortest paths between origin and destination when you have to visit the given
        amount of cities. Returns the best found sequence of cities.
        :param origin: City
        :param destination: City
        :param visiting_cities: int
        :return:
        """

        # Assign amount of cities to visit to the class
        self.__cities_to_visit = visiting_cities

        # Print a summary
        print(f"Start: {origin.name} - {origin.get_region().name} - {origin.get_country().name}")
        print(f"Destination: {destination.name} - {destination.get_region().name} - {destination.get_country().name}")
        print(f"Amount of cities to visit: {str(visiting_cities)}")

        # Count the iterations
        iterations = 0

        # Start timer
        start_time = time.time()

        print(f"============================================================")
        for traverse_level in self.__traverse_levels:

            # Reset runs to zero
            self.__runs_without_improvement = 0

            # Run til level has converged
            while self.__runs_without_improvement < self.__converge_threshold:

                iterations += 1

                # Initialize an Ant
                ant = Ant()                 # type: Ant
                ant.starting_city = origin
                ant.current_city = origin
                ant.destination_city = destination

                while len(ant.visited_cities) <= self.__cities_to_visit:
                    # Get next city
                    next_city = self.__get_next_city(ant, traverse_level)

                    # Assign next city
                    ant.visited_cities.append(next_city)
                    ant.current_city = next_city

                # Get the score for the ant
                ant = self.__calculate_score(ant)

                # Check if current ant beats the previous best ant
                if self.__best_ant is None or self.__best_ant.score > ant.score:
                    self.__best_ant = ant
                    self.__runs_without_improvement = 0
                    print(f"Found new best route with score: {ant.score}")

                    if traverse_level is Country:
                        self.__country_sequence = [city.get_country() for city in ant.visited_cities]

                    if traverse_level is Region:
                        self.__region_sequence = [city.get_region() for city in ant.visited_cities]

                    continue

                self.__runs_without_improvement += 1

            print(f"Search has converged on traverse level {traverse_level.__name__}")

        self.__print_best_route()
        print(f"Iterations: {iterations}")
        print(f"Total time elapsed: {time.time()-start_time} ")

        return self.__best_ant.visited_cities

    def __print_best_route(self) -> None:
        """
        Prints a summary of the best route discovered
        :return: None
        """
        best_ant = self.__best_ant  # type: Ant
        print("============================================================")
        print(f"Best route, score {best_ant.score}: ")
        for index, city in enumerate(self.__best_ant.visited_cities):
            print(f"{index}. - {city.name} - {city.get_region().name} - {city.get_country().name}")
        print("============================================================")

    def __calculate_score(self, ant) -> Ant:
        """
        Calculates the score for the ant
        :param ant:
        :return:
        """
        distance: float = 0.0

        # Calculate the distance for each
        for index, city in enumerate(ant.visited_cities):

            # Check if on last element
            if index == len(ant.visited_cities)-1:
                break

            next_city = ant.visited_cities[index+1]     # type: City
            distance += self.__calculate_vector_distance(city.get_coordinates(), next_city.get_coordinates())

        ant.score = distance

        return ant

    def __get_next_city(self, ant: Ant, traverse_level) -> City:
        """
        Get the next city that the ant should visit
        :param ant:
        :return: City
        """

        if len(ant.visited_cities)+1 >= self.__cities_to_visit:
            return ant.destination_city

        if traverse_level is Country:
            country = random.choice(list(self.__database.countries.values()))           # type: Country
            next_city = list(country.get_cities())[0]
            return next_city
        elif traverse_level is Region:
            visited_cities = len(ant.visited_cities)
            next_country = self.__country_sequence[visited_cities]                      # type: Country
            next_region = random.choice(next_country.get_regions())                     # type: Region
            return next_region.get_cities()[0]
        elif traverse_level is City:
            visited_cities = len(ant.visited_cities)
            next_region = self.__region_sequence[visited_cities]                        # type: Region
            next_city = random.choice(next_region.get_cities())                         # type: City
            return next_city

        raise Exception(f"Unknown traverse level: {traverse_level}")

    @staticmethod
    def __calculate_vector_distance(vector_x, vector_y):
        """
        Calculates the absolute value of the distance between vector x and vector y
        :param vector_x: tuple(float, float)
        :param vector_y: tuple(float, float)
        :return: float
        """
        return math.fabs(math.sqrt(((vector_y[0]-vector_x[0])**2)+(vector_y[1]-vector_x[1])**2))
