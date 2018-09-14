from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404

from symptoms.models import Symptom

class SearchSymptomView(ListView):
    template_name = "symptoms/list.html"

    def get_queryset(self, *args, **kwargs):
        context = super(SearchSymptomView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        request = self.request
        return Symptom.objects.all()

    def get_context_data(self, *args, **kwargs):
        request = self.request
        method_dict = resquet.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Symptom.objects.search(query)
        return "Sympyom does not exists"
