from django.contrib import admin
from .models import Fazenda, Animal, QualidadeLeite
# Register your models here.
admin.site.register(Fazenda)
admin.site.register(Animal)
admin.site.register(QualidadeLeite)