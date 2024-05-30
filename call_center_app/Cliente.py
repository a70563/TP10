from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ClienteForm(BoxLayout):
    def __init__(self, **kwargs):
        super(ClienteForm, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.nome = ''
        self.morada = ''
        self.telefone = ''
        
        self.add_widget(Label(text='Nome Cliente:'))
        self.nome_input = TextInput(text=self.nome)
        self.nome_input.bind(on_text=self.on_nome_text)
        self.add_widget(self.nome_input)

        self.add_widget(Label(text='Morada:'))
        self.morada_input = TextInput(text=self.morada)
        self.morada_input.bind(on_text=self.on_morada_text)
        self.add_widget(self.morada_input)

        self.add_widget(Label(text='Telefone:'))
        self.telefone_input = TextInput(text=self.telefone)
        self.telefone_input.bind(on_text=self.on_telefone_text)
        self.add_widget(self.telefone_input)

        self.registrar_button = Button(text='Adicionar Cliente')
        self.registrar_button.bind(on_press=self.submit_cliente)
        self.add_widget(self.registrar_button)



    def on_nome_hamburguer_text(self, instance, value):
        self.nome_hamburguer = value

    def on_quantidade_text(self, instance, value):
        self.quantidade = int(value) if value.isdigit() else 1

    def on_tamanho_text(self, instance, value):
        self.tamanho = value

    def on_valor_total_text(self, instance, value):
        self.valor_total = float(value) if value.replace('.', '', 1).isdigit() else 0.0

    def submit_pedido(self, instance):
        print(f"Pedido Registrado: Hambúrguer: {self.nome_hamburguer}, Quantidade: {self.quantidade}, Tamanho: {self.tamanho}, Valor Total: {self.valor_total}")