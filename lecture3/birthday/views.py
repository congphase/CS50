from django.shortcuts import render
import datetime

# Create your views here.
def index(request, birthday):
    now = datetime.datetime.now()
    return render(request, "birthday/index.html", {
        "birthdayflag": (now.strftime("%b").lower() == birthday[:3] and now.strftime("%d") == birthday[-2:])
    })