from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class HamburguerForm(BoxLayout):
    def __init__(self, **kwargs):
        super(HamburguerForm, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.nome_hamburguer = ''
        self.ingredientes = ''


        self.add_widget(Label(text='Nome do Hambúrguer:'))
        self.nome_hamburguer_input = TextInput(text=self.nome_hamburguer)
        self.nome_hamburguer_input.bind(on_text=self.on_nome_hamburguer_text)
        self.add_widget(self.nome_hamburguer_input)

        self.add_widget(Label(text='Ingredientes:'))
        self.ingredientes_input = TextInput(text=self.ingredientes)
        self.ingredientes_input.bind(on_text=self.on_ingredientes_text)
        self.add_widget(self.ingredientes_input)

        self.registar_button = Button(text='Adicionar hamburguer')
        self.registar_button.bind(on_press=self.submit_hamburguer)
        self.add_widget(self.registar_button)

    def on_id_cliente_text(self, instance, value):
        self.id_cliente = value

    def on_nome_hamburguer_text(self, instance, value):
        self.nome_hamburguer = value

    def on_quantidade_text(self, instance, value):
        self.quantidade = int(value) if value.isdigit() else 1

    def on_tamanho_text(self, instance, value):
        self.tamanho = value

    def on_valor_total_text(self, instance, value):
        self.valor_total = float(value) if value.replace('.', '', 1).isdigit() else 0.0

    def submit_pedido(self, instance):
        self.database.add_pedido(self.id_cliente, self.nome_hamburguer, self.quantidade, self.tamanho, self.valor_total)
        print(f"Pedido Registrado: Cliente ID: {self.id_cliente}, Hambúrguer: {self.nome_hamburguer}, Quantidade: {self.quantidade}, Tamanho: {self.tamanho}, Valor Total: {self.valor_total}")