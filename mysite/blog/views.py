from blog.models import Post, Section, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Count, Q

def index(request):

    latest_post = Post.objects.order_by('-created_on')[:3]
    post_list = Post.objects.order_by('-created_on')
    usr_list = User.objects.annotate(Count('post'))
    blog_sect = Section.objects.all()
    content = {'post_list': post_list, 'usr_list': usr_list, 'blog_sect': blog_sect, 'latest_post': latest_post}
    return render(request, 'blog/index.html', content)

def displayPost(request, post_id):

    latest_post = Post.objects.order_by('-created_on')[:3]
    post = get_object_or_404(Post, pk=post_id)
    usr_list = User.objects.annotate(Count('post'))
    blog_sect = Section.objects.all()
    post_comments = Comment.objects.filter(commented_on_post_id=post_id)
    content = {'post': post, 'usr_list': usr_list, 'blog_sect': blog_sect,
     'latest_post': latest_post, 'post_comments': post_comments}

    return render(request, 'blog/post.html', content)

def display_author_posts_list(request, author):

    latest_post = Post.objects.order_by('-created_on')[:3]
    usr_list = User.objects.annotate(Count('post'))
    usr = User.objects.filter(username=author)
    usr_posts = Post.objects.filter(author=usr).order_by('-created_on')
    blog_sect = Section.objects.all()
    content = {'usr_posts': usr_posts, 'latest_post': latest_post, 'blog_sect': blog_sect, 'usr_list': usr_list}

    return render(request, 'blog/usr_posts.html', content)

def display_section_post(request, section):

    latest_post = Post.objects.order_by('-created_on')[:3]
    usr_list = User.objects.annotate(Count('post'))
    blog_sect = Section.objects.all()

    sect = Section.objects.filter(section_name=section)
    posts = Post.objects.filter(section=sect)
    
    content = {'posts': posts, 'usr_list': usr_list, 'blog_sect': blog_sect, 'latest_post': latest_post}
    return render(request, 'blog/section_post.html', content)

def search(request):

    if(request.POST):

    	search_term = request.POST['search']

        search_result = Post.objects.filter(Q(title__contains=search_term) | Q(body__contains=search_term) |
            Q(post_tags__contains=search_term))

        content = {'search_result': search_result}

        return render(request, 'blog/search.html', content)


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('blog.views.index')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render(request, 'login.html', {'state':state, 'username': username})

def user_logout(request):
	logout(request)
	return render(request, 'login.html', {})
