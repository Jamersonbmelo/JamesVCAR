from django.forms import ModelForm
from .models import Carro, Cliente, Aluguel
from django.contrib.auth.forms import UserCreationForm

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = '__all__'

class AluguelForm(ModelForm):
    
    class Meta:
        model = Aluguel
        fields = '__all__'
        
class MyUserCreationForm(UserCreationForm):
    pass
