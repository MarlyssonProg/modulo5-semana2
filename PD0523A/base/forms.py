from django import forms
# De base = nome da app (pasta).models = arquivo models.py importando Contato(classe do arquivo models)
from base.models import Contato, Reserva

# Formulário contato

# Formulario automatizado, modelo a partir da class Contato em models.py


class ContatoForm(forms.ModelForm):
    class Meta:
        # Definindo o Modelo do formulário
        model = Contato

        # Definindo os campos do formulario (nome das variáveis  definidas no arquivo modelo.py)
        fields = ['nome', 'email', 'mensagem']

        # Modificador do designer dos inputs que irão ser visualizados na pagina de contato
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'placeholder': 'Informe seu nome'
                    # Posso adicionar mais atributos como: 'class': 'nome-classe-css'

                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Informe seu e-mail'
                    # Posso adicionar mais atributos como: 'class': 'nome-classe-css'
                }
            ),
            'mensagem': forms.Textarea(
                attrs={
                    'placeholder': 'Aqui sua mensagem'
                    # Posso adicionar mais atributos como: 'class': 'nome-classe-css'
                }
            )
        }

        # Definindo as labels dos inputs da página Contato
        labels = {
            'nome': 'Nome:',
            'email': 'E-mail:',
            'mensagem': 'Mensagem:',
        }


# Estrutura antes da automatização do formulário (CRIADO na MÃO)
# class ContatoForm(forms.Form):
# nome = forms.CharField()
# email = forms.EmailField(label="E-mail")
# mensagem = forms.CharField(widget=forms.Textarea)

# Classe reponsável pela a geração de um datepicker selecionável
# para a utilização do usuário no input 'data_reserva'
class DateInput(forms.DateInput):
    input_type = 'date'
# Formulário de reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        # Definindo modelo
        model = Reserva

        # Campos do formulário
        fields = ['nomePet', 'telefone', 'data_reserva', 'observacoes']

        widgets = {
            'nomePet': forms.TextInput(
                attrs={
                    'placeholder': 'Informe o nome de seu Pet'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'placeholder': 'Informe seu telefone'
                }
            ),
            'data_reserva': DateInput(),

            'observacoes': forms.Textarea(
                attrs={
                    'placeholder': 'Obeservações aqui!'
                }
            )

        }

        # Definindo as labels dos inputs da página Reserva
        labels = {
            'nomePet': 'NomePet:',
            'telefone': 'Telefone:',
            'data_reserva': 'Data da reserva:',
            'observacoes': 'Observações:',
        }


# Estrutura antes da automatização do formulário (CRIADO na MÃO)
# class ReservaForm(forms.Form):
# nome_pet = forms.CharField(label="Nome do Pet")
# telefone = forms.CharField()
# data_reserva = forms.DateField(label="Data da Reserva")
# observacoes = forms.CharField(widget=forms.Textarea, label="Observações")
