from djangonepal.models import Province,District,Municipality
import csv
import os
import sys

import os
mypath = os.path.abspath(__file__)
finalpath = os.path.dirname(mypath)
def run():
    with open(f'{finalpath}/geo-data.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Province.objects.all().delete()
        District.objects.all().delete()
        Municipality.objects.all().delete()

        for row in reader:
            print(row)

            province, _ = Province.objects.get_or_create(name=row[0])

            district, _ = District.objects.get_or_create(district=row[1],province=province)
            municipality = Municipality(municipality=row[2],district=district,province=province)
            municipality.save()
