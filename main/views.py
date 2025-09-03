from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406495994',
        'name': 'Abdurrahman Ammar Abqary',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)