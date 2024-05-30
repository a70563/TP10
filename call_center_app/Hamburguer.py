from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests


class HamburguerForm(BoxLayout):
    def __init__(self, **kwargs):
        super(HamburguerForm, self).__init__(**kwargs)
        self.database = None
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

    def set_database(self, database):
        self.database = database
        
    def on_nome_hamburguer_text(self, instance, value):
        self.nome_hamburguer = value

    def on_ingredientes_text(self, instance, value):
        self.ingredientes = value

    def submit_hamburguer(self, instance):
        data = {
            'nome_hamburguer': self.nome_hamburguer,
            'ingredientes': self.ingredientes
        }
        response = requests.post('http://127.0.0.1:5000/hamburgueres', json=data)
        if response.status_code == 201:
            print(f"Hambúrguer Registrado: Nome: {self.nome_hamburguer}, Ingredientes: {self.ingredientes}")
            # Limpar campos do formulário
            self.nome_hamburguer_input.text = ''
            self.ingredientes_input.text = ''
        else:
            print("Erro ao registrar hambúrguer!")
            # Exibir mensagem de erro para o usuário
            # Por exemplo, usando um popup do Kivy
