from django.db import models


# Tabela e Modelo para armazenar os dados da página de contato no BD
class Contato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    mensagem = models.CharField(max_length=3000)
    data = models.DateField(auto_now_add=True)
    # Insere a funcionalidade do admin verificar se a menssagem foi lida
    # blank -> pode ser um campo em branco e null -> um campo nulo
    lido = models.BooleanField(default=False, blank=True, null=True)

# Configuração Django para organização dos objetos(Dados)
# Mostra o objeto.nome para ficar visível qual nome do cadastro
    def __str__(self):
        return self.nome

# Tabela e Modelo para armazenar os dados da página de reserva no BD


class Reserva(models.Model):
    nomePet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    data_reserva = models.DateField()
    observacoes = models.CharField(max_length=3000)
