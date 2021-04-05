from django.urls import path
from .views import (BoardView,
                    ArticleDetailView,
                    AddPostView,
                    UpdatePostView,
                    DeletePostView,
                    AddCategoryView,
                    CategoryView,
                    AddCommentView)

app_name = 'community'

urlpatterns = [
                path('community-board', BoardView.as_view(), name='board'),
                path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
                path('add-post', AddPostView.as_view(), name='add-post'),
                path('add_category', AddCategoryView.as_view(), name='add_category'),
                path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
                path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
                path('category/<str:cats>/', CategoryView, name='category'),
                path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
]
