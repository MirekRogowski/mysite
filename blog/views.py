from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from .models import Post, Category, Comment
from .forms import PostForm, UpdateForm, CategoryForm, CommentForm, NewsletterForm, SendMailForm


class HoneView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = 'posts'
    queryset = Post.objects.filter(status='publish')
    ordering = ['-created_date']


class EditView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'posts'
    ordering = ['-created_date']
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
    success_url = reverse_lazy("post-list")
    success_message = "Add post"

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Nowy post został dodany'
        )
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = UpdateForm
    success_url = reverse_lazy("post-list")
    context_object_name = 'post'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Post został zaktualizowany'
        )
        return super().form_valid(form)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Post został usunięty'
        )
        return super().form_valid(form)


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
        return super().form_valid(form)
    # zakomentowane linie poniewż używamy CategoryForm
    # fields = "__all__"
    # fields = ['author', 'title', 'title_tag', 'text']


# def post_category_view(request, category):
#     category_posts = Post.objects.filter(category=category)
#     return render(request, 'blog/category_post.html',
#                   {'category': category, 'category_posts': category_posts})


class PostCategoryView(ListView):
    context_object_name = 'category_name'
    template_name = 'blog/category_post.html'
    ordering = ['-created_date']

    def get_queryset(self):
        content = {
            'cat': Category.objects.get(id=self.kwargs['category']),
            'posts': Post.objects.filter(category=self.kwargs['category']).filter(status='publish'),
        }
        return content


class AddNewsLetter(CreateView):
    form_class = NewsletterForm
    template_name = 'blog/newsletter.html'
    success_url = reverse_lazy("newsletter")

    # def get_success_message(self, cleaned_data):
    #     print(cleaned_data)
    #     return "Zapisałeś się na newslette"
    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Zapisałeś się na newsletter'
        )
        return super().form_valid(form)


class SendPostView(UpdateView):
    model = Post
    template_name = 'blog/newsletter_send.html'
    form_class = SendMailForm
    success_url = reverse_lazy("post-list")
    context_object_name = 'send'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Post został zaktualizowany'
        )
        return super().form_valid(form)

