from django.views.generic import TemplateView

# Create your views here.

# class IndexView(TemplateView):
#     template_name = "index.html"
    
class PaginaInicial(TemplateView):
     template_name = "paginas/modelo.html"