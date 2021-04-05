from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy


class BoardView(ListView):
    model                   = Post
    template_name           = 'board/board.html'
    ordering                = ['-post_created']
    paginate_by             = 5

    def get_context_data(self, *args, **kwargs):
        cat_menu            = Category.objects.all()
        context             = super(BoardView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts          = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'board/categories.html', {'cats':cats.replace('-', ' '), 'category_posts':category_posts})


class ArticleDetailView(DetailView):
    model                   = Post
    template_name           = 'board/article_details.html'
    paginate_by             = 2

    def get_context_data(self, *args, **kwargs):
        cat_menu            = Category.objects.all()
        context             = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddPostView(CreateView):
    model                   = Post
    form_class              = PostForm
    template_name           = 'board/add_posts.html'

class AddCategoryView(CreateView):
    model                   = Category
    template_name           = 'board/add_category.html'
    fields                  = '__all__'

class UpdatePostView(UpdateView):
    model                   = Post
    form_class              = EditForm
    template_name           = 'board/update_post.html'


class DeletePostView(DeleteView):
    model                   = Post
    template_name           = 'board/delete_post.html'
    success_url             = reverse_lazy('community:board')


class AddCommentView(CreateView):
    model                   = Comment
    form_class              = CommentForm
    template_name           = 'board/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('community:article-detail', kwargs={'pk': self.kwargs['pk']})