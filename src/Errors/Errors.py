from controllers.Lexema import Lexema
from controllers.abstract import Expression
def ErrorFile(listaErrores):
    contador=1
    texto="{"
    archivo=open("static/ERRORES_202111490.json","w")
    archivo.write("")
    #Aca generamos el archivo JSON con los errores del archivo ingresado por el usuario
    for element in listaErrores:
        texto+="{"
        texto+=f'''
        "No.":{contador}
        "Descripcion-Token":
        '''
        texto+="{"
        texto+=f'''
            "Lexema":{element.lexema}
            "Tipo":Error Léxico
            "Columna":{element.columna}
            "Fila":{element.fila}
        '''
        texto+="}"
        texto+="},"
        contador+=1
    texto+="}"
    contador=0
    listaErrores=[]
    archivo.write(texto)
    archivo.close           
    pass


 
