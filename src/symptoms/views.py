from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404

from .models import Symptom

class SymptomListView(ListView):
    template_name = "symptoms/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Symptom.objects.all()
    # queryset = Symptom.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(SymptomListView,self).get_context_data(*args,**kwargs)
    #     return context

def symptom_list_view(request):
    queryset = Symptom.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "symptoms/list.html", context)
