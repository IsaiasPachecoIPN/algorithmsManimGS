
galeShapleyGroupOne = {
    "worle": ["tom","ben","sophie","katherine","anna"],
    "priory": ["sophie","ben","tom","anna","katherine"],
    "wyvem": ["tom","katherine","anna","sophie","ben"],
    "broadoak": ["ben","tom","anna","sophie","katherine"],
    "sidcot": ["sophie","tom","anna","katherine","ben"],
}

galeShapleyGroupTwo = {
    "anna": ["sidcot","broadoak","priory","wyvem","worle"],
    "ben": ["priory","worle","sidcot","broadoak","wyvem"],
    "katherine": ["priory","broadoak","sidcot","wyvem","worle"],
    "sophie": ["wyvem","priory","worle","sidcot","broadoak"],
    "tom": ["wyvem","broadoak","worle","sidcot","priory"]
}

def isWomanSingle( w, arr_solteras):
    return True if w in arr_solteras else False

def assignMandWToBeEngaged(m,w, lista_asignaciones):
    lista_asignaciones.append([m, w])

def isSomeManSingle( arr_solteros ):
    """
    Retorna si hay algun hombre soltero en el arreglo
    """
    return True if len(arr_solteros) > 0 else False

def addSingleManToArr( man, arr_solteros ):
    arr_solteros.append(man)

def getPreferenceOfElements(group_id, elem_1, elem_2):
    #print("group_id: ", group_id)
    #print("elem_1: ", elem_1)
    #print("elem_2: ", elem_2)
    #Retorna si el elemento 1 esta antes que el elemento 2 en la lista de preferencias del galeShapleyGroupTwo
    return galeShapleyGroupTwo[group_id].index(elem_1) < galeShapleyGroupTwo[group_id].index(elem_2)

def getFianceOfElement(elem_val, lista_asignaciones):
    #Retorna el elemento con el que esta casado el elemento group_id
    for elem in lista_asignaciones:
        if elem_val in elem:
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
    while isSomeManSingle(solteros) and isSomeManSingle(solteras):
        for m, m_preference_list in galeShapleyGroupOne.items():
            if not isSomeManSingle(solteros):
                break
            if( getFianceOfElement(m, lista_asignaciones) != None ):
                continue # m is not single
            print("m: ", m)
            for w in m_preference_list:
                print("w: ", w)
                #If w is single, then m and w become engaged
                if isWomanSingle(w, solteras):
                    assignMandWToBeEngaged(m, w, lista_asignaciones)
                    solteras = removeElemFromList(w, solteras)
                    solteros = removeElemFromList(m, solteros)
                    #if m and w are engaged, w is removed from m's preference list
                    galeShapleyGroupOne[m] = removeElemFromList(w, galeShapleyGroupOne[m])
                    break
                # If w is not single, then w chooses between m and her fiance
                elif (getPreferenceOfElements(w, m, getFianceOfElement(w, lista_asignaciones))):
                    old_fiance = getFianceOfElement(w, lista_asignaciones)
                    lista_asignaciones.remove([old_fiance, w])
                    assignMandWToBeEngaged(m, w, lista_asignaciones)
                    galeShapleyGroupOne[m] = removeElemFromList(w, galeShapleyGroupOne[m])
                    solteros = removeElemFromList(m, solteros)
                    addSingleManToArr(old_fiance, solteros)
                    break
                else:
                    #w rejects m
                    galeShapleyGroupOne[m] = removeElemFromList(w, galeShapleyGroupOne[m])
                    break
                    

                
            print("Lista solteras: ", solteras)
            print("Lista solteros: ", solteros)
            print("lista_asignaciones: ", lista_asignaciones)
    

galeShapleyAlgorithm(None, galeShapleyGroupOne, galeShapleyGroupTwo)