from django.shortcuts import render
from .models import Person


#write views here
def index(request):
    letter = request.GET.get('letter', '')
    # Case-insensitive filter
    persons = Person.objects.filter(name__istartswith=letter)
    
    # Case-sensitive filter (use __startswith for case-sensitive)
    # persons = Person.objects.filter(name__startswith=letter)

    context = {'persons': persons}
    return render(request, 'index.html', context)