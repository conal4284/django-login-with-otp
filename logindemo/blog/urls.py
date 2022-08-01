from django.urls import path
from blog.models import Blog
from blog.views import BlogCreate, BlogUpdate, BlogList

urlpatterns = [
    path('add/', BlogCreate.as_view(), name='add_blog'),
    path('<pk>/update/', BlogUpdate.as_view(), name='update_blog'),
    path('list/', BlogList.as_view(), name='list_blogs'),
]