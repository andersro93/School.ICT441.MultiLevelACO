import os
from typing import List

from WorldCitiesDatabase import Database, City, Region, Country


class DatabaseParser(object):

    import_file_path = "/assets/world_cities_pop.txt"
    """ The path to the data importer """

    file_encoding = 'Latin-1'
    """ The encoding used on the import file """

    minimum_population = 50000
    """ The minimum population for a city to be imported """

    __column_country = 0
    """ The column number of country name """

    __column_region = 3
    """ The column number of region name """

    __column_city = 1
    """ The column number of city name """

    __column_population = 4
    """ The column number of population """

    __column_longitude = 6
    """ The column number of longitude """

    __column_latitude = 5
    """ The column number of latitude """

    __column_delimiter = ","
    """ The delimiter between columns"""

    __database = None
    """ The database that is created """

    def __init__(self):
        self.__database = Database()

    def create_database(self):
        """
        Parses the file and creates a pre-defined database based on the import files properties
        :return: Database
        """
        print(f"Starting database generation")
        file_contents = self.__read_file_contents()

        for index, line in enumerate(file_contents):
            self.__parse_line(line)

            if index % 100000 == 0 and index is not 0:
                print(f"Done parsing record number: {index}")

        print(f"Done generating the database")
        self.__database.print_database_summary()

        return self.__database

    def __parse_line(self, line: str):
        """
        Parses the given line
        :param line:
        :return:
        """
        exploded_line: List[str] = line.split(self.__column_delimiter)

        country_raw = exploded_line[self.__column_country]
        region_raw = exploded_line[self.__column_region]
        city_raw = exploded_line[self.__column_city]
        population_raw = int(exploded_line[self.__column_population]) if exploded_line[self.__column_population] else 0
        long_raw = float(exploded_line[self.__column_longitude]) if exploded_line[self.__column_longitude] else None
        lat_raw = float(exploded_line[self.__column_latitude]) if exploded_line[self.__column_latitude] else None

        if population_raw < self.minimum_population:
            return self

        if long_raw is None or lat_raw is None:
            return self

        country: Country
        if country_raw in self.__database.countries:
            country = self.__database.countries[country_raw]
        else:
            country = Country(country_raw)
            self.__database.countries[country_raw] = country

        region: Region
        if f"{country_raw}-{region_raw}" in self.__database.countries:
            region = self.__database[f"{country_raw}-{region_raw}"]
        else:
            region = Region(region_raw, country)
            country.add_region(region)
            self.__database.regions[f"{country_raw}-{region_raw}"] = region

        city: City
        if f"{country_raw}-{region_raw}-{city_raw}" in self.__database.cities:
            city = self.__database.cities[f"{country_raw}-{region_raw}-{city_raw}"]
        else:
            city = City(city_raw, region, country)
            city.set_population(population_raw)
            city.set_coordinates(longitude=long_raw, latitude=lat_raw)
            country.add_city(city)
            region.add_city(city)
            self.__database.cities[f"{country_raw}-{region_raw}-{city_raw}"] = city

        return self

    def __read_file_contents(self) -> list:
        data: str
        try:
            with open(os.getcwd() + self.import_file_path, 'r', encoding=self.file_encoding) as file_reader:
                data = file_reader.read()
                file_reader.close()

        except Exception as e:
            print(f"Unable to parse file: {os.getcwd() + cls.import_file_path}")
            raise e
            return list()

        lines = data.splitlines()

        if len(lines) == 0:
            print(f"Not a proper file")
            return list()

        return lines[1:]



