from typing import Any
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from .models import Fazenda, Animal, QualidadeLeite, HistoricoAnimal, Cio, GanhoPeso

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.
class FazendaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Fazenda
    fields = ['nome', 'localizacao', 'cpfcnpj', 'numero']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('fazenda-list')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Fazendas"
        context['botao'] = "Concluir"
        
        return context
    
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
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Animais"
        context['botao'] = "Concluir"
        
        
        return context
    
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
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Qualidade"
        context['botao'] = "Concluir"
        
        return context
    
class HistoricoAnimalCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = HistoricoAnimal
    fields = ['animal' ,'observacoes' ,'medicamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('historicoanimal-list')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Historico"
        context['botao'] = "Concluir"
        
        return context
    
class CioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cio
    fields = ['animal', 'diasServ', 'ultimaServ']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cio-list')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Cios"
        context['botao'] = "Concluir"
        
        return context
    
class GanhoPesoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = GanhoPeso
    fields = ['animal','dia', 'pesoDia', 'quantidadeRacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('ganhopeso-list')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Peso"
        context['botao'] = "Concluir"
        
        return context
    
################### UPDATE ####################

class FazendaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Fazenda
    fields = ['nome', 'localizacao', 'cpfcnpj', 'numero']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('fazenda-list')
    success_message = "Fazenda cadastrada com sucesso!"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Edição da Fazenda"
        context['botao'] = "Concluir"
        
        return context
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Fazenda, pk=self.kwargs['pk'], usuario=self.request.user)
        
        return self.object
    
class AnimalUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Animal
    fields = ['nome', 'lote', 'nomePai', 'numeroPai', 'nomeMae', 'numeroMae', 'motivoBaixa', 'partosNaoLancados', 'dataNascimento', 'dataBaixa', 'fazenda']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('animal-list')
    success_message = "Animal cadastrado com sucesso!"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Edição do Animal"
        context['botao'] = "Concluir"
        
        return context
    
    def get_object(self, queryset=None):
        self.object = self.object = get_object_or_404(Animal, pk=self.kwargs['pk'], usuario=self.request.user)
        
        return self.object
    
class QualidadeLeiteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = QualidadeLeite
    fields = ['nt', 'dias', 'estado', 'kgLeite', 'porcentagemGordura', 'porcentagemProteinas', 'lactose', 'gp', 'ccs', 'ureia', 'cetose', 'pps', 'animal', 'diaRetirado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('qualidadeleite-list')
    success_message="Qualidade cadastrada com sucesso"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Edição do Leite"
        context['botao'] = "Concluir"
        
        return context
    
class HistoricoAnimalUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = HistoricoAnimal
    fields = ['animal' ,'observacoes' ,'medicamento']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('historicoanimal-list')
    success_message = "Histórico salvo com sucesso"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Edição do Istórico"
        context['botao'] = "Concluir"
        
        return context

class CioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cio
    fields = ['animal', 'diasServ', 'ultimaServ']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cio-list')
    success_message="Cia cadastrado com sucesso!"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Edição do Cio"
        context['botao'] = "Concluir"
        
        return context
    
class GanhoPesoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = GanhoPeso
    fields = ['animal','dia', 'pesoDia', 'quantidadeRacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('ganhopeso-list')
    success_message="Pesagem cadastrada com sucesso!"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Edição do Peso"
        context['botao'] = "Concluir"
        
        return context
    


################### DELETE ####################

class FazendaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Fazenda
    template_name = 'cadastros/form-delete.html'
    success_url = reverse_lazy('fazenda-list')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Fazenda, pk=self.kwargs['pk'], usuario=self.request.user)
        
        return self.object
    
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
    
    def get_queryset(self):
        self.object_list = Fazenda.objects.filter(usuario=self.request.user)
        return self.object_list
    
    
class AnimalList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Animal
    template_name = 'cadastros/listas/animal.html'
    
    def get_queryset(self):
        self.object_list = Animal.objects.filter(usuario=self.request.user)
        return self.object_list
      
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