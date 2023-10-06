# Registro de modelos             # Adicionado esse import messages para passar o retorno de uma função
from django.contrib import admin, messages
# Importação da pasta base do modelo Contato do arquivo models.py
from base.models import Contato

# Utilizar esse decorador a função é colocada na action pelo próprio Django
@admin.action(description='Marcar como lido')
# Definição de uma função de action com 3 parametros
# O 1º parâmetro é Gerenciador do modelo  Admin do Django
# O 2º parâmetro é solicitação de status do objeto
# O 3º parâmetro é o responsável por alterar o valor do campo do model
def marcar_como_lido(modeladmin, request, queryset):

    # Atualiza o campo do models.py para true
    queryset.update(lido=True)

    # mensagem para usuário que o campo foi atualizado
    modeladmin.message_user(resquest, "Marcado como lido!", messages.SUCCESS)

# Registro do modelo Contato


@admin.register(Contato)
# Administrador do Django para modelo Contato
# ContatoAdmin = Administrador do Django para o modelo contato
# Dentro do parentses é uma herança de uma classe Contato que está dentro do arquivo admin.py
class ContatoAdmin(admin.ModelAdmin):

    # Adcionarmos uma lista para visulaização das demais informações dos cadastros no admin Django
    list_display = ['nome', 'email', 'data', 'lido']

    # Adcionarmos uma lista para filtrar cadastros no admin Django por data
    list_filter = ['data', 'lido']

    # Campos de buscas
    search_fields = ['nome', 'email']
    actions = [marcar_como_lido]
