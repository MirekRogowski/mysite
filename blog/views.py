from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView, TemplateView, FormView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from .models import Post, Category, Comment, Newsletter, NewsLetterPost
from .forms import PostForm, CategoryForm, CommentForm, \
    NewsLetterForm, NewsLetterPostForm, ContactForm

from django.apps import apps


class PostListView(ListView):
    model = Post
    # template_name = "blog/index.html"
    context_object_name = 'posts'
    queryset = Post.objects.filter(status='publish')
    ordering = ['-created_date']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = "blog/posts_user.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).filter(status='publish').order_by('-created_date')


class PostAuthorizedView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'posts'
    ordering = ['-created_date']
    paginate_by = 5
    # queryset = Post.objects.filter(status='publish').latest()


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comments.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, email=email, content=content, post=post
            )

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)
        return self.render_to_response(context=context)


class AddPostView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_add.html'
    success_url = reverse_lazy("post-add")
    success_message = "Post został dodany"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        return {'author': self.request.user}


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = PostForm
    success_url = reverse_lazy("post-list")
    context_object_name = 'post'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Post został zaktualizowany'
        )
        print(form.cleaned_data)
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    # success_url = reverse_lazy('post-list')
    success_url = '/post-list'
    success_message = "Post został usunięty"

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Post został usunięty'
        )
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AddCategoryView(CreateView):
    model = Post
    form_class = CategoryForm
    template_name = 'blog/category_add.html'
    success_url = reverse_lazy("category-add")

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            f'Dodano nową kategorię',
        )
        print(form.cleaned_data)
        return super().form_valid(form)

# def post_category_view(request, category):
#     category_posts = Post.objects.filter(category=category)
#     return render(request, 'blog/category_post.html',
#                   {'category': category, 'category_posts': category_posts})


class PostCategoryView(ListView):
    context_object_name = 'posts'
    template_name = 'blog/posts_category.html'
    ordering = ['-created_date']
    paginate_by = 5

    def get_queryset(self):
        category = get_object_or_404(Category, name=self.kwargs.get('category'))
        return Post.objects.filter(category=category).filter(status='publish').order_by('-created_date')

    # def get_queryset(self):
    #     content = {
    #         'cat': Category.objects.get(id=self.kwargs['category']),
    #         'posts': Post.objects.filter(category=self.kwargs['category']).filter(status='publish'),
    #     }
    #     return content



class AddNewsLetterView(CreateView):
    model = Newsletter
    form_class = NewsLetterForm
    template_name = 'blog/newsletter.html'
    success_url = reverse_lazy("newsletter")


    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Zapisałeś się na newsletter'
        )
        email = form.cleaned_data.get('email')
        return super().form_valid(form)


class NewsLetterPostView(DetailView):
    model = Post
    template_name = 'blog/newsletter_send.html'
    form_class = NewsLetterPostForm
    success_url = reverse_lazy("success")
    context_object_name = 'send'

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     print(form)
    #     return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Zapisałeś się na newsletter'
        )
        email = form.cleaned_data.get('email')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(NewsLetterPostView, self).get_context_data(**kwargs)
        context['title'] = self.get_object().title
        print("tytul---1", self.get_object().title)
        context['content'] = self.get_object().content
        print("contemt---2", self.get_object().content)
        return context

    def send(self, request, **kwargs):
        form = NewsLetterPostForm
        post = self.get_object()
        context = super(NewsLetterPostView, self).get_context_data(**kwargs)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            emails = NewsLetterPost.object.create(post=post)
