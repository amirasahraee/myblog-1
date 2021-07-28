from django.urls import path
from .views import PostView, PostListView, ContactUsView, MetaView

urlpatterns = [

    path('posts', PostListView.as_view()),
    path('posts/<int:id>', PostView.as_view()),
    path('contactUs', ContactUsView.as_view()),
    path('siteInformation', MetaView.as_view())

]
