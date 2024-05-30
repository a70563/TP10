from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from database import Database
from Cliente import ClienteForm
from Hamburguer import HamburguerForm
from Pedido import PedidoForm

class CallCenterApp(App):
    def build(self):
        self.database = Database()
        
        root = BoxLayout(orientation='vertical')
        
        self.cliente_form = ClienteForm()
        self.cliente_form.set_database(self.database)
        root.add_widget(self.cliente_form)
        
        self.hamburguer_form = HamburguerForm()
        self.hamburguer_form.set_database(self.database)
        root.add_widget(self.hamburguer_form)
        
        self.pedido_form = PedidoForm()
        self.pedido_form.set_database(self.database)
        root.add_widget(self.pedido_form)
        
        return root

if __name__ == '__main__':
    CallCenterApp().run()

