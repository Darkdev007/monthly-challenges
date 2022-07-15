from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

months_dictionary = {
    'january' : 'Read for 120 minutes',
    'february' : 'Read for 110 minutes',
    'march' : 'Read for 100 minutes',
    'april' : 'Read for 90 minutes',
    'may' : 'Read for 80 minutes',
    'june' : 'Read for 70 minutes',
    'july' : 'Read for 60 minutes',
    'august' : 'Read for 50 minutes',
    'september' : 'Read for 40 minutes',
    'october' : 'Read for 30 minutes',
    'november' : 'Read for 20 minutes',
    'december' : 'Read for 10 minutes',
}

def index(request):
    response_data = ""
    months = list(months_dictionary.keys())
    for month in months:
        capital = month.capitalize()
        month_url = reverse('month-challenges', args=[month])
        response_data += f"<li><a href= \"{month_url}\">{capital}</a></li>"
    return HttpResponse(f'<ul>{response_data}</ul>')
def number(request, month):
    months = list(months_dictionary.keys())
    if month > len(months):
        return HttpResponseNotFound('You have entered an invalid month')
    else:
        redirect_month = months[month-1]
        redirect_url = reverse('month-challenges', args=[redirect_month])
        return HttpResponseRedirect(redirect_url)

def show_task(request, month):
    try:
        challenge_response = months_dictionary[month]
        return HttpResponse(challenge_response)
    except:
        return HttpResponseNotFound('You have entered an invalid month')



