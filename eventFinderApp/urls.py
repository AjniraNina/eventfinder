from django.urls import path
from . import views
#from rest_framework.authtoken import views

app_name = 'eventFinderApp'
urlpatterns = [
    path('test', views.test),
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # event-finder/my-account
    path('my-account/', views.account, name='account'),
    # event-finder/event_creator_form
    path('event_creator_form/', views.add_event, name='event_creator_form'),
    #event_creator_form
    #path(r'api-auth-token/', views.obtain_auth_token),
    #tokens
]