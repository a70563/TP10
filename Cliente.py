from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
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