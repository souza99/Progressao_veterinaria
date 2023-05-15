from django.urls import path

from .views import FazendaCreate, AnimalCreate, QualidadeLeiteCreate

urlpatterns = [
    path('cadastrar/fazenda/', FazendaCreate.as_view(), name='fazenda_create'),
    path('cadastrar/animal/', AnimalCreate.as_view(), name='animal_create'),
    path('cadastrar/qualidadeleite/', QualidadeLeiteCreate.as_view(), name='qualidadeleite_create'),       
]
