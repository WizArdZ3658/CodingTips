from abc import ABC

from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post, Comment

"""posts = [
    {
        'author': 'Somnath',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Meenal',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'
    }
]"""


def home(request):  # not using this
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # looks for <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('blog/like_section.html', context, request=request)
        return JsonResponse({'form': html})
    # return redirect('post_detail', pk=post.pk)


def vote_comment(request):
    comment = get_object_or_404(Comment, id=request.POST.get('id'))
    mode = request.POST.get('mode')

    if mode == 'downvote':
        if comment.downvotes.filter(id=request.user.id).exists():
            comment.downvotes.remove(request.user)
        else:
            if comment.upvotes.filter(id=request.user.id).exists():
                comment.upvotes.remove(request.user)
            comment.downvotes.add(request.user)

    elif mode == 'upvote':
        if comment.upvotes.filter(id=request.user.id).exists():
            comment.upvotes.remove(request.user)
        else:
            if comment.downvotes.filter(id=request.user.id).exists():
                comment.downvotes.remove(request.user)
            comment.upvotes.add(request.user)

    context = {
        'post': comment.post
    }
    if request.is_ajax():
        html = render_to_string('blog/comment_section.html', context, request=request)
        return JsonResponse({'form': html})


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # looks for <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        is_liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            is_liked = True
        context['is_liked'] = is_liked
        context['total_likes'] = post.total_likes()
        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):  # use loginrequiredmixin cause cant use decorators on classes
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # use loginrequiredmixin cause cant use
    model = Post  # decorators on classes
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


def autocomplete(request):
    if request.is_ajax():
        queryset = Post.objects.filter(title__istartswith=request.GET.get('search', None))
        list = []
        for i in queryset:
            list.append(i.title)
        data = {
            'list': list,
        }
        return JsonResponse(data)


def search_blogpost(request):
    if request.is_ajax():
        post = Post.objects.filter(title=request.GET.get('title', None))
        # print(post)
        id = 0
        if len(post) == 0:
            id = -1
        else:
            # print(post[0].id)
            id = post[0].id
        data = {
            'id': id,
        }
        return JsonResponse(data)