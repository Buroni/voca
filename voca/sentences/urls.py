from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import index, SentenceDetailView, SentenceFormsView, SentenceReportView, UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet)

app_name = "sentences"

urlpatterns = [
    path('', index, name='index'),
    path('auth/', include(router.urls)),
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='create-user'),
    path('report/', SentenceReportView.as_view(), name='report'),
    path('<str:language>/<str:word>/', SentenceFormsView.as_view(), name='sentence-list'),
    path('<str:pk>/', SentenceDetailView.as_view(), name='sentence-detail'),
]
