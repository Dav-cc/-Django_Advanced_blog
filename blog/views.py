from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
# Create your views here.

def indexview(request):
    return render(request, 'base.html', context = {"name" : "mmad"})

class HomeView(TemplateView):
    template_name = "base.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context
