from main.models import *
import random
import datetime

start_lat=18.73
start_long=77.56


type1 = HealthCenterType.objects.get(pk=2)
type2 = HealthCenterType.objects.get(pk=1)

for i in range(2000):
    if i%5==0:
        name = 'Primary Health Center '+ str(i/5 +1)
        type = type1
    else:
        name = 'Sub Health Center '+ str(4*(i/5)+i%5)
        type = type2
    lat = start_lat - 3.8*random.random()
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




