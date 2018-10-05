from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from symptomss.models import Symptom

class SearchSymptomView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchSymptomView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Symptom.objects.filter(symptom__icontains=query)
        return Symptom.objects.all()
