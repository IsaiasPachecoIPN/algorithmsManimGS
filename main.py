from manim import *
from utils import *


def agregarElementoAScene(scene, elem):
    scene.add(elem.getElemento().getFigure()  )
    first_elem = elem.lista_preferencias[0].getFigure()
    scene.add(first_elem.next_to(elem.getElemento().getFigure(), RIGHT))
    for i in range(1,len(elem.lista_preferencias)):
        scene.wait(1)
        mobject_len = len(scene.mobjects)
        #Agregar elementos debajo del ultimo mobject del scene 
        #scene.add(elem.lista_preferencias[i].getFigure().next_to(scene.mobjects[-1], DOWN))
        scene.add(elem.lista_preferencias[i].getFigure().next_to(scene.mobjects[mobject_len-2], DOWN, buff = MED_LARGE_BUFF))

    print("scence lenght: ", len(scene.mobjects))

class CreateScene(Scene):
    def construct(self):
        elem = construirListaA()
        agregarElementoAScene(self, elem)
        self.wait(2)