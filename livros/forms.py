from django.forms import ModelForm
from .models import Meus_livros

class Meus_livros_form(ModelForm):
    class Meta:
        model = Meus_livros
        fields = '__all__'