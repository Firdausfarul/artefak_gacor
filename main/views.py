from django.shortcuts import render
import random
import requests
# Create your views here.
def show_main(request):
    context = reqnft()
    return render(request, "main.html", context)

def reqnft():
    temp = random.randint(1, 124)
    res = requests.get(f'https://raw.githubusercontent.com/Firdausfarul/Intft_stellar/main/img/test/{temp}.json')
    res = res.json()
    img_url = res['image']
    emoji = res['name']
    country = res['attributes'][0]['value']
    continent = res['attributes'][1]['value']
    return {
        'name': "Crimson Witch of Flames",
        'part': 'Goblet of Eonothem',
        'amount': random.randint(1, 100),
        'description': "Artifact suitable for pyro character",
        'img': img_url,
        'emoji': emoji,
        'country': country,
        'continent': continent,
        'price': random.randint(4, 159)
    }