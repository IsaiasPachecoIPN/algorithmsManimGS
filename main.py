from manim import *
from utils import *


listagaleShapley = {
    "h1": ["m1", "m2", "m3"],
    "h2": ["m2", "m1", "m3"],
    "h3": ["m3", "m2", "m1"],
    "m1": ["h1", "h2", "h3"],
    "m2": ["h2", "h1", "h3"],
    "m3": ["h3", "h1", "h2"],
}

def agregarElementoAScene(scene, elem, nextTo = None):
    
    if nextTo == None:
        scene.add(elem.getElemento().getFigure())
    else:
        scene.add(elem.getElemento().getFigure().next_to(nextTo, RIGHT))

    first_elem = elem.lista_preferencias[0].getFigure()
    
    scence_lenght = len(scene.mobjects)
    last_mobject = scene.mobjects[scence_lenght-1]
    
    scene.add(first_elem.next_to(last_mobject, RIGHT))



    #mostrar coordenadas de firs_elem
    for i in range(1,len(elem.lista_preferencias)):
        scence_lenght = len(scene.mobjects)
        scene.wait(1)
        new_mobject = elem.lista_preferencias[i].getFigure()
        last_mobject = scene.mobjects[scence_lenght-1]
        new_buff = (new_mobject.get_height() + last_mobject.get_height())/2
        scene.add(new_mobject.next_to(last_mobject.get_center(), DOWN, buff = new_buff-0.1))

class CreateScene(Scene):
    def construct(self):
        self.width = 2000
        self.height = 2000
        elem = construirListaPreferencias("", listagaleShapley["h1"])
        elem2 = construirListaPreferencias("", listagaleShapley["h2"], "#0B2161")
        agregarElementoAScene(self, elem)
        agregarElementoAScene(self, elem2, self.mobjects[1])
        self.wait(2)