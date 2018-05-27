import urllib.request
import io
import gzip
from pathlib import Path

import self as self


class WorldCitiesDataFetcher(object):
    """
    Helper class for downloading the assets files
    """

    save_location: str = "./assets/world_cities_pop.txt"
    """ The location to unpack and save the downloaded file """

    __download_url: str = "http://download.maxmind.com/download/worldcities/worldcitiespop.txt.gz"
    """ Download url to the world cities dataset """

    def __init__(self):
        """
        WorldCitiesDataFetcher constructor
        """
        super(WorldCitiesDataFetcher, self).__init__()

    def download_and_unpack_data(self) -> self:
        """
        Downloads and unpacks the compressed file into the path specified by class
        :return: self
        """
        print('Starting file and de-compression task, please hang on')
        response = urllib.request.urlopen(self.__download_url)
        compressed_file = io.BytesIO(response.read())
        decompressed_file = gzip.GzipFile(fileobj=compressed_file)

        with open(self.save_location, 'wb') as outfile:
            outfile.write(decompressed_file.read())

        print('File and de-compression complete')
        return self

    def ensure_assets_file_in_place(self) -> self:
        """
        Ensures that the project has the assets files needed to continue
        :return: self
        """
        print(f'Checking if file {self.save_location} exists')

        if Path(self.save_location).is_file():
            print('The file exists, no download is needed')
            return self

        print('The file does not exist')

        return self.download_and_unpack_data()
