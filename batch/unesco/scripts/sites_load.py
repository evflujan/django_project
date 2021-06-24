import csv

# python3 manage.py runscript sites_load

from unesco.models import Category, State, Region, Iso, Site
from decimal import *

file = '/home/evflujan/Coursera/Lab/django_project/batch/unesco/whc-sites-2018-clean.csv'

def run():
    fhand = open(file)
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row[0],row[3],row[7],row[8],row[9],row[10])

        try:
            y = int(row[3])
        except:
            y = None

        if row[6] == '0' or row[6] == '':
            a = None
        else:
            a = Decimal(row[6].replace(',','.'))

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])
        sit = Site(
            name=row[0],
            year=y,
            area_hectares=a,
            category=c,
            state=s,
            region=r,
            iso=i,
            )
        sit.save()
