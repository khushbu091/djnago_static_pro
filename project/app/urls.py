from django.urls import path
from  .views import home


urlpatterns = [
    path('home/', home, name='home')
    # path('about/', about, name='about'),
    # path('electronic/', electronic, name='electronic'),
    # path('details/', details, name='details'),
    # path('contact/', contact, name='contact'),

]
