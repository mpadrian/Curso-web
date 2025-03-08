from django.urls import path # importamos la función path de django para mapear las urls a las vistas de la aplicación
from website.views import HomePageView, AboutPageView # importamos la vista creada en el archivo views.py de la aplicación

urlpatterns = [
    path('', HomePageView.as_view(), name = 'main'), # indicamos que la url raíz se mapea a la vista HomePageView
    path('about/', AboutPageView.as_view(), name = 'about'), # indicamos que la url /about se mapea a la vista AboutPageView
]