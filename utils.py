from manim import *


class Elem:

    """
        Clase para representar los elementos
    """

    def __init__(self):
        self.color = "#87c2a5"
        self.text = "Elem"
    
    def getFigure(self):
        return create_textbox(self.color, self.text)
    
    def changeFigureColor(self, color):
        self.color = color
        return self
    
    def changeFigureText(self, text):
        self.text = text
        return self

class Persona(Elem):

    def __init__(self) -> None:
        super().__init__()
        self.elemento = Elem()
        self.lista_preferencias = []

    def changeTipeText(self, text):
        self.text = text
        return self
    
    def addToListaPreferencias(self, elem):
        self.lista_preferencias.append(elem)
        return self
    
    def getListaPreferencias(self):
        return self.lista_preferencias


class HM(Persona):
    
        def __init__(self) -> None:
            super().__init__()
            self.color = "#87c2a5"
            self.text = "Hombre"

        def getElemento(self):
            return self.elemento


def construirListaA():
     
     hombre = HM()
     elemA = Elem().changeFigureText("A").changeFigureColor("#F6CECE")
     elemB = Elem().changeFigureText("B").changeFigureColor("#F6CECE")
     elemC = Elem().changeFigureText("C").changeFigureColor("#F6CECE")

     hombre.addToListaPreferencias(elemA)
     hombre.addToListaPreferencias(elemB)
     hombre.addToListaPreferencias(elemC)

     return hombre


def construirListaPreferencias(elem, lista_preferencias, color = "#F6CECE"):
     
     #De eleme se va a sacar el nombre del elemento
     obj = HM()
     for i in range(len(lista_preferencias)):
         obj_elem = Elem().changeFigureText(lista_preferencias[i]).changeFigureColor(color)
         obj.addToListaPreferencias(obj_elem)
    
     return obj
     

def create_textbox(color, string):
    result = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        height=1, width=2, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    print("box: ", box.get_center())
    #text = Text(string) # create text
    result.add(box) # add both objects to the VGroup
    return result