from django.conf.urls import url

from .views import (
        SearchSymptomView,
        )

urlpatterns = [
    url(r'^$', SearchSymptomView.as_view(), name="query"),
]
