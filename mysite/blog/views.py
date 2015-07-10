from blog.models import Post, Section
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission

def index(request):

	post_list = Post.objects.order_by('created_on')
	usr_list = User.objects.order_by('date_joined')
	blog_sect = Section.objects.all()
	content = {'post_list': post_list, 'usr_list': usr_list, 'blog_sect': blog_sect}
	return render(request, 'blog/index.html', content)

def displayPost(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	usr_list = User.objects.order_by('date_joined')
	blog_sect = Section.objects.all()
	content = {'post': post, 'usr_list': usr_list, 'blog_sect': blog_sect}
	return render(request, 'blog/post.html', content)

def display_author_posts_list(request, author):
    usr = User.objects.filter(username=author)
    usr_posts = Post.objects.filter(author=usr).order_by('created_on')
    content = {'usr_posts': usr_posts}
    return render(request, 'blog/usr_posts.html', content)

def display_section_post(request, section):
    sect = Section.objects.filter(section_name=section)
    posts = Post.objects.filter(section=sect)
    content = {'posts': posts}
    return render(request, 'blog/section_post.html', content)


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
                state = "You're successfully logged in as %s!" % username
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render(request, 'login.html', {'state':state, 'username': username})

def user_logout(request):
	logout(request)
	return render(request, 'login.html', {})
