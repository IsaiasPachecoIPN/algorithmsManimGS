from manim import *
from utils import *


DEFAULT_BUFF = 0.25
Y_DEFAULT_COORD = DEFAULT_BUFF * 3

galeShapleyGroupOne = {
    "h1": ["m1", "m2", "m3"],
    "h2": ["m2", "m1", "m3"],
    "h3": ["m3", "m2", "m1"],
}

galeShapleyGroupTwo = {
    "m1": ["h1", "h2", "h3"],
    "m2": ["h2", "h1", "h3"],
    "m3": ["h3", "h1", "h2"],
}

def getNextListStartPoint(scence):

    """
        Function to get the next coord point to add the next
        fisrt group list of preferences in the scene
    """

    #Return fistElement x and LastElement y
    firstElement = scence.mobjects[0]
    lastElement = scence.mobjects[-1]
    y_coord =  lastElement.get_y() - ( 1 + firstElement.get_height() - Y_DEFAULT_COORD) 
    #print("y_coord: ", y_coord)
    return [firstElement.get_center()[0], y_coord, 0]

def addGSEvalueationPairsAnimation(scene, elemA, elemB ):

    elem_a = getElemByID(elemA, scene)
    elem_b = getElemByID(elemB, scene)

    scene.play(elem_a.animate.set_fill("#FFF400"))
    scene.play(elem_b.animate.set_fill("#FFF400"))

    scene.play(elem_a.animate(rate_func=there_and_back).flip())    
    scene.play(elem_b.animate(rate_func=there_and_back).flip())

def addElementToScene(scene, elem, nextTo = None, position = DOWN, coords = None):
    
    """
    Function to add an element to the scene
    (param) scene: Scene
    (param) elem: Element
    (param) nextTo: Element
    (param) position: Position
    """

    if nextTo == None:
        scene.add(elem.getElemento().getFigure())
    elif coords != None:
        scene.add(elem.getElemento().getFigure().move_to(coords))
    else:
        scene.add(elem.getElemento().getFigure().next_to(nextTo, position))

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
        scene.add(new_mobject.next_to(last_mobject.get_center(), DOWN, buff = Y_DEFAULT_COORD))
        #Print y coord of new_mobject
        #print("new_mobject: ", new_mobject.get_y())


def showAllMobjectIDs(scene):
    for elem in scene.mobjects:
        #Si el elemento es de tipo VGroup se obtiene el elemnto [1]
        if( type (elem) == VGroup):
            print("elem: ", elem.name)


def getElemByID(id, scene):
    for elem in scene.mobjects:
        if elem.name == id:
            return elem
    return None

class CreateScene(Scene):
    def construct(self):
        self.width = 2000
        self.height = 2000
        
        elem = construirListaPreferencias("h1", galeShapleyGroupOne["h1"])
        #elem2 = construirListaPreferencias("h2", galeShapleyGroupOne["h2"], "#0B2161")
        elem3 = construirListaPreferencias("m1", galeShapleyGroupTwo["m1"], "#0B2161")
        addElementToScene(self, elem)
        #print("NextListStartPoint: ", getNextListStartPoint(self))
        #addElementToScene(self, elem2, self.mobjects[0], coords=getNextListStartPoint(self))
        addElementToScene(self, elem3, self.mobjects[1], position=RIGHT)

        self.wait(1)
        #getElemByID("h1m1", self).animate.set_color("#FFF400")
        #rectToAnimate = getElemByID("h1m1", self)
        #self.play(rectToAnimate.animate.set_fill("#FFF400"))
        #self.play(rectToAnimate.animate(rate_func=there_and_back).flip())
        
        #Se inicia la lista de preferencias
        addGSEvalueationPairsAnimation(self, "h1m1", "m1h1")

        print("mobjects: ", self.mobjects)
        showAllMobjectIDs(self)

        self.wait(2)