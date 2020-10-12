from django.urls import path

from . import views

app_name = 'my_new_app'
urlpatterns = [
    # ex: /my_new_app/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /my_new_app/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /my_new_app/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /my_new_app/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
