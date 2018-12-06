from django.urls import path

from . import views


urlpatterns = [
    path('<username>/', views.getUser, name='getUser'),
    path('<username>/<twitter>/<insta>/create/', views.createUser, name='createUser'),
    path('<username>/delete/', views.deleteUser, name='deleteUser'),
    path('<username>/<twitter>/<insta>/update/', views.updateUser, name='updateUser'),
    path('<username>/<text>/selfPost/create/selfPost/', views.createSelfPost, name='createSelfPost'),
    path('<idx>/<text>/selfPost/update/selfPost/', views.updateSelfPost, name='updateSelfPost'),
    path('<idx>/selfPost/delete/selfPost/', views.deleteSelfPost, name='deleteSelfPost'),
    path('<username>/posts/', views.getPosts, name='getPosts'),
    path('<username>/twitter/', views.getTwiiter, name='getTwitter'),
    path('<username>/instagram/', views.getInstagram, name='getInstagram'),
    path('search/<username>/<text>/', views.searchText, name='search'),

]