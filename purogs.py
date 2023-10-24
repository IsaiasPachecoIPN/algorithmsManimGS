
galeShapleyGroupOne = {
    "xavier": ["amy", "bertha", "clare"],
    "yancey": ["bertha", "amy", "clare"],
    "zeus": ["amy", "bertha", "clare"],
}

galeShapleyGroupTwo = {
    "amy": ["yancey", "xavier", "zeus"],
    "bertha": ["xavier", "yancey", "zeus"],
    "clare": ["xavier", "yancey", "zeus"],
}


def getPreferenceOfElements(group_id, elem_1, elem_2):
    #print("group_id: ", group_id)
    #print("elem_1: ", elem_1)
    #print("elem_2: ", elem_2)
    #Retorna si el elemento 1 esta antes que el elemento 2 en la lista de preferencias del galeShapleyGroupTwo
    return galeShapleyGroupTwo[group_id].index(elem_1) < galeShapleyGroupTwo[group_id].index(elem_2)

def getFianceOfElement(elem_val, lista_asignaciones):
    #Retorna el elemento con el que esta casado el elemento group_id
    for elem in lista_asignaciones:
        if elem[1] == elem_val:
            return elem[0]
    return None

def removeElemFromList(elem, lista):
    #Retorna la lista sin el elemento elem
    return [x for x in lista if x != elem]

def galeShapleyAlgorithm(scene,groupOne, groupTwo):

    lista_asignaciones = []
    solteras = [key for key in galeShapleyGroupTwo.keys()]
    solteros = [key for key in galeShapleyGroupOne.keys()]

    #print("solteras: ", solteras)
    #print("solteros: ", solteros)

    #Se inicia recorrer la lista de preferencias de cada elemento del grupo 1
    while len(solteras) > 0:
        for key, value in galeShapleyGroupOne.items():
            print("key: ", key)
            for val in value:
                print("val: ", val)
                #addGSEvalueationPairsAnimation(scene, str(key), str(val))
                #Si la mujer val esta soltera
                if val in solteras:
                    lista_asignaciones.append([key, val])
                    solteras = removeElemFromList(val, solteras)
                    solteros = removeElemFromList(key, solteros)
                    #Una vez que key ha esta en una asignacion con val, se elimina val de la lista de preferencias de key
                    galeShapleyGroupOne[key] = removeElemFromList(val, galeShapleyGroupOne[key])
                    break
                elif (getPreferenceOfElements(val, key, getFianceOfElement(val, lista_asignaciones))):
                    old_fiance = getFianceOfElement(val, lista_asignaciones)
                    lista_asignaciones.remove([getFianceOfElement(val, lista_asignaciones), val])
                    lista_asignaciones.append([key, val])
                    solteros = removeElemFromList(key, solteros)
                    solteros.append(old_fiance)
                    break
                else:
                    print("No se hace nada")

                
            
            print("lista_asignaciones: ", lista_asignaciones)
    
    print("solteras: ", solteras)
    print("solteros: ", solteros)
    #Se muestra la lista de preferencias de los solteros
    for i in solteros:
        print("i: ", galeShapleyGroupOne[i])

galeShapleyAlgorithm(None, galeShapleyGroupOne, galeShapleyGroupTwo)