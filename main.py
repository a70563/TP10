from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Cliente import ClienteForm
from Hamburguer import HamburguerForm
from Pedido import PedidoForm


        
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
