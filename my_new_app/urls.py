from django.urls import path

from . import views

app_name = 'my_new_app'
urlpatterns = [
    # ex: /my_new_app/
    path('', views.index, name='index'),
    # ex: /my_new_app/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /my_new_app/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /my_new_app/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
