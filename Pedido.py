from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

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
        
        self.submit_button = Button(text='Adicionar Pedido')
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