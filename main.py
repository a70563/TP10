from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class ClienteForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.add_widget(Label(text='Nome:'))
        self.nome = TextInput(multiline=False)
        self.add_widget(self.nome)

        self.add_widget(Label(text='Morada:'))
        self.morada = TextInput(multiline=False)
        self.add_widget(self.morada)

        self.add_widget(Label(text='Telefone:'))
        self.telefone = TextInput(multiline=False)
        self.add_widget(self.telefone)

        self.submit_button = Button(text='Adicionar Cliente')
        self.submit_button.bind(on_press=self.add_cliente)
        self.add_widget(self.submit_button)

        self.result_label = Label(text='')
        self.add_widget(self.result_label)
        

    def add_cliente(self):
        url = 'http://127.0.0.1:5000/clientes'
        cliente_data = {
            'nome': self.nome.text,
            'morada': self.morada.text,
            'telefone': self.telefone.text
        }
        response = requests.post(url, json=cliente_data)
        if response.status_code == 201:
            self.result_label.text = 'Cliente adicionado com sucesso!'
        else:
            self.result_label.text = 'Erro ao adicionar cliente!'
            
            
class HamburguerForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text='Nome do Hambúrguer:'))
        self.nome_hamburguer = TextInput(multiline=False)
        self.add_widget(self.nome_hamburguer)

        self.add_widget(Label(text='Ingredientes:'))
        self.ingredientes = TextInput(multiline=False)
        self.add_widget(self.ingredientes)

        self.submit_button = Button(text='Adicionar Hambúrguer')
        self.submit_button.bind(on_press=self.add_hamburguer)
        self.add_widget(self.submit_button)

        self.result_label = Label(text='')
        self.add_widget(self.result_label)

    def add_hamburguer(self):
        url = 'http://127.0.0.1:5000/hamburgueres'
        hamburguer_data = {
            'nome_hamburguer': self.nome_hamburguer.text,
            'ingredientes': self.ingredientes.text
        }
        response = requests.post(url, json=hamburguer_data)
        if response.status_code == 201:
            self.result_label.text = 'Hambúrguer adicionado com sucesso!'
        else:
            self.result_label.text = 'Erro ao adicionar hambúrguer!'



class PedidoForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.add_widget(Label(text='ID do Cliente'))
        self.id_cliente = TextInput(multiline=False)
        self.add_widget(self.id_cliente)
        
        self.add_widget(Label(text='Nome do Hambúrguer'))
        self.nome_hamburguer = TextInput(multiline=False)
        self.add_widget(self.nome_hamburguer)
        
        self.add_widget(Label(text='Quantidade'))
        self.quantidade = TextInput(multiline=False)
        self.add_widget(self.quantidade)
        
        self.add_widget(Label(text='Tamanho (infantil, normal, duplo)'))
        self.tamanho_layout = BoxLayout(orientation='horizontal')
        self.tamanho_infantil = CheckBox(group='tamanho')
        self.tamanho_normal = CheckBox(group='tamanho')
        self.tamanho_duplo = CheckBox(group='tamanho')
        
        self.tamanho_layout.add_widget(Label(text='Infantil')) 
        self.tamanho_layout.add_widget(self.tamanho_infantil) 
        self.tamanho_layout.add_widget(Label(text='Normal'))
        self.tamanho_layout.add_widget(self.tamanho_normal)
        self.tamanho_layout.add_widget(Label(text='Duplo'))
        self.tamanho_layout.add_widget(self.tamanho_duplo)
        self.add_widget(self.tamanho_layout)
        
        
        self.add_widget(Label(text='Valor Total'))
        self.valor_total = TextInput(multiline=False)
        self.add_widget(self.valor_total)
        
        self.submit_button = Button(text='Registrar Pedido')
        self.submit_button.bind(on_press=self.add_pedido)
        self.add_widget(self.submit_button)
        
        self.result_label = Label(text='')
        self.add_widget(self.result_label)

def get_tamanho(self):
        if self.tamanho_infantil.active:
            return 'infantil'
        elif self.tamanho_normal.active:
            return 'normal'
        elif self.tamanho_duplo.active:
            return 'duplo'
        return ''
        

def add_pedido(self):
        url = 'http://127.0.0.1:5000/pedidos'
        pedido_data = {
            'id_cliente': self.id_cliente.text,
            'nome_hamburguer': self.nome_hamburguer.text,
            'quantidade': self.quantidade.text,
            'tamanho': self.get_tamanho(),
            'valor_total': self.valor_total.text
        }
        response = requests.post(url, json=pedido_data)
        if response.status_code == 201:
            self.result_label.text = 'Pedido adicionado com sucesso!'
        else:
            self.result_label.text = 'Erro ao adicionar pedido!'


        
class CallCenterApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        
        self.cliente_form = ClienteForm()
        root.add_widget(self.cliente_form)
        
        self.hamburguer_form = HamburguerForm()
        root.add_widget(self.hamburguer_form)
        
        self.pedido_form = PedidoForm()
        root.add_widget(self.pedido_form)
        
        return root


if __name__ == '__main__':
    CallCenterApp().run()
