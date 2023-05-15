from django.views.generic.edit import CreateView

from .models import Fazenda, Animal, QualidadeLeite

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
    
