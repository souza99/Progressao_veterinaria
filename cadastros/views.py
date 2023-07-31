from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from .models import Fazenda, Animal, QualidadeLeite, HistoricoAnimal, Cio, GanhoPeso

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
# Create your views here.
class FazendaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Fazenda
    fields = ['nome', 'localizacao', 'cpfcnpj', 'numero']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('fazenda-list')
    
    def form_valid(self, form):
        
        #Antes do super não foi criado o objeto e nem salvou no banco
        form.instance.usuario = self.request.user
        
        url = super().form_valid(form)
        
        return url
    
class AnimalCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Animal
    fields = ['nome', 'lote', 'nomePai', 'numeroPai', 'nomeMae', 'numeroMae', 'motivoBaixa', 'partosNaoLancados', 'dataNascimento', 'dataBaixa', 'fazenda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('animal-list')
    
    def form_valid(self, form):
        
        #Antes do super não foi criado o objeto e nem salvou no banco
        form.instance.usuario = self.request.user
        
        url = super().form_valid(form)
        
        return url
    
class QualidadeLeiteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = QualidadeLeite
    fields = ['nt', 'dias', 'estado', 'kgLeite', 'porcentagemGordura', 'porcentagemProteinas', 'lactose', 'gp', 'ccs', 'ureia', 'cetose', 'pps', 'animal', 'diaRetirado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('qualidadeleite-list')
    
class HistoricoAnimalCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = HistoricoAnimal
    fields = ['animal' ,'observacoes' ,'medicamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('historicoanimal-list')
    
class CioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cio
    fields = ['animal', 'diasServ', 'ultimaServ']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cio-list')
    
class GanhoPesoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = GanhoPeso
    fields = ['animal','dia', 'pesoDia', 'quantidadeRacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('ganhopeso-list')
    
################### UPDATE ####################

class FazendaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Fazenda
    fields = ['nome', 'localizacao', 'cpfcnpj', 'numero']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('fazenda-list')
    
class AnimalUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Animal
    fields = ['nome', 'lote', 'nomePai', 'numeroPai', 'nomeMae', 'numeroMae', 'motivoBaixa', 'partosNaoLancados', 'dataNascimento', 'dataBaixa', 'fazenda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('animal-list')
    
class QualidadeLeiteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = QualidadeLeite
    fields = ['nt', 'dias', 'estado', 'kgLeite', 'porcentagemGordura', 'porcentagemProteinas', 'lactose', 'gp', 'ccs', 'ureia', 'cetose', 'pps', 'animal', 'diaRetirado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('qualidadeleite-list')
    
class HistoricoAnimalUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = HistoricoAnimal
    fields = ['animal' ,'observacoes' ,'medicamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('historicoanimal-list')

class CioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cio
    fields = ['animal', 'diasServ', 'ultimaServ']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cio-list')
    
class GanhoPesoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = GanhoPeso
    fields = ['animal','dia', 'pesoDia', 'quantidadeRacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('ganhopeso-list')
    


################### DELETE ####################

class FazendaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Fazenda
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('fazenda-list')
    
class AnimalDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Animal
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('animal-list')
    
class QualidadeLeiteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = QualidadeLeite
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('qualidadeleite-list')
    
class HistoricoAnimalDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = HistoricoAnimal
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('historicoanimal-list')
    
    
class CioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cio
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('cio-list')
    
class GanhoPesoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = GanhoPeso
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('ganhopeso-list')
    
################### LIST ####################

class FazendaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Fazenda
    template_name = 'cadastros/listas/fazenda.html'
    
class AnimalList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Animal
    template_name = 'cadastros/listas/animal.html'
      
class HistoricoanimalList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = HistoricoAnimal
    template_name = 'cadastros/listas/historicoanimal.html'
    
class QualidadeLeiteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = QualidadeLeite
    template_name = 'cadastros/listas/qualidadeleite.html'
    
class CiosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Cio
    template_name = 'cadastros/listas/cio.html'
    
class GanhoPesosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = GanhoPeso
    template_name = 'cadastros/listas/ganhopeso.html'