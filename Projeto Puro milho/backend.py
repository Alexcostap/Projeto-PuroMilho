from biblioteca import saida,retorno,cadastroPreco

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class Menu(Screen):
    def menu():
        return 'Tela de Menu'
class TelaAjustePreco(Screen):
    def inputs_AjustePreco(self):
        milho = float(self.ids.vlrMilho.text)
        canjicaPequena = float(self.ids.vlrCanjicaPequena.text)
        canjicaGrande = float(self.ids.vlrCanjicaGrande.text)
        pamonha = float(self.ids.vlrPamonha.text)
        boloMilho = float(self.ids.vlrBoloMilho.text)
        boloMacaxeira = float(self.ids.vlrBoloMacaxeira.text)
        peDeMoleque = float(self.ids.vlrPeDeMoleque.text)

        ajustePreco = cadastroPreco(milho,canjicaPequena,canjicaGrande,pamonha,boloMilho,boloMacaxeira,peDeMoleque)
        self.ids.resultado_label.text = "Os valores foram ajustados"

class TelaRetorno(Screen):
    def inputs_retorno(self):
        nome = self.ids.nome_input.text
        milho = int(self.ids.milhoQtdRetorno.text)
        canjicaPequena = int(self.ids.canjicaPequenaQtdRetorno.text)
        canjicaGrande = int(self.ids.canjicaGrandeQtdRetorno.text)
        pamonha = int(self.ids.pamonhaQtdRetorno.text)
        boloMilho = int(self.ids.boloMilhoQtdRetorno.text)
        boloMacaxeira = int(self.ids.boloMacaxeiraQtdRetorno.text)
        peDeMoleque = int(self.ids.peDeMolequeQtdRetorno.text)

        retornoFuncao = retorno(nome,milho,canjicaPequena,canjicaGrande,pamonha,boloMilho,boloMacaxeira,peDeMoleque)
        #print(saidaFuncao)
        self.ids.resultado_label.text = f"{retornoFuncao[3]} retornou com R${retornoFuncao[0]:.2f}. Sendo o valor final R${retornoFuncao[1]:.2f} e sua comissão: R${retornoFuncao[2]:.2f}"
        self.ids.nome_input.text = ""
        self.ids.milhoQtdRetorno.text = ""
        self.ids.canjicaPequenaQtdRetorno.text = ""
        self.ids.canjicaGrandeQtdRetorno.text = ""
        self.ids.pamonhaQtdRetorno.text = ""
        self.ids.boloMilhoQtdRetorno.text = ""
        self.ids.boloMacaxeiraQtdRetorno.text = ""
        self.ids.peDeMolequeQtdRetorno.text = ""

class TelaSaida(Screen):
    def inputs_saida(self):
        nome = self.ids.nome_input.text
        milho = int(self.ids.milhoQtdSaida.text)
        canjicaPequena = int(self.ids.canjicaPequenaQtdSaida.text)
        canjicaGrande = int(self.ids.canjicaGrandeQtdSaida.text)
        pamonha = int(self.ids.pamonhaQtdSaida.text)
        boloMilho = int(self.ids.boloMilhoQtdSaida.text)
        boloMacaxeira = int(self.ids.boloMacaxeiraQtdSaida.text)
        peDeMoleque = int(self.ids.peDeMolequeQtdSaida.text)

        saidaFuncao = saida(nome,milho,canjicaPequena,canjicaGrande,pamonha,boloMilho,boloMacaxeira,peDeMoleque)
        #print(saidaFuncao)
        self.ids.resultado_label.text = f"{saidaFuncao[0]} saiu com R${saidaFuncao[1]:.2f}"
        self.ids.nome_input.text = ""
        self.ids.milhoQtdSaida.text = ""
        self.ids.canjicaPequenaQtdSaida.text = ""
        self.ids.canjicaGrandeQtdSaida.text = ""
        self.ids.pamonhaQtdSaida.text = ""
        self.ids.boloMilhoQtdSaida.text = ""
        self.ids.boloMacaxeiraQtdSaida.text = ""
        self.ids.peDeMolequeQtdSaida.text = ""

class MeuAplicativo(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Menu(name='Menu'))
        sm.add_widget(TelaAjustePreco(name='Ajuste de Preço'))
        sm.add_widget(TelaRetorno(name='Retorno'))
        sm.add_widget(TelaSaida(name='Saida'))
        return sm

Builder.load_file("tela.kv")

MeuAplicativo().run()
# saida = retorno('Alex Costa',0,5,5,0,3,0,5)
# print(saida)
