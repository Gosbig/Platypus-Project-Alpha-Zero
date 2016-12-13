import os
import csv

from email import email_user
from converter import csv_converter

def main():
    #Launch GUI (user_input) WIP
    #Call dict_converter to write dict to xls file (automatic?)
    #email.py said xls file to email.py address provided in user_input via xls_email


    my_dict = {
        'Apples' : 12,
        'Oranges' : 15,
        'Bananas' : 20,
        'Limes' : 8,
    }

    current_path = os.getcwd()
    inventory_csv = current_path

    inventory_columns = ['Row', 'Item', 'Amount']

    csv_converter.csv_writer(inventory_csv,inventory_columns,my_dict)



    close_app = False

    if close_app == True:
        email_user()


if __name__ == '__main__':
    main()