from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

           
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
