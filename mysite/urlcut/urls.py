from django.urls import path
from .views import Homepage, ShortenerCreateApiView, ShortenerListAPIView, Redirector
from .views import RemoveUnusedLinksZeroCount, RemoveUnusedLinksInMinute, RemoveUnusedLinksDayly, RemoveAll
from .views import RemoveUsedLinksInMinute, RemoveUsedLinksDayly

urlpatterns = [
    path('', Homepage, name='create_api'),
    path('link_generator/', ShortenerCreateApiView.as_view(), name='link_generator'),

    path('list/',ShortenerListAPIView.as_view(), name='link_list/'),
    path('remove_unused/zerocount', RemoveUnusedLinksZeroCount, name='remove_zerocount'),
    path('remove_unused/minute', RemoveUnusedLinksInMinute, name='remove_minute'),
    path('remove_unused/day', RemoveUnusedLinksDayly, name='remove_day'),
    path('remove_used/minute', RemoveUsedLinksInMinute, name='remove_minute'),
    path('remove_used/day', RemoveUsedLinksDayly, name='remove_day'),
    path('remove_unused/all', RemoveAll, name='remove_all'),
    
    path('<str:shortener_link>/', Redirector.as_view(), name='redirector'),
]
