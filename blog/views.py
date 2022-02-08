from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from .models import Post
from .forms import PostForm, UpdateForm



# Create your views here.
# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#     return render(request, 'blog/index.html', {'posts': posts})


class HoneView(ListView):
    model = Post
    template_name = "blog/index.html"


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_add.html'
    # zakomentowane linie poniewż używamy PostForm
    # fields = "__all__"
    # fields = ['author', 'title', 'title_tag', 'text']


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = UpdateForm
    # fields = ['title', 'title_tag', 'text']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

