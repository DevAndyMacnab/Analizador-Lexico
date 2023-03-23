from controllers.Trigonometrica import Trigonometricas
from controllers.abstract import Expression
from controllers.Numero import Numero
from controllers.Lexema import Lexema
from controllers.Aritmetica import Aritmetica
from Errors.Errors import ErrorFile
reserved=['Operacion','Valor1','Valor2','Suma','Resta','Multiplicacion','Division','Potencia','Raiz','Inverso','Seno','Coseno','Tangente','Modulo','Texto'
          ,'Color-Fondo-Nodo','Color-Fuente-Nodo','Forma-Nodo',',','.',':','[',']','{','}'," ","\n" ]

lexemas=reserved
global nLinea
global nColumna
global instrucciones
global listaLexemas
global listaErrores
listaErrores=[]
instrucciones=[]
listaLexemas=[]
nLinea=0
nColumna=0


#Esta funcion recibe la cadena que le pasamos como parametro 
def Instruccion (cadena):
    
    global nLinea
    global nColumna
    global listaLexemas
    
    lexema=''
    puntero=0
    
    while cadena:
        char= cadena[puntero]
        puntero+=1
        
        if char=='\"':
            lexema, cadena= buildLexeme(cadena[puntero:])
            if lexema and cadena:
                nColumna+=1
                #Aqui armo lexema como clase
                l=Lexema(lexema,nLinea,nColumna)
                
                listaLexemas.append(l)
                nColumna+=len(lexema)+1
                puntero=0
                
        elif char.isdigit():
            token,cadena=ArmarNumero(cadena)
            if token and cadena:
                nColumna+=1
                #Aqui agregamos el lexema a la list de lexemas
                n= Numero(token,nLinea,nColumna)
                listaLexemas.append(n)
                nColumna+=len(str(token))+1
                puntero=0 
                     
        elif char=='[' or char==']':
            #Aqui armo mi lexema de clase
            c=Lexema(char,nLinea,nColumna)
            listaLexemas.append(c)
            cadena=cadena[1:]
            puntero=0
            nColumna+=1
                
        elif char=='\t':
            nColumna+=4
            cadena=cadena[4:]
            puntero=0
        elif char=='\n':
            cadena = cadena[1:]
            puntero=0
            nLinea+=1
            nColumna=1
        else:
            if char not in reserved:
                error=Lexema(char,nLinea+1,nColumna)
                listaErrores.append(error)
                
            cadena=cadena[1:]
            puntero=0
            nColumna+=1
    
    ErrorFile(listaErrores)        
    return listaLexemas
                           
def buildLexeme(cadena):
    global nLinea
    global nColumna
    global listaLexemas
    lexema=''
    puntero=''
    
    for char in cadena:
        puntero+=char
        if char=='\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema+=char
    return None, None
            
def ArmarNumero(cadena):
    numero=''
    puntero=''
    decimal=False
    for char in cadena:
        puntero+=char
        if char=='.':
            decimal=True
        if char=='\"' or char ==' ' or char =='\n'or char =='\t':
            if decimal:
                return float(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]
        else:
            numero += char
    return None, None 
                                
def operar():
    global listaLexemas
    global instrucciones
    operacion=""
    n1=""
    n2=""
   
    while listaLexemas:
        
        lexema=listaLexemas.pop(0)
        
        if lexema.operar(None)=="Operacion":
            operacion=listaLexemas.pop(0)
                    
        elif lexema.operar(None)=="Valor1":
            n1=listaLexemas.pop(0)
            if n1.operar(None)=='[':
                n1=operar()
           
        elif lexema.operar(None)=="Valor2":
            n2=listaLexemas.pop(0)
            if n2.operar(None)=='[':
                n2=operar()
                    
        if operacion and n1 and n2:
            return (Aritmetica(n1,n2,operacion,f'Inicio:{operacion.getFila()}:{operacion.getColumna()}',f'Fin:{n2.getFila()}:{n2.getColumna()}'))
        
        
        elif operacion and n1 and operacion.operar(None)==("Seno"or "Coseno" or "Tangente"):
            return (Trigonometricas(n1,operacion,f'Inicio:{operacion.getFila()}:{operacion.getColumna()}',f'Fin:{n1.getFila()}:{n1.getColumna()}'))
    return None

def operar_():
    global instrucciones
    instrucciones=[]
    while True:
        operacion=operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
        
    
    return instrucciones

