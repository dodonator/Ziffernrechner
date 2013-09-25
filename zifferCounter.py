'''
Es gibt Zahlen, in denen jede Ziffer nur einmal vorkommt.
Beispiel: 1987 oder 2013
Das Programm soll diese Zahlen in einem vorgegebenen Bereich finden.
'''
def zifferCounter(zahl):
    ziffernCounter = [0,0,0,0,0,0,0,0,0,0]
    for tmpZiffer in zahl:
        tmpZiffer = int(tmpZiffer)
        for i in range(10):
            if tmpZiffer == i:
                ziffernCounter[i] += 1
    return ziffernCounter

def uniqueTester(zC):
    result = []
    testResult = []
    for i in range(10):
        testResult.append(True)
    for element in zC:
        if element == 1 or element == 0:
            result.append(True)
        else:
            result.append(False)
    if result == testResult:
        return True # Jede Ziffer kommt nur einmal vor
    else:
        return False # Eine Ziffer kommt mehrmals vor
        
def eingabe():
    anfang = raw_input('Bitte geben sie den Anfang des Wertebereichs ein: \n')
    MaxZahl = raw_input('Bitte geben sie die maximale Zahl ein: \n')
    difSortWahl = raw_input('''
Möchten Sie einen Differenzsortierer:
0: Keinen Differenzsortierer
MAX: Maximalen Wert zur Sortierung
MIN: Minimaler Wert zur Sortierung
MM: Beide
''')
    return [anfang, MaxZahl,difSortWahl]

def differenz(a,b):
    d = int(b) - int(a)
    return d
def dmax(difList):
    return max(difList)
def dmin(difList):
    return min(difList)
def differenzSortiererMin(difList,minZahl):
    result = []
    for element in difList:
        if element >= minZahl:  
            result.append(element)
        else:
            continue
    return result
def differenzSortiererMax(difList,maxZahl):
    result = []
    for element in difList:
        if element <= maxZahl:  
            result.append(element)
        else:
            continue
    return result

def frequenz(Durchlaeufe,Anzahl):
    f = Durchlaeufe/Anzahl
    return f
    
def main():
    global RESKeys
    RESKeys = ['X','Y','F','L','LENL','RL','DL','DSW']
    RES = {}
    lastI = 0
    resultListe = []
    Liste = []
    DifferenzListe = []
    Eingabe = eingabe()
    anfang = Eingabe[0]
    maxZahl = Eingabe[1]
    difSortWahl = Eingabe[2]
    for i in range(int(anfang),int(maxZahl)+1):
        i = str(i)
        result = uniqueTester(zifferCounter(i))
        if result == True:
            resultListe.append(result)
            DifferenzListe.append(differenz(lastI,i))
            Liste.append(i)
            # print i
        else:
             resultListe.append(False)
             continue
        lastI = i
    if difSortWahl == '0':
        pass
        
    if difSortWahl == 'MIN':
    
        minZahl = raw_input('Minimum:\n')
        difSortMin = differenzSortiererMin(DifferenzListe,minZahl)
        RES['DSMIN'] = difSortMin
        RESKeys.append('DSMIN')
    if difSortWahl == 'MAX':
    
        maxZahl = raw_input('Maximum:\n')
        difSortMax = differenzSortiererMin(DifferenzListe,maxZahl)
        RES['DSMAX'] = difSortMax
        RESKeys.append('DSMAX')
        
    if difSortWahl == 'MM':
        minZahl = raw_input('Minimum:\n')
        maxZahl = raw_input('Maximum:\n')
        difSortMin = differenzSortiererMin(DifferenzListe,minZahl)
        difSortMax = differenzSortiererMin(DifferenzListe,maxZahl)
        RES['DSMAX'] = difSortMax
        RES['DSMIN'] = difSortMin
        RESKeys.append('DSMIN')
        RESKeys.append('DSMAX')
    RES['X'] = int(anfang)
    RES['Y'] = maxZahl
    RES['F'] = frequenz((int(maxZahl)),len(Liste))
    RES['L'] = Liste
    RES['LENL'] = len(Liste)
    RES['RL'] = resultListe
    RES['DL'] = DifferenzListe
    RES['DSW'] = difSortWahl
    RES['DMIN'] = dmin(DifferenzListe)
    RES['DMAX'] = dmax(DifferenzListe)
    RESKeys.append('DMIN')
    RESKeys.append('DMAX')
    print RES['Y']
    print RES['LENL']
    print RES['F']
    
    return RES

def Output(DICT,Auswahl):
    for element in RESKeys:
        if element == Auswahl:
            print DICT[Auswahl]
    
M = main()
I = raw_input('Wahl des Outputs: \n')
Output(M,I)
    




        
