from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
import django.views.defaults
from django.http import HttpResponse
import csv

from .models import Fish
from .models import User

from time import strptime


def homepage(request):
    # importData()
    context = {
        "page": "map",
    }
    return render(request, 'template.html', context)


def listFish(request):
    data = []
    for fish in Fish.objects.all():
        row = {
            "name": fish.name,
            "location": fish.get_location_display(),
            "size": fish.get_size_display(),
            "months": fish.months,
            "times": fish.times,
            "price": fish.price,
            "caught": request.user.is_authenticated and (
                        User.objects.filter(user_id=request.user, caught__name=fish.name).count() == 1)
        }
        data.append(row)
    # test = {"authenticated": request.user.is_authenticated, "id": request.user.id}
    return JsonResponse(data, safe=False)
    # return render(request, 'fish.json', context)
    # pass


def changeCaught(request):
    if (not request.user.is_authenticated):
        return django.views.defaults.HttpResponseForbidden()
    name = request.GET.get('name', None)
    caught = request.GET.get('caught', None)
    if (name is None or caught is None):
        print("name or caught is None. name: {}, caught: {}".format(name, caught))
        return django.views.defaults.HttpResponseBadRequest()
    caught = caught == "true"
    try:
        user = User.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
        print("Creating user")
        user = User(user_id=request.user.id)
        user.save()

    try:
        fish = Fish.objects.get(name=name)
    except ObjectDoesNotExist:
        print("Fish {} not found in database".format(name))
        return django.views.defaults.HttpResponseBadRequest()

    if (caught):
        user.caught.add(fish)
    else:
        user.caught.remove(fish)
    user.save()
    return HttpResponse(status=204)


def logout_view(request):
    logout(request)
    return redirect('index')
