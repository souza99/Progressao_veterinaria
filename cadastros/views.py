from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from .models import Fazenda, Animal, QualidadeLeite, HistoricoAnimal

from django.urls import reverse_lazy
# Create your views here.
class FazendaCreate(CreateView):
    model = Fazenda
    fields = ['nome', 'localizacao', 'cpfcnpj', 'numero']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class AnimalCreate(CreateView):
    model = Animal
    fields = ['nome', 'lote', 'nomePai', 'numeroPai', 'nomeMae', 'numeroMae', 'motivoBaixa', 'partosNaoLancados', 'dataNascimento', 'dataBaixa', 'fazenda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class QualidadeLeiteCreate(CreateView):
    model = QualidadeLeite
    fields = ['nt', 'dias', 'estado', 'kgLeite', 'porcentagemGordura', 'porcentagemProteinas', 'lactose', 'gp', 'ccs', 'ureia', 'cetose', 'pps', 'animal', 'diaRetirado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class HistoricoAnimalCreate(CreateView):
    model = HistoricoAnimal
    fields = ['animal' ,'observacoes' ,'medicamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
    
    
################### UPDATE ####################

class FazendaUpdate(UpdateView):
    model = Fazenda
    fields = ['nome', 'localizacao', 'cpfcnpj', 'numero']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['nome', 'lote', 'nomePai', 'numeroPai', 'nomeMae', 'numeroMae', 'motivoBaixa', 'partosNaoLancados', 'dataNascimento', 'dataBaixa', 'fazenda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class QualidadeLeiteUpdate(UpdateView):
    model = QualidadeLeite
    fields = ['nt', 'dias', 'estado', 'kgLeite', 'porcentagemGordura', 'porcentagemProteinas', 'lactose', 'gp', 'ccs', 'ureia', 'cetose', 'pps', 'animal', 'diaRetirado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class HistoricoAnimalUpdate(UpdateView):
    model = HistoricoAnimal
    fields = ['animal' ,'observacoes' ,'medicamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    


################### DELETE ####################

class FazendaDelete(DeleteView):
    model = Fazenda
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('index')
    
class AnimalDelete(DeleteView):
    model = Animal
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('index')
    
class QualidadeLeiteDelete(DeleteView):
    model = QualidadeLeite
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('index')
    
class HistoricoAnimalDelete(DeleteView):
    model = HistoricoAnimal
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('index')

class FazendaList(ListView):
    model = Fazenda
    template_name = 'cadastros/listas/fazenda.html'
    
