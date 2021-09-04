from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views import View # 클래스형 view
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView # 제네릭 view
)
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.

# # (1) 함수형 view
# def index(request):
#     return redirect('post-list')

# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 6)
#     curr_page_number = request.GET.get('page')
#     if curr_page_number is None:
#         curr_page_number = 1
#     page = paginator.page(curr_page_number)
#     context = {'page': page}
#     return render(request, 'posts/post_list.html', context)

# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     context = {"post":post}
#     return render(request, 'posts/post_detail.html', context)

# def post_create(request):
#     if request.method =='POST':
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)
#     else:
#         post_form = PostForm()
#     return render(request, 'posts/post_form.html', {'form':post_form})

# def post_update(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post_form = PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post-detail', post_id=post.id)
#     else:
#         post_form = PostForm(instance=post)
#     return render(request, 'posts/post_form.html', {'form':post_form})

# def post_delete(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post-list')
#     else:
#         return render(request, 'posts/post_confirm_delete.html', {'post':post})

####################################################################################################

# # (2) 제네릭 view
# class IndexRedirectView(RedirectView):
#     pattern_name = 'post-list'

# class PostListView(ListView):
#     model = Post
#     template_name = 'posts/post_list.html'
#     context_object_name = 'posts'
#     ordering = ['-dt_created']
#     paginate_by = 6
#     page_kwarg = 'page'

# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'posts/post_detail.html'
#     pk_url_kwarg = 'post_id'
#     context_object_name = 'post'

# class PostCreateView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'posts/post_form.html'

#     def get_success_url(self):
#         return reverse('post-detail', kwargs={'post_id':self.object.id})

# class PostUpdateView(UpdateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'posts/post_form.html'
#     pk_url_kwarg = 'post_id'

#     def get_success_url(self):
#         return reverse('post-detail', kwargs={'post_id':self.object.id})

# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = 'posts/post_confirm_delete.html'
#     pk_url_kwarg = 'post_id'
#     context_object_name = 'post'

#     def get_success_url(self):
#         return reverse('post-list')

####################################################################################################

# (3) 제네릭 view (코드 간단히)
class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'

class PostListView(ListView):
    model = Post
    # template_name = 'posts/post_list.html' # 기본값
    # context_object_name = 'posts' # post_list.html > 22 line: page_obj.object_list -> object_list로 변경
    ordering = ['-dt_created']
    paginate_by = 6
    # page_kwarg = 'page'

class PostDetailView(DetailView):
    model = Post
    # template_name = 'posts/post_detail.html'
    # pk_url_kwarg = 'post_id' # 기본값은 'pk', 주석처리 후 urls.py에서 <int:pk>로 변경
    # context_object_name = 'post' # 기본값

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # template_name = 'posts/post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk':self.object.id}) # post_id를 pk로 변경

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    # template_name = 'posts/post_form.html'
    # pk_url_kwarg = 'post_id' # 기본값은 'pk', 주석처리 후 urls.py에서 <int:pk>로 변경

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk':self.object.id}) # post_id를 pk로 변경

class PostDeleteView(DeleteView):
    model = Post
    # template_name = 'posts/post_confirm_delete.html'
    # pk_url_kwarg = 'post_id' # 기본값은 'pk', 주석처리 후 urls.py에서 <int:pk>로 변경
    # context_object_name = 'post'

    def get_success_url(self):
        return reverse('post-list')

####################################################################################################

# # (4) 클래스형 view
# class PostCreateView(View):
#     def get(self, request):
#         post_form = PostForm()
#         return render(request, 'posts/post_form.html', {'form':post_form})

#     def post(self, request):
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)