# Universidad de Guadalajara - Centro Universitario de Ciencias Exactas e Ingenierías.

## Actividad 7 - Entrega 1 Huffman | Alumno: Alan Marcel Arenas Venegas, Código: 219036383

## Introducción:
### ¿Qué es el algormitmo de Huffman?
El algoritmo de huffman provee un método que permite comprimir información mediante la recódificación de los bytes que lo componen. En particular, si los bytes que se van a comprimir están almacenados en un archivo, al recodificarlos con secuencias de bits más cortas diremos que lo comprimimos. La técnica consiste en asignar a cada byte del archivo que vamos a comprimir un código binario compuesto por una cantidad de bits tan corta como sea posible.

Osea, tenemos los carácteres O, M y C. La 'O' aparece 11 veces y la 'C' 7 veces. por tanto, significa que estos tienen la mayor probabilidad de ocurrecia. al momento de codificar cada carácter, sería algo así: O: 01, M: 001, C: 000. Se ordenan de menor a mayor codificación y quedaría algo así: 00001001, osease 1 byte para su almacenamiento.

El byte 00001001 ahora representa una secuencia de letras "C", "O" y "M", pero esta información sólo puede interpretarse si conoce el código binario utilizado para escribir el byte original. De lo contrario no puede haber información a restaurar. Para obtener estas combinaciones de bits únicas, el algoritmo de Huffman propone seguir una serie de pasos a través de los cuales obtendremos un árbol binario llamado “arbol Huffman”. Luego, las hojas del árbol representarán a los diferentes caracteres que aparecen en el archivo y los caminos que se deben recorrer para llegar a esas hojas representarán la nueva codificación del carácter.

## Objetivos:

En esta parte del entregable, tocaría implementar el FrontEnd del programa final, osease que va a capturar la frecuencia de carácteres del texto y los enlistará. Esto para que cuando se haga la parte del BackEnd, solamente quedaría agregarle la parte del Árbol de Huffman. Esto lo podemos desarrollar ya con la utilizada librería de Python, Tkinter, en la cual como se ha mencionado, es una librería de interfaz gráfica con multiples funciones como ya sea el filedialog, en la cual nos permitirá leer el archivo deseado para así poder hacer el cálculo de frecuencia de carácteres.

## Desarrollo:

### Entregable 1:
#### Implementación base para la interfaz:
La implementación base sería que es lo que cada ventana y/o función hará. Entonces, al momento de iniciar el código, le pedirá al usuario 3 opciones (2 de estas están deshabilitadas, ya que eso sería para el siguiente entregable.). La primera, sería el elegir (exáminar) el documento para así calcular la frecuencia.

#### main:
winPrin = tk.Tk()
botonAbrir = tk.Button(winPrin, text="Examinar", font="arial 10" , bg="#53d1e6", command=examinar)
botonAbrir.pack(pady=5)

Esto, llevaría a la función de 'examinar'. En la cual, este tiene 4 funciones dentro (abrir, analizar, calcuFrecuencia y mostrarResultados)

Para la parte de 'abrir', simplemente abre el archivo para su lectura y este hace una comparación si el archivo se puede leer o no.

#### examinar - abrir()

def abrir():

    file_path = tk.filedialog.askopenfilename()    #Función para leer el archivo seleccionado
        if file_path:                              #Comparación si el archivo puede ser leído
            analizar(file_path)                    #Si se puede leer, pasa a la función analizar.

#### examinar - analizar(file_path)

def analizar(file_path):

    try:
        with open(file_path, 'r') as file:
            contenido = file.read()                  #Lee todo el contenido del archivo en una cadena
            frecuencia = calcuFrecuencia(contenido)  #Calcula la frecuencia de caracteres en el contenido
            mostrarResultados(frecuencia)            #Muestra los resultados de frecuencia
    except FileExistsError:                          #Función si se produjo un error al momento de leer el archivo.
        print("Archivo no encontrado")

#### examinar - calcuFrecuencia(contenido)

def calcuFrecuencia(contenido):

    contador = Counter(contenido.lower())           #Cuenta la frecuencia de cada carácter del contenido
    frecuencia = sorted(contador.items())           #Ordena los elementos contados en orden alfabético
    return frecuencia                               #Devuelvas la lista de frecuencia

Y para la función de mostrar resultados, simplemente es una ventana con un ciclo for, para todas las letras que hay en la cadena de texto.

## Conclusión:

### Entregable 1:
En esta parte de la actividad se me hizo facíl, ya que es lo que más hemos trabajado en el semestre. Acerca de la interfaz, como leer un archivo y que haga sus operaciones. Agregué cosas extras como por ejemplo el try y except, por si no se llegara a leer el archivo correctamente. Una cosa que no he trabajado, es la parte de 'Counter' ya que no lo hemos trabajado anteriormente en el semestre.

## Referencias:

de Huffman, C. de A. M. el A. (s/f). Módulo 3 / Aplicación práctica. Com.mx. Recuperado el 24 de abril de 2024, de https://libroweb.alfaomega.com.mx/book/393/free/data/Capitulos/cap16.pdf
