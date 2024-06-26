from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.app import App
import requests

class PedidoForm(BoxLayout):
    def __init__(self, **kwargs):
        super(PedidoForm, self).__init__(**kwargs)
        self.database = None
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.id_cliente = ''
        self.nome_hamburguer = ''
        self.quantidade = 1
        self.tamanho = 'normal'
        self.valor_total = 0.0
        
        self.add_widget(Label(text='ID do Cliente'))
        self.id_cliente_input = TextInput()
        self.id_cliente_input.bind(text=self.on_id_cliente_text)
        self.add_widget(self.id_cliente_input)
        
        self.add_widget(Label(text='Nome do Hambúrguer'))
        self.nome_hamburguer_input = TextInput()
        self.nome_hamburguer_input.bind(text=self.on_nome_hamburguer_text)
        self.add_widget(self.nome_hamburguer_input)
        
        self.add_widget(Label(text='Quantidade'))
        self.quantidade_input = TextInput(input_filter='int')
        self.quantidade_input.bind(text=self.on_quantidade_text)
        self.add_widget(self.quantidade_input)
        
        self.add_widget(Label(text='Tamanho:'))
        self.tamanho_spinner = Spinner(text='normal', values=['infantil', 'normal', 'duplo'])
        self.tamanho_spinner.bind(text=self.on_tamanho_text)
        self.add_widget(self.tamanho_spinner)
        
        self.add_widget(Label(text='Valor Total'))
        self.valor_total_input = TextInput(input_filter='float')
        self.valor_total_input.bind(text=self.on_valor_total_text)
        self.add_widget(self.valor_total_input)
        
        self.registar_button = Button(text='Adicionar Pedido')
        self.registar_button.bind(on_press=self.submit_pedido)
        self.add_widget(self.registar_button)
        
    def set_database(self, database):
        self.database = database
        
    def on_id_cliente_text(self, _, value):
        self.id_cliente = value

    def on_nome_hamburguer_text(self, _, value):
        self.nome_hamburguer = value

    def on_quantidade_text(self, _, value):
        self.quantidade = int(value) if value.isdigit() else 1

    def on_tamanho_text(self, _, value):
        self.tamanho = value

    def on_valor_total_text(self, _, value):
        self.valor_total = float(value) if value.replace('.', '', 1).isdigit() else 0.0

    def submit_pedido(self, _):
        data = {
            'id_cliente': int(self.id_cliente),
            'nome_hamburguer': self.nome_hamburguer,
            'quantidade': self.quantidade,
            'tamanho': self.tamanho,
            'valor_total': self.valor_total
        }
        response = requests.post('http://127.0.0.1:5000/pedidos', json=data)
        if response.status_code == 201:
            print(f"Pedido Adicionado: Cliente ID: {self.id_cliente}, Hambúrguer: {self.nome_hamburguer}, Quantidade: {self.quantidade}, Tamanho: {self.tamanho}, Valor Total: {self.valor_total}")
        else:
            print("Erro ao adicionar pedido!")
            # Exibir mensagem de erro para o utilizador
            

class PedidoApp(App):
    def build(self):
        return PedidoForm()
    
if __name__ == '__main__':
    PedidoApp().run()