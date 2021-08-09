from django.contrib import admin
from django.urls import path
from biceps4u import views

urlpatterns = [ 
    path("", views.index, name = 'biceps4u'),
    path("aboutus", views.aboutus, name = 'aboutus'),
    path("workouts", views.workouts, name = 'workouts'),
    path("gallary", views.gallary, name = 'gallary'),
    path("packages", views.packages, name = 'packages'),
    path("social", views.social, name = 'social'),
    path("contactus", views.contactus, name = 'contactus'),
]