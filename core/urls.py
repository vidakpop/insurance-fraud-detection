from django.urls import path,include

from core import views
app_name="core"

urlpatterns=[
    path("", views.index,name="index"),
    path("profile/",views.profile,name="profile"),
    path("predict/", views.predict,name="predict"),
    path("predict/result", views.formInfo,name="result"),
]