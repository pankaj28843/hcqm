from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from main.models import *

def home(request):
    hctypes = HealthCenterType.objects.all()
    return render(request, 'main/home.html', {'hctypes':hctypes})

def show_ratings(request, hctype_id):
    hctype = HealthCenterType.objects.get(id=hctype_id)
    return render(request, 'main/show_ratings.html', {'hctype':hctype})

def get_health_centers(request, hctype_id):
    hctype = HealthCenterType.objects.get(id=hctype_id)
    health_centers = hctype.get_health_centers()
    mimetype = 'application/json'
    json_serializer = serializers.get_serializer('json')()
    data = json_serializer.serialize(health_centers, ensure_ascii=False)
    return HttpResponse(data, mimetype)

def get_ratings(request, hctype_id):
    hctype = HealthCenterType.objects.get(id=hctype_id)
    ratings = hctype.get_ratings()
    mimetype = 'application/json'
    json_serializer = serializers.get_serializer('json')()
    data = json_serializer.serialize(ratings, ensure_ascii=False)
    return HttpResponse(data, mimetype)

