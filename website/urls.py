from django.urls import path # importamos la función path de django para mapear las urls a las vistas de la aplicación
from website.views import HomePageView # importamos la vista creada en el archivo views.py de la aplicación

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'), # indicamos que la url raíz se mapea a la vista HomePageView
]