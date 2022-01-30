from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db.models import Q
from django.http import HttpResponse

from blog.models import BlogPost
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm

from django.contrib.auth.decorators import login_required


@login_required
def create_blog_view(request):

    context = {}
    form = CreateBlogPostForm()

    context['form'] = form

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    if request.method == 'POST':
        form = CreateBlogPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = request.user
            obj.author = author
            obj.save()

        return redirect(reverse('blog'))

    return render(request, "blog/create_blog.html", context)


def detail_blog_view(request, slug):

    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'blog/detail_blog.html', context)


def edit_blog_view(request, slug):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    blog_post = get_object_or_404(BlogPost, slug=slug)

    if blog_post.author != user:
        return HttpResponse('You are not the author of that post.')

    if request.POST:
        form = UpdateBlogPostForm(request.POST or None,
                                  request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj

    form = UpdateBlogPostForm(
            initial={
                    "title": blog_post.title,
                    "body": blog_post.body,
                    "image": blog_post.image,
            }
        )

    context['form'] = form
    return render(request, 'blog/edit_blog.html', context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a blog """

    blog = get_object_or_404(BlogPost, pk=blog_id)

    if request.method == 'POST':
        form = UpdateBlogPostForm(request.POST, instance=blog)
        # check if form is valid
        if form.is_valid():
            form.save()
            return redirect(reverse('blog',
                                    args=[blog.id]))
    # get form
    else:
        form = UpdateBlogPostForm(instance=blog)

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")  # python install 2019 = [python, install, 2019]
    for q in queries:
        posts = BlogPost.objects.filter(
                Q(title__icontains=q) |
                Q(body__icontains=q)
            ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))


def all_blog_posts(request):

    all_posts = BlogPost.objects.all()

    context = {
        'blog_posts': all_posts,
    }

    return render(request, "blog/blog.html", context)
