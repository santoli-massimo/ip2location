

import csv

from pymongo import MongoClient
connection = MongoClient()


db = connection.get_database('ip2location')
collection = db.get_collection('ipmap')


with open('0_ip2location_split.csv', 'rb') as csvfile:
    ipreader = csv.reader(csvfile, delimiter=',')
    for row in ipreader:
        cacca = collection.insert_one(
            {
                "range1":row[0],
                "range2":row[1],
                "county_code":row[2],
                "country":row[3]
            })

        print cacca

        

