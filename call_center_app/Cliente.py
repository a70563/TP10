from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests


class ClienteForm(BoxLayout):
    def __init__(self, **kwargs):
        super(ClienteForm, self).__init__(**kwargs)
        self.database = None
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

        self.registar_button = Button(text='Adicionar Cliente')
        self.registar_button.bind(on_press=self.submit_cliente)
        self.add_widget(self.registar_button)


    def set_database(self, database):
        self.database = database
        
    def on_nome_text(self, instance, value):
        self.nome = value

    def on_morada_text(self, instance, value):
        self.morada = value

    def on_telefone_text(self, instance, value):
        self.telefone = value

    def submit_cliente(self, instance):
        data = {
        'nome': self.nome,
        'morada': self.morada,
        'telefone': self.telefone
        }
        response = requests.post('http://127.0.0.1:5000/clientes', json=data)
        if response.status_code == 201:
            print(f"Cliente Registrado: Nome: {self.nome}, Morada: {self.morada}, Telefone: {self.telefone}")
            # Limpar campos do formulário
            self.nome_input.text = ''
            self.morada_input.text = ''
            self.telefone_input.text = ''
        else:
            print("Erro ao registrar cliente!")
            # Exibir mensagem de erro para o usuário
            # Por exemplo, usando um popup do Kivy
