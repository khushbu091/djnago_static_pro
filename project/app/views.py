from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
# def about(request):
#     return render(request, 'about.html')
# def contact(request):
#     return render(request, 'contact.html')
# def details(request):
#     return render(request, 'details.html')
# def electronic(request):
#     return render(request, 'electronic.html')