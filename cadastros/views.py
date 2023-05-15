from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from .models import Fazenda, Animal, QualidadeLeite, HistoricoAnimal

from django.urls import reverse_lazy
# Create your views here.
class FazendaCreate(CreateView):
    model = Fazenda
    fields = ['nome', 'localizacao', 'cpfcnpj', 'numero']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('fazenda-list')
    
class AnimalCreate(CreateView):
    model = Animal
    fields = ['nome', 'lote', 'nomePai', 'numeroPai', 'nomeMae', 'numeroMae', 'motivoBaixa', 'partosNaoLancados', 'dataNascimento', 'dataBaixa', 'fazenda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('animal-list')
    
class QualidadeLeiteCreate(CreateView):
    model = QualidadeLeite
    fields = ['nt', 'dias', 'estado', 'kgLeite', 'porcentagemGordura', 'porcentagemProteinas', 'lactose', 'gp', 'ccs', 'ureia', 'cetose', 'pps', 'animal', 'diaRetirado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('qualidadeleite-list')
    
class HistoricoAnimalCreate(CreateView):
    model = HistoricoAnimal
    fields = ['animal' ,'observacoes' ,'medicamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('historicoanimal-list')
    
    
    
################### UPDATE ####################

class FazendaUpdate(UpdateView):
    model = Fazenda
    fields = ['nome', 'localizacao', 'cpfcnpj', 'numero']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('fazenda-list')
    
class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['nome', 'lote', 'nomePai', 'numeroPai', 'nomeMae', 'numeroMae', 'motivoBaixa', 'partosNaoLancados', 'dataNascimento', 'dataBaixa', 'fazenda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('animal-list')
    
class QualidadeLeiteUpdate(UpdateView):
    model = QualidadeLeite
    fields = ['nt', 'dias', 'estado', 'kgLeite', 'porcentagemGordura', 'porcentagemProteinas', 'lactose', 'gp', 'ccs', 'ureia', 'cetose', 'pps', 'animal', 'diaRetirado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('qualidadeleite-list')
    
class HistoricoAnimalUpdate(UpdateView):
    model = HistoricoAnimal
    fields = ['animal' ,'observacoes' ,'medicamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('historicoanimal-list')
    


################### DELETE ####################

class FazendaDelete(DeleteView):
    model = Fazenda
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('fazenda-list')
    
class AnimalDelete(DeleteView):
    model = Animal
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('animal-list')
    
class QualidadeLeiteDelete(DeleteView):
    model = QualidadeLeite
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('qualidadeleite-list')
    
class HistoricoAnimalDelete(DeleteView):
    model = HistoricoAnimal
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('historicoanimal-list')

class FazendaList(ListView):
    model = Fazenda
    template_name = 'cadastros/listas/fazenda.html'
    
class AnimalList(ListView):
    model = Animal
    template_name = 'cadastros/listas/animal.html'
      
class HistoricoanimalList(ListView):
    model = HistoricoAnimal
    template_name = 'cadastros/listas/historicoanimal.html'
    
class QualidadeLeiteList(ListView):
    model = QualidadeLeite
    template_name = 'cadastros/listas/qualidadeleite.html'