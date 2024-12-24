from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from django.views.generic import ListView, DetailView , FormView, CreateView, UpdateView, DeleteView
from .forms import PostCreatForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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

class PostList(PermissionRequiredMixin,ListView):
    permission_required = 'blog.view_post'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    ordering = 'id'




class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'




# class PostCreatFormView(FormView):
#     template_name = "blog/form.html"
#     form_class = PostCreatForm
#     success_url = '/post'
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class PostCreatView(CreateView):
    model = Post
    fields = ['title', 'content', 'category', 'status', 'published_date']
    success_url = '/post'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','content']
    success_url = '/post'









class PostDeleteView(DeleteView):
    model = Post
    success_url = '/post'
