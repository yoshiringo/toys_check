from django.shortcuts import render
from django.views import generic
from .models import Toys
from .forms import ToysModelForm
from django.contrib import messages
from django.shortcuts import resolve_url
from django.urls import reverse_lazy

class Index(generic.ListView):
    model = Toys
    template_name = 'toys/index.html'

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            toys_list = Toys.objects.filter(
                name__icontains=query)
        else:
            toys_list = Toys.objects.all()
        return toys_list

class Register(generic.CreateView):
    template_name = "toys/register.html"
    form_class = ToysModelForm
    success_url = "/"

    def get_success_url(self):
        messages.success(self.request, 'おもちゃ登録しました')
        return resolve_url('toys:index')

class ToysDeleteView(generic.DeleteView):
    model = Toys
    template_name = "toys/toys_delete.html"
    success_url = reverse_lazy("toys:index")

class ToysUpdateView(generic.UpdateView):
    model = Toys
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('toys:index')
