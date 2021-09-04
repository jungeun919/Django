from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView
)
from django.urls import reverse
from .models import Page
from .forms import PageForm

# Create your views here.

# # (1) 함수형 view
# def index(request):
#     return render(request, 'diary/index.html')

# def page_list(request):
#     object_list = Page.objects.all()
#     paginator = Paginator(object_list, 8)
#     curr_page_number = request.GET.get('page')
#     if curr_page_number is None:
#         curr_page_number = 1
#     page = paginator.page(curr_page_number)
#     return render(request, 'diary/page_list.html', {'page':page})

# def info(request):
#     return render(request, 'diary/info.html')

# def page_create(request):
#     if request.method == 'POST':
#         form = PageForm(request.POST)
#         if form.is_valid():
#             new_page = form.save()
#             return redirect('page-detail', page_id=new_page.id)
#     else:
#         form = PageForm()
#     return render(request, 'diary/page_form.html', {'form':form})

# def page_detail(request, page_id):
#     object = Page.objects.get(id=page_id)
#     return render(request, 'diary/page_detail.html', {'object':object})

# def page_update(request, page_id):
#     object = Page.objects.get(id=page_id)
#     if request.method == 'POST':
#         form = PageForm(request.POST, instance=object)
#         if form.is_valid():
#             form.save()
#             return redirect('page-detail', page_id=object.id)
#     else:
#         form = PageForm(instance=object)
#     return render(request, 'diary/page_form.html', {'form':form})

# def page_delete(request, page_id):
#     object = Page.objects.get(id=page_id)
#     if request.method == 'POST':
#         object.delete()
#         return redirect('page-list')
#     else:
#         return render(request, 'diary/page_confirm_delete.html', {'object':object})

####################################################################################################

# # (2) 제네릭 view
# def index(request):
#     return render(request, 'diary/index.html')

# class PageListView(ListView):
#     model = Page
#     template_name = 'diary/page_list.html'
#     ordering = ['-dt_created']
#     paginate_by = 8
#     page_kwarg = 'page'

# def info(request):
#     return render(request, 'diary/info.html')

# class PageCreateView(CreateView):
#     model = Page
#     form_class = PageForm
#     template_name = 'diary/page_form.html'

#     def get_success_url(self):
#         return reverse('page-detail', kwargs={'page_id':self.object.id})

# class PageDetailView(DetailView):
#     model = Page
#     template_name = 'diary/page_detail.html'
#     pk_url_kwarg = 'page_id'

# class PageUpdateView(UpdateView):
#     model = Page
#     form_class = PageForm
#     template_name = 'diary/page_form.html'
#     pk_url_kwarg = 'page_id'

#     def get_success_url(self):
#         return reverse('page-detail', kwargs={'page_id':self.object.id})

# class PageDeleteView(DeleteView):
#     model = Page
#     template_name = 'diary/page_confirm_delete.html'
#     pk_url_kwarg = 'page_id'

#     def get_success_url(self):
#         return reverse('page-list')

####################################################################################################

# (3) 제네릭 view (코드 간단히)
def index(request):
    return render(request, 'diary/index.html')

class PageListView(ListView):
    model = Page
    ordering = ['-dt_created']
    paginate_by = 8

def info(request):
    return render(request, 'diary/info.html')

class PageCreateView(CreateView):
    model = Page
    form_class = PageForm

    def get_success_url(self):
        return reverse('page-detail', kwargs={'pk':self.object.id})

class PageDetailView(DetailView):
    model = Page

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm

    def get_success_url(self):
        return reverse('page-detail', kwargs={'pk':self.object.id})

class PageDeleteView(DeleteView):
    model = Page

    def get_success_url(self):
        return reverse('page-list')