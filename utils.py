from manim import *
from main import DEFAULT_BOX_WIDTH, DEFAULT_BOX_HEIGHT

class Elem:

    """
        Clase para representar los elementos
    """

    def __init__(self):
        self.color = "#87c2a5"
        self.text = "Elem"
        self.id = 0
    
    def getFigure(self):
        return create_textbox(self.color, self.text, self.id)
    
    def changeFigureColor(self, color):
        self.color = color
        return self
    
    def changeFigureText(self, text):
        self.text = text
        return self
    
    def getID(self):
        return self.id
    
    def setID(self, id):
        self.id = id
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


def construirListaPreferencias(elem_id, lista_preferencias, color = "#F6CECE"):
     
     #De eleme se va a sacar el nombre del elemento
     obj = HM()
     obj.getElemento().setID(elem_id)
     obj.getElemento().changeFigureText(elem_id)
     for i in range(len(lista_preferencias)):
         obj_elem = Elem().changeFigureText(lista_preferencias[i]).changeFigureColor(color)
         obj_elem.setID(elem_id+lista_preferencias[i])
         obj.addToListaPreferencias(obj_elem)
    
     return obj
     

def create_textbox(color, string, ID = None):

    print("ID: ", ID)

    result = VGroup() # create a VGroup
    result.name = ID
    box = Rectangle(  # create a box
        height=DEFAULT_BOX_HEIGHT, width=DEFAULT_BOX_WIDTH, fill_color=color, 
        fill_opacity=0.5, stroke_color=color, name = ID
    )
    print("box: ", box.get_center())
    text = Text(string) # create text
    result.add(text,box) # add both objects to the VGroup
    #result.add(box) # add both objects to the VGroup
    return result