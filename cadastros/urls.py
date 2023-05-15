from django.urls import path

from .views import FazendaCreate, AnimalCreate, QualidadeLeiteCreate, HistoricoAnimalCreate
from .views import FazendaUpdate, AnimalUpdate, QualidadeLeiteUpdate, HistoricoAnimalUpdate
from .views import FazendaDelete, AnimalDelete, QualidadeLeiteDelete, HistoricoAnimalDelete
from .views import FazendaList, AnimalList, HistoricoanimalList, QualidadeLeiteList

urlpatterns = [
    path('cadastrar/fazenda/', FazendaCreate.as_view(), name='fazenda-create'),
    path('cadastrar/animal/', AnimalCreate.as_view(), name='animal-create'),
    path('cadastrar/qualidadeleite/', QualidadeLeiteCreate.as_view(), name='qualidadeleite-create'),
    path('cadastrar/historicoanimal/', HistoricoAnimalCreate.as_view(), name='historicoanimal-create'), 
     
    path('editar/fazenda/<int:pk>/', FazendaUpdate.as_view(), name='fazenda-update'),
    path('editar/animal/<int:pk>/', AnimalUpdate.as_view(), name='animal-update'),
    path('editar/qualidadeleite/<int:pk>/', QualidadeLeiteUpdate.as_view(), name='qualidadeleite-update'),
    path('editar/historicoanimal/<int:pk>/', HistoricoAnimalUpdate.as_view(), name='historicoanimal-update'), 
    
    path('deletar/fazenda/<int:pk>/', FazendaDelete.as_view(), name='fazenda-delete'),
    path('deletar/animal/<int:pk>/', AnimalDelete.as_view(), name='animal-delete'),
    path('deletar/qualidadeleite/<int:pk>/', QualidadeLeiteDelete.as_view(), name='qualidadeleite-delete'),
    path('deletar/historicoanimal/<int:pk>/', HistoricoAnimalDelete.as_view(), name='historicoanimal-delete'),
    
    path('listar/fazendas/', FazendaList.as_view(), name='fazenda-list'),
    path('listar/animais/', AnimalList.as_view(), name='animal-list'),
    path('listar/historicos/', HistoricoanimalList.as_view(), name='historicoanimal-list'),
    path('listar/qualidadeleites/', QualidadeLeiteList.as_view(), name='qualidadeleite-list'),
    
]
