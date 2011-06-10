from main.models import *
import random
import datetime

start_lat=19.2
start_long=77.56


type1 = HealthCenterType(name='Primary Health Center', description='')
type1.save()

type2 = HealthCenterType(name='Sub Center', description='')
type2.save()

def create():
    for i in range(1000):
        if i%5==0:
            name = type1.name + ' '+ str(i/5 +1)
            type = type1
        else:
            name = type2.name + ' ' + str(4*(i/5)+i%5)
            type = type2
        lat = start_lat - 4.5*random.random()
        long = start_long + 2.24*random.random()
        h = HealthCenter(name=name, type=type, latitude=lat, longitude=long, description='')
        h.save()
        print h

    hc_set = HealthCenter.objects.all()
    rating_criterias = RatingCriteria.objects.all()

    for hc in hc_set:
        for rc in rating_criterias:
            r = Rating(value=random.randint(int(rc.min_value)+1, int(rc.max_value)), health_center=hc, criteria=rc, date=datetime.datetime.now())
            r.save()
            print r

