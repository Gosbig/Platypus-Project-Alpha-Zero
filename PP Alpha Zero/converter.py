import os
import csv

class csv_converter:

    def csv_writer(inventory_csv, inventory_columns, my_dict):

        with open(inventory_csv, 'w', newline='') as myCSVFile:
            csvWriter = csv.DictWriter(myCSVFile, fieldnames=inventory_columns, dialect='excel',
                                       quoting=csv.QUOTE_NONNUMERIC)
            csvWriter.writeheader()
            for data in my_dict:
                csvWriter.writerow(data)


        return