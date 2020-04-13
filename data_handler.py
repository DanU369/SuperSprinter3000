import os
import csv

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    with open('/home/dan/PycharmProjects/Sprinter3000/data.csv') as csvfile:
        result = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            new = dict(row)
            result.append(new)
        return result

def write_to_file(datafile):
    with open('/home/dan/PycharmProjects/Sprinter3000/data.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=DATA_HEADER)
        writer.writeheader()
        for item in datafile:
            writer.writerow(item)



