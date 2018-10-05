from django.conf.urls import url

from .views import (
        DiseaseListView
        )

urlpatterns = [
    url(r'^$', DiseaseListView.as_view(), name="query"),
]
