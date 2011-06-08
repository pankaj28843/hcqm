from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

import json

from main.models import *

def home(request):
    hctypes = HealthCenterType.objects.all()
    return render(request, 'main/home.html', {'hctypes':hctypes})

def show_ratings(request, hctype_id):
    hctype = HealthCenterType.objects.get(id=hctype_id)
    rating_criterias = RatingCriteria.objects.all().order_by('-max_value')
    return render(request, 'main/show_ratings.html', {'hctype':hctype,
        'rating_criterias':rating_criterias})

def get_health_centers(request, hctype_id):
    hctype = HealthCenterType.objects.get(id=hctype_id)
    health_centers = hctype.get_health_centers()
    mimetype = 'application/json'
    json_serializer = serializers.get_serializer('json')()
    data = json_serializer.serialize(health_centers, ensure_ascii=False)
    return HttpResponse(data, mimetype)

def get_ratings(request, hctype_id, rc_id=0):
    hctype = HealthCenterType.objects.get(id=hctype_id)
    ratings = []
    for hc in hctype.get_health_centers():
        ratings.append(hc.get_rating(rc_id=rc_id))
    try:
        c = RatingCriteria.objects.get(id=rc_id)
        max_value = c.max_value
        min_value = c.min_value
        name = c.name
        description = c.description

    except:
        criterias = RatingCriteria.objects.all()
        max_value = 0
        min_value = 0
        name = 'Overall Rating'
        description = ''
        for c in criterias:
            max_value = max_value + c.max_value
            min_value = min_value + c.min_value
    
    mimetype = 'application/json'
    data = json.dumps([{'max_value':max_value, 'min_value':min_value,
        'name':name, 'description':description}, ratings])
    return HttpResponse(data, mimetype)

