from django.conf.urls import url

from .views import (
        SymptomListView
        )

urlpatterns = [
    url(r'^$', SymptomListView.as_view(), name="list"),

]
