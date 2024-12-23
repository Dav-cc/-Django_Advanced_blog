from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from django.views.generic import ListView, DetailView , FormView
from .forms import PostCreatForm
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

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 2
    ordering = 'id'




class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'




class PostCreatFormView(FormView):
    template_name = "blog/form.html"
    form_class = PostCreatForm
    success_url = '/post'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
