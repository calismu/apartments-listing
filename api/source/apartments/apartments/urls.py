from django.urls import path, include


# root url pattern '/app' preceeding all paths

urlpatterns = [
    path('app/', include('api.urls'), name='app'),
]
