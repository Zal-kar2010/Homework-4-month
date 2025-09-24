from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog
from django.core.paginator import Paginator
from django.views import generic




#Search

class SearchView(generic.ListView):
  def get(self, request):
    query = request.GET.get('s', '')
    if query:
       blog_lst = Blog.objects.filter(title__icontains=query)
    else:
      blog_lst = Blog.objects.none
    context = {
    'blog_lst': blog_lst,
    's': query,
     }
    return render(request, template_name='blog.html', context=context)



# def search_view(request):
#   query = request.GET.get('s', '')
#   blog_lst = Blog.objects.filter(title__icontains=query) if query else Blog.objects.none
#   context = {
#     'blog_lst': blog_lst,
#     's': query,
#   }
#   return render(request, template_name='blog.html', context=context)





class BlogDetailView(generic.DetailView):
  template_name = 'blog_detail.html'
  context_object_name = 'blog_id'

  def get_object(self, *args, **kwargs):
    blog_id = self.kwargs.get('id')
    return get_object_or_404(Blog, id=blog_id)


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog_lst'
    ordering = ['-id']

    def get_queryset(self):
      return Blog.objects.all()


class FirstPageView(generic.View):
  def get(self, request):
    return HttpResponse('Привет это мой первый проект на Django!')

class TextPageView(generic.View):
  def get(self, request):
    return HttpResponse('Lorem Ipsum is simply ' \
    'dummy text of the printing and typesetting ' \
    'industry. Lorem Ipsum has been the industrys' \
    ' standard dummy text ever since the 1500s,' \
    ' when an unknown printer took a galley of ' \
    'type and scrambled it to make a type specimen book.' \
    ' It has survived not only five centuries, ' \
    'but also the leap into electronic typesetting, ' \
    'remaining essentially unchanged. It was popularised '
    'in the 1960s with the release of Letraset sheets ' \
    'containing Lorem Ipsum passages, and more recently' \
    ' with desktop publishing software like Aldus' \
    ' PageMaker including versions of Lorem Ipsum')

