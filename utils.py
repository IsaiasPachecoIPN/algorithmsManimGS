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


class Hombre(Persona):
    
        def __init__(self) -> None:
            super().__init__()
            self.color = "#87c2a5"
            self.text = "Hombre"

        def getElemento(self):
            return self.elemento

class Mujer(Persona):

        def __init__(self) -> None:
            super().__init__()
            self.color = "#f7cdab"
            self.text = "Mujer"


def construirListaA():
     
     hombre = Hombre()
     elemA = Elem().changeFigureText("A")
     elemB = Elem().changeFigureText("B")
     elemC = Elem().changeFigureText("C")

     hombre.addToListaPreferencias(elemA)
     hombre.addToListaPreferencias(elemB)
     hombre.addToListaPreferencias(elemC)

     return hombre

def create_textbox(color, string):
    result = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        height=2, width=3, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    text = Text(string).move_to(box.get_center()) # create text
    result.add(box, text) # add both objects to the VGroup
    return result