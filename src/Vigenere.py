'''
Santiago Díaz Pontón, No.cuenta: 317164402
Criptografía y Ciberseguridad, 2024-1
Clase correspondiente a la tarea Vigenere.
'''
class Vigenere():
    cypher = "YYAXQ ACFIT LYYTL EAHVV GFVMH CRXRR SAHXQ RRXWZ GGNKT NVLXG VIVGS ATMSG JLHBM AIESK KCAYD RZHVI SJGNQ AIXPK BYEVH TFXRK ECTHD NKXVU WMZXI OIJYK VYFMQ UZKPU LIZTQ IEMEI LIHGQ EXBQO WHGHT NRVSS HUABZ OLGIY UONWQ OEXWS WDBKP UVWIY LLHBQ LFVST KYTNH RTBIT NCPMN RZTWK FWVXM BRMER DUFGNEJEES WXVWZ DVEEN SVVEH DRWWU EYGXQ ACXRK ECTHR IEEYI ZUEXR LRLYV JYZTD XTXPK FWVTC EVLXK EIQHK OHNIK KXRFZ XZFEO EJBKS AEVMG WHYTF UVKVG WMNMZ CRKPG WMGKZ TVZMG VYYXM EDBKU DIFXF UEWSS WDBKD SIHQV WLFNR ACBET RUFFD DZTRZ WFNWH PCHQG UCNXM TVKGK JFHZZ RMBIT WUGTB AITWA WDRKB IKHCR SJRHQ DVMSJ SMYTR EJMVG LYTBZ SVLEZ SWNKB ILWEJ WMNMZ CRKGO MXNWD SVLER YIDND SFESN SXRAZ CVKWK UONGC OEHLG QHVGF UETSZ JUNES EIGEZ APNRZ QLXPG HLRIZ RRVMU FXRXR CLWSY QMHMQ AELTU JNRRS EEXVV JYCTQ AUTWR SMNKL AJRIR WKHBO OEXGK KUEBN RVJYO WLRTK MVGSY LLRLL EJXWE EIAMZ RCTWS SKHBM AJWIG KYQBN YCTWK KWNEZ SGTVG SMNES AIEEY EOETK LRLVK IOVXQ EFMVU KNEXR MVLIY SXVVH OETPK KYYZD NVKER AHPTO AQWII GHGKN LRKWA AGCTB IVGGO SIEWD NRKEG DUFMQ OGTWI SLTTQ CFGXX SFNLL UITPR SMPHM ECKIY MFGTC OUXUA WOAMD RTBSJ WYYEZ SGXVK UYETR IEAEH WLGHL AUHPG UCHWZ DRLMJ WWNEZ MZMSY GYFTS ATTVI AOQTC EJTWO HORLK OJOIX VUQXQ ADXRZ WBNUH LVLIT DUTND RITWU EYGXM ACXNK JWVMN EEXQO YIFBM BRMER DUEVZ PKNVG FFNLB ILWEJ WMRGD MZZEY KCATR ACMEX DUFRR ERISJ WLNGC ECXWZ SXBXM EDBKU KCAVZ MGTRG KJEHK OEZEJ SMFNL EKTIY LIZTQ IEMEI LIGHC OTNET LIUTX BRCSK DWVXK ODXHO SHGXB OELMJ WLNVH OEXWK KNETS EXBGG KWBFN RVLYR LUQHR UJMVU HUFGN SVWIY YUFMZ RRGCR SMTTM AEVMG KMRKZ NTHQV DYGTR EJMIK KYYTQ TVWIR SYFMQ AKXKO SISXM SZOEK FWBGR ETNIT UCNXK AIMIJ WOFTQ TIHTG KYFXR TVLMY WYFWH EQOII WMFNO EIBSX SFRGD MZZSX GXRTC LVLMY WYFVH NTHZK UYFFZ SWNIX LYNMZ CRWPK KCFXS IVGIK DXBUK EUXJA WLMTR DZOMJ AXYXR IJXIY LUNEZ PRKWA HYETC LVFIJ AUAMD UEUYK FJYTM SZLIK KNNXM IEYIX AIEBC AUGYS WLVVZ SVWGG HUPXR DVFET LYAXQ ASBIX LUHGZ VZTHK JYGBQ AUTCY AMRXR TRXRJ WMIXM TRCEK FNBWN SCHWG KJRVS OJLIJ UUCTB EJWIK DOQBQ LVIYK KOATE UVKDG HYDND NRGSK KHNWZ EOVIV LIOHS IEIEX SOATL AJISJ WLBLZ SZLIK FZEXM TRTIR DUGXL EITVO SGRGS EVEKK FYETK EJXPG KCFMD NKXHK DMBUD RRGSJ WFRLS AUHWO WMGTZ SZLXK FWVTD SVLXX WWUTD LVLXG VIFXQ AWNIX LYFBM DLWEY AYFWD BZEIR WMGTC OJXVG UCRKS ADXRZ WXRUH L"
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    texto = "Puedo escribir los versos mas tristes esta noche Escribir por ejemplo La noche esta estrellada, y tiritan azules los astros a lo lejos El viento de la noche gira en el cielo y canta Puedo escribir los versos mas tristes esta noche Yo la quise y a veces ella tambien me quiso En las noches como esta la tuve entre mis brazos La bese tantas veces bajo el cielo infinito Ella me quiso a veces yo tambien la queria Como no haber amado sus grandes ojos fijos Puedo escribir los versos mas tristes esta noche Pensar que no la tengo Sentir que la he perdido Oír la noche inmensa mas inmensa sin ella Y el verso cae al alma como al pasto el rocio Que importa que mi amor no pudiera guardarla La noche esta estrellada y ella no está conmigo Eso es todo A lo lejos alguien canta A lo lejos Mi alma no se contenta con haberla perdido Como para acercarla mi mirada la busca Mi corazon la busca y ella no esta conmigo La misma noche que hace blanquear los mismos arboles Nosotros los de entonces ya no somos los mismos Ya no la quiero es cierto pero cuanto la quise Mi voz buscaba el viento para tocar su oido De otro Sera de otro Como antes de mis besos Su voz su cuerpo claro Sus ojos infinitos Ya no la quiero es cierto pero tal vez la quiero Es tan corto el amor y es tan largo el olvido Porque en noches como esta la tuve entre mis brazos mi alma no se contenta con haberla perdido Aunque este sea el ultimo dolor que ella me causa y estos sean los ultimos versos que yo le escribo"
    clave = "NAHUALES"
    texto = texto.upper()
    vig1 = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    vig2 = "A A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    vig3 = "B B C D E F G H I J K L M N O P Q R S T U V W X Y Z A"
    vig4 = "C C D E F G H I J K L M N O P Q R S T U V W X Y Z A B"
    vig5 = "D D E F G H I J K L M N O P Q R S T U V W X Y Z A B C"
    vig6 = "E E F G H I J K L M N O P Q R S T U V W X Y Z A B C D"
    vig7 = "F F G H I J K L M N O P Q R S T U V W X Y Z A B C D E"
    vig8 = "G G H I J K L M N O P Q R S T U V W X Y Z A B C D E F"
    vig9 = "H H I J K L M N O P Q R S T U V W X Y Z A B C D E F G"
    vig10 = "I I J K L M N O P Q R S T U V W X Y Z A B C D E F G H"
    vig11 = "J J K L M N O P Q R S T U V W X Y Z A B C D E F G H I"
    vig12 = "K K L M N O P Q R S T U V W X Y Z A B C D E F G H I J"
    vig13 = "L L M N O P Q R S T U V W X Y Z A B C D E F G H I J K"
    vig14 = "M M N O P Q R S T U V W X Y Z A B C D E F G H I J K L"
    vig15 = "N N O P Q R S T U V W X Y Z A B C D E F G H I J K L M"
    vig16 = "O O P Q R S T U V W X Y Z A B C D E F G H I J K L M N"
    vig17 = "P P Q R S T U V W X Y Z A B C D E F G H I J K L M N O"
    vig18 = "Q Q R S T U V W X Y Z A B C D E F G H I J K L M N O P"
    vig19 = "R R S T U V W X Y Z A B C D E F G H I J K L M N O P Q"
    vig20 = "S S T U V W X Y Z A B C D E F G H I J K L M N O P Q R"
    vig21 = "T T U V W X Y Z A B C D E F G H I J K L M N O P Q R S"
    vig22 = "U U V W X Y Z A B C D E F G H I J K L M N O P Q R S T"
    vig23 = "V V W X Y Z A B C D E F G H I J K L M N O P Q R S T U"
    vig24 = "W W X Y Z A B C D E F G H I J K L M N O P Q R S T U V"
    vig25 = "X X Y Z A B C D E F G H I J K L M N O P Q R S T U V W"
    vig26 = "Y Y Z A B C D E F G H I J K L M N O P Q R S T U V W X"
    vig27 = "Z Z A B C D E F G H I J K L M N O P Q R S T U V W X Y"
    numA = 0
    numB = 0
    numC = 0
    numD = 0
    numE = 0
    numF = 0
    numG = 0
    numH = 0
    numI = 0
    numJ = 0
    numk = 0
    numL = 0
    numM = 0
    numN = 0
    numÑ = 0
    numO = 0
    numP = 0
    numQ = 0
    numR = 0
    numS = 0
    numT = 0
    numU = 0
    numV = 0
    numW = 0
    numX = 0
    numY = 0
    numZ = 0
    total = 0
    tablaVigenere = []
    numeroDeLetrasEnOrden = []
    cifrado = " "
    descifrado = " "
    textoPorEspacio = []
    cifradoEnString = ""
    textoTotal = []

    """
     * Constructor de la clase.
     * Lee un archivo conteniendo un criptograma, nos devuelve las ocurrencias de cada una de las letras, total de letras, y además mete el número total
     * de ocurrencias de cada una de las letras en una lista
    """
    def __init__(self):
        textoCifrado = self.cypher
        self.cifradoEnString= self.readFile(self.cypher)
        self.cuentaLetras(self.textoTotal)
        self.muestraNumLetras()
        self.meteEnListaAlfabeto()
        self.meteVigenere

    def meteVigenere(self):
        self.tablaVigenere.append(self.vig1)
        self.tablaVigenere.append(self.vig2)
        self.tablaVigenere.append(self.vig3)
        self.tablaVigenere.append(self.vig4)
        self.tablaVigenere.append(self.vig5)
        self.tablaVigenere.append(self.vig6)
        self.tablaVigenere.append(self.vig7)
        self.tablaVigenere.append(self.vig8)
        self.tablaVigenere.append(self.vig9)
        self.tablaVigenere.append(self.vig10)
        self.tablaVigenere.append(self.vig11)
        self.tablaVigenere.append(self.vig12)
        self.tablaVigenere.append(self.vig13)
        self.tablaVigenere.append(self.vig14)
        self.tablaVigenere.append(self.vig15)
        self.tablaVigenere.append(self.vig16)
        self.tablaVigenere.append(self.vig17)
        self.tablaVigenere.append(self.vig18)
        self.tablaVigenere.append(self.vig19)
        self.tablaVigenere.append(self.vig20)
        self.tablaVigenere.append(self.vig21)
        self.tablaVigenere.append(self.vig22)
        self.tablaVigenere.append(self.vig23)
        self.tablaVigenere.append(self.vig24)
        self.tablaVigenere.append(self.vig25)
        self.tablaVigenere.append(self.vig26)
        self.tablaVigenere.append(self.vig27)
    def deleteRepeated(self):
        nuevaClave = ""
        for letra in self.clave:
            if(not letra in nuevaClave):
                nuevaClave+=letra
        print(nuevaClave)
        self.clave = nuevaClave
    """
     * Cuenta el número de incidencias de cada una de las letras del alfabeto en una cadena.
     * @Param string la cadena de la cual contará las incidencias de las letras
    """
    def cuentaLetras(self, string):
            self.cifrado = string
            for i in range(len(string)):
                if(string[i] == 'K'):
                    self.numk+= 1
                if(string[i] == 'P'):
                    self.numP += 1
                if(string[i] == 'M'):
                    self.numM += 1
                if(string[i] == 'F'):
                    self.numF += 1
                if(string[i] == 'Q'):
                    self.numQ += 1
                if(string[i] == 'J'):
                    self.numJ += 1
                if(string[i] == 'A'):
                    self.numA+= 1
                if(string[i] == 'B'):
                    self.numB+= 1
                if(string[i] == 'C'):
                    self.numC+= 1
                if(string[i] == 'D'):
                    self.numD+= 1
                if(string[i] == 'E'):
                    self.numE+= 1
                if(string[i] == 'G'):
                    self.numG+= 1
                if(string[i] == 'H'):
                    self.numH+= 1
                if(string[i] == 'I'):
                    self.numI+= 1
                if(string[i] == 'L'):
                    self.numL+= 1
                if(string[i] == 'N'):
                    self.numN+= 1
                if(string[i] == 'Ñ'):
                    self.numÑ+= 1
                if(string[i] == 'O'):
                    self.numO+= 1
                if(string[i] == 'R'):
                    self.numR+= 1
                if(string[i] == 'S'):
                    self.numS+= 1
                if(string[i] == 'T'):
                    self.numT += 1
                if(string[i] == 'U'):
                    self.numU += 1
                if(string[i] == 'V'):
                    self.numV += 1
                if(string[i] == 'W'):
                    self.numW+= 1
                if(string[i] == 'X'):
                    self.numX += 1
                if(string[i] == 'Y'):
                    self.numY += 1
                if(string[i] == 'Z'):
                    self.numZ += 1
                self.total +=1
    """
     * Imprime en pantalla el número de ocurrencias por letra.
    """
    def muestraNumLetras(self):
        print("total de letras = ", self.total)
        print("Tabla de frecuencias:")
        print("A = ", self.numA)
        print("B = ", self.numB)
        print("C = ", self.numC)
        print("D = ", self.numD)
        print("E = ", self.numE)
        print("F = ", self.numF)
        print("G = ", self.numG)
        print("H = ", self.numH)
        print("I = ", self.numI)
        print("J = ", self.numJ)
        print("k = ", self.numk)
        print("L = ", self.numL)
        print("M = ", self.numM)
        print("N = ", self.numN)
        print("Ñ = ", self.numÑ)
        print("O = ", self.numO)
        print("P = ", self.numP)
        print("Q = ", self.numQ)
        print("R = ", self.numR)
        print("S = ", self.numS)
        print("T = ", self.numT)
        print("U = ", self.numU)
        print("V = ", self.numV)
        print("W = ", self.numW)
        print("X = ", self.numX)
        print("Y = ", self.numY)
        print("Z = ", self.numZ)

    """
     * Lee archivo y actualiza variables de clase,
     * Actualiza tres variables:
     * 1- TextoPorEspacio: Regresa una lista donde cada índice es el criptograma separado por cada espacio (5 caracteres exactamente excepto por el último)
     * 2- total: criptograma pero en string
     * 3- TextoTotal: criptograma pero en lista.
     * @return el criptograma pero en una sola cadena
    """
    def readFile(self, textoCifrado):
        palabra = ""
        total= ""
        for texto in textoCifrado:
            palabra += texto
            if(texto == " " or texto == '\n'):
                self.textoPorEspacio.append(palabra[:len(palabra)-1])
                palabra =""
            if(texto != " " and texto != '\n'):
                total += texto
                self.textoTotal.append(texto)
        return total


    """
     * Calcula el número de incidencias del criptograma
     * @return el número de incidencias.
    """
    def numeroDeIncidencias(self):
        sumatotal = 0
        dividendo = self.total*(self.total-1)
        print(self.numeroDeLetrasEnOrden)
        for letra in range(27):
            num1 = self.numeroDeLetrasEnOrden[letra]
            num2 = num1*(num1-1)
            num3 = num2/dividendo
            sumatotal+=num3
        print("Índice  de Coindidencias: ", sumatotal)
        return sumatotal
    """
     * Calcula el número de alfabetos usando la fórmula para r, r~ (0.036)*N/((IC(T)*(N-1)-(0.038*N+0.0744))
     * @Param indiceDeCoindicendia el índice de coincidencia del criptograma.
    """
    def calculaNumeroDeAlfabetos(self, indiceDeCoincidencia):
        divisor = 0.036*self.total
        div1 = indiceDeCoincidencia*(self.total-1)
        div2 = (0.038*self.total)+ .0744
        totalAlfabetos = divisor/(div1-div2)
        print("r= ",totalAlfabetos)
        return round(totalAlfabetos)


    """
     * Dado el número de ocurrencias de una letra en un criptograma, actualiza la variables de clase donde se encuentra el número de cada una de las letras.
    """
    def meteEnListaAlfabeto(self):
        self.numeroDeLetrasEnOrden.append(self.numA)
        self.numeroDeLetrasEnOrden.append(self.numB)
        self.numeroDeLetrasEnOrden.append(self.numC)
        self.numeroDeLetrasEnOrden.append(self.numD)
        self.numeroDeLetrasEnOrden.append(self.numE)
        self.numeroDeLetrasEnOrden.append(self.numF)
        self.numeroDeLetrasEnOrden.append(self.numG)
        self.numeroDeLetrasEnOrden.append(self.numH)
        self.numeroDeLetrasEnOrden.append(self.numI)
        self.numeroDeLetrasEnOrden.append(self.numJ)
        self.numeroDeLetrasEnOrden.append(self.numk)
        self.numeroDeLetrasEnOrden.append(self.numL)
        self.numeroDeLetrasEnOrden.append(self.numM)
        self.numeroDeLetrasEnOrden.append(self.numN)
        self.numeroDeLetrasEnOrden.append(self.numÑ)
        self.numeroDeLetrasEnOrden.append(self.numO)  
        self.numeroDeLetrasEnOrden.append(self.numP)
        self.numeroDeLetrasEnOrden.append(self.numQ)
        self.numeroDeLetrasEnOrden.append(self.numR)
        self.numeroDeLetrasEnOrden.append(self.numS)
        self.numeroDeLetrasEnOrden.append(self.numT)
        self.numeroDeLetrasEnOrden.append(self.numU)
        self.numeroDeLetrasEnOrden.append(self.numV)
        self.numeroDeLetrasEnOrden.append(self.numW)
        self.numeroDeLetrasEnOrden.append(self.numX)
        self.numeroDeLetrasEnOrden.append(self.numY)
        self.numeroDeLetrasEnOrden.append(self.numZ)

    """
     * Calcula el número de factores primos de un número.
     * @Param numero el número a verificar sus factores primos
     * @return los factores primos del número
    """
    def factoresPrimos(self, numero):
        divisor = 2
        factores = []
        while(numero > 1):
            while(numero % divisor == 0):
                factores.append(divisor)
                numero = numero / divisor
            divisor += 1
        return factores
    """
     * Dada un texto, revisa las cadenas repetidas dentro de este. Una vez que tiene las cadenas repetidas, revisa la distancia entre las repeticiones,
     * y sus factores primos.
     * @return la cadena repetida, la distancia entre ellas y sus factores primos
     * PREGUNTA: ¿Cuál es la complejidad de este algoritmo?
     * Es una complejidad bastante elevada. Tomando en cuenta que estamos revisando CADA una de las letras al menos una vez, y luego volviendo a iterar
     * desde este índice al final de la cadena, la complejidad resulta ser n^2
    """
    def buscaRepetidas(self):
        cadenasRepetidas = []
        factoresPrimos = []
        distancias = []
        print("CADENA, DISTANCIA, FACTORES PRIMOS\n")
        print("----------------------------------------")
        for i in range(len(self.cifradoEnString)):
            initial = i+3
            # Busca apartir de las primeras 3 letras (y sólo buscamos apartir de la i, no entre todos los elementos para bajar complejidad)
            for j in range(initial,len(self.cifradoEnString)):
                #La cadena a buscar va desde i+3 (ya que tiene que ser mayor a 3), más nuestra variable de iteración
                cadena = self.cifradoEnString[i:j]
                # Buscamos apartir de j, ya que lo que antes de j ya fue leido
                if(self.cifradoEnString[j:].find(cadena)!= -1):
                    # La distancia es, justo donde se encuentra la cadena, restando los números que ya leimos (i) y sumando las letras extra que estamos tomando (j)
                    distance = self.cifradoEnString[j:].find(cadena)-i+j
                    if distance > 1:
                        factores = self.factoresPrimos(distance)
                        cadenasRepetidas.append(cadena)
                        factoresPrimos.append(factores)
                        distancias.append(distance)
                        print("| ", cadena,",", distance,",",  factores,",")
        return cadenasRepetidas


    def cifra(self):

        return

def main():
    print("1. Indice de Coindicencias y tabla de frecuencias:")
    cipher  = Vigenere()
    incidencias = cipher.numeroDeIncidencias()
    print("2. Número de alfabetos:")
    cipher.calculaNumeroDeAlfabetos(incidencias)
    print("3. Cadenas repetidas, de su distancia y los factores primos de esa distancia.:")
    #cipher.buscaRepetidas()
    print(cipher.texto)
    cipher.deleteRepeated()


if __name__ == '__main__':
    main()