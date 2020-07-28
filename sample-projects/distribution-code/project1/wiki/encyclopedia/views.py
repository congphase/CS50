from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, entryTitle):
    if(util.get_entry(entryTitle) == None):
        return HttpResponseNotFound('404 :D')
    return render(request, "encyclopedia/entry.html", {
        "entryTitle": entryTitle,
        "entry": util.get_entry(entryTitle)
    })
