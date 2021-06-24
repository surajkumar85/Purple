from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="start_page"),
    path("about/",views.about,name="about_page"),
    path("pricing/",views.pricing,name="pricing_page"),
    path("contact/",views.contact,name="contact_page"),
    path("work/",views.work,name="work_page"),
]