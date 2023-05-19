from django.contrib import admin
from django.urls import path,include
from apply import views


app_name="book"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.applications,name="application"),
    path("thank/", views.thank, name="thank"),

]


