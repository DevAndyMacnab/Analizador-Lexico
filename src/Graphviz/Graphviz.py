import graphviz

def GraficandoDatos(texto, colorFondo, colorFuente, forma, nodos, respuestas):
    spanishColors={
        "Negro":"black", "Rojo":"red","Amarillo":"yellow","Verde":"green","Naranja":"orange","Morado":"purple","Blanco":"white"
        ,"Cafe":"brown","Azul":"blue","Gris":"gray","Rosado":"pink","Cian":"cian","Corinto":"maroon"
    }
    spanishFigures={
        "Cuadrado":"square","Circulo":"circle","Triangulo":"triangle","Trapezoide":"trapezoid","Estrella":"star","Rectangulo":"rectangle"
        ,"Octagono":"octagon","Corazon":"heart","Diamante":"diamond","Rombo":"rhombus","Hexagono":"hexagon","Elipse":"ellipse"
    }
        
    global operacion
    listaNodos = []
    
    d = graphviz.Digraph(filename="RESULTADOS_202111490.gv")
    with d.subgraph(name="cluster_0")as s:
        #Estilos para nuestro grafico
        s.attr(label=f"{texto}")
        s.attr(rank="same")    
        fondoColor=spanishColors.get(colorFondo,"black")
        fuenteColor=spanishColors.get(colorFuente,"white")
        setFigure=spanishFigures.get(forma,"circle")
        s.attr("node", shape=f"{setFigure}", style="filled",
               fillcolor=f"{fondoColor}", fontcolor=f"{fuenteColor}")
        
        global puntero
        puntero=0
        global anidadoValor1
        anidadoValor1=False
        global anidadoValor2
        anidadoValor2=False
        global identificador
        identificador=1
        
        while nodos:
            palabraClave=""
            
            nodo=nodos.pop(0)
            
            if nodo=="Operacion":   
                if anidadoValor2==True:
                    palabraClave=f"ID ->{identificador}\n "+ nodos.pop(0)
                    listaNodos.append(palabraClave)
                    puntero+=1
                    identificador+=1
                    
                    s.edge(listaNodos[puntero-3],listaNodos[puntero-1])
                    anidadoValor2=False
                    
                elif anidadoValor1==True:
                    palabraClave=f"ID -> {identificador}\n"+ nodos.pop(0)
                    listaNodos.append(palabraClave)
                    puntero+=1
                    identificador+=1
                    
                    s.edge(listaNodos[puntero-2],listaNodos[puntero-1])
                    anidadoValor1=False
                else:
                    palabraClave=f"ID -> {identificador}\n" +nodos.pop(0) +" \n "+ respuestas.pop(0)
                    listaNodos.append(palabraClave)
                    puntero+=1
                    identificador+=1
                               
            elif nodo=="Valor1":
                
                palabraClave=f"ID -> {identificador}\n"+str(nodos.pop(0))
                
                if "[" in palabraClave:
                    anidadoValor1=True
                    pass
                else:
                    listaNodos.append(palabraClave)
                    identificador+=1
                    puntero+=1
                    
                    s.edge(listaNodos[puntero-2],listaNodos[puntero-1])
                    
            elif nodo=="Valor2":
                
                palabraClave=f"ID -> {identificador}\n" +str(nodos.pop(0)) 
                if "[" in palabraClave:
                    anidadoValor2=True
                    pass
                     
                else:
                    listaNodos.append(palabraClave)
                    identificador+=1
                    puntero+=1
                    if "Seno" in listaNodos[puntero-3] or "Coseno" in listaNodos[puntero-3] or "Tangente" in listaNodos[puntero-3]:
                        s.edge(listaNodos[puntero-4],listaNodos[puntero-1])
                    else:
                        s.edge(listaNodos[puntero-3],listaNodos[puntero-1])
                                          
    s.attr(label=f"{texto}")
    d.view()

lista = ['Operacion', 'Suma', 'Valor1', 4.5, 'Valor2', 5.32, 'Operacion', 'Resta', 'Valor1', 4.5, 'Valor2', '[', 'Operacion',
         'Potencia', 'Valor1', 10, 'Valor2', 3, ']', 'Operacion', 'Suma', 'Valor1', '[', 'Operacion', 'Seno', 'Valor1', 90, ']', 'Valor2', 5.32]
respuestas = ["respuesta1", "respuesta2", "respuesta3","respuesta4","respuesta5"]
#GraficandoDatos("Texto de prueba", "Corinto", "asjdha", "Diamante", lista, respuestas)
