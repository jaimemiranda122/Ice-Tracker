from django.urls import path

from . import views
app_name = 'orders'
urlpatterns = [
	path('',views.index, name='index'),
        path('inputPage/',views.input,name='input'),
        path('<int:order_id>/',views.detail,name='detail'),
        path('<int:order_id>/results/',views.results,name='results'),
        path('<int:order_id>/vote/',views.vote,name='vote'),
]
