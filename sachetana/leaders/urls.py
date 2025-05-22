from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'leaders', views.LeaderViewSet)
router.register(r'promises', views.PromiseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('leaders/<int:pk>/', views.LeaderDetailView.as_view(), name='leader-detail'), 
]