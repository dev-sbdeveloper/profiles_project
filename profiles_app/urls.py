from django.urls import path, include
from profiles_app import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
router.register("profiles", views.UserProfileViewSet)
router.register("feed", views.PostFeedViewSet)

urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),
    path("login/", views.UserLoginApiView.as_view()),
    path("", include(router.urls)),
]
