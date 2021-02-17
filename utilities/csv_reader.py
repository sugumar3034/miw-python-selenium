import csv
import pandas


class CsvReader:

    def __init__(self, filepath):
        self.file_path = filepath

    def read_csv(self):
        reader = csv.DictReader(open(self.file_path))
        csv_data = []
        for element in reader:
            csv_data.append(element)
        return csv_data

    def pandas_read_csv(self):
        csv_data = pandas.read_csv(self.file_path)
        return csv_data
