import tkinter as tk
from tkinter import filedialog
import heapq
import os

#* QUE SE AGREGÓ/MODIFICÓ
# COMENTARIOS NORMALES/ORIGINALES

#* Nodo para el árbol de Huffman
class NodoHuffman:
    #* Constructor de la clase
    def __init__(self, caracter, frecuencia):
        #* Caracter representado por el nodo
        self.caracter = caracter
        #* Frecuencia representado por el nodo
        self.frecuencia = frecuencia
        #* Referencia al nodo hijo izquierdo
        self.izquierda = None
        #* Referencia al nodo hijo derecho
        self.derecha = None

    #* Método para comparar nodos basado en sus frecuencias
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

#* Función para construir el árbol de Huffman
def construir_arbol_huffman(diccionario):
    heap = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in diccionario.items()]
    #* Convierte la lista en un heap (cola de prioridad)
    heapq.heapify(heap)
    while len(heap) > 1:
        izquierda = heapq.heappop(heap)
        derecha = heapq.heappop(heap)
        nodo = NodoHuffman(None, izquierda.frecuencia + derecha.frecuencia)
        nodo.izquierda = izquierda
        nodo.derecha = derecha
        heapq.heappush(heap, nodo)
    #* Retorna la raíz del árbol de Huffman
    return heap[0]

#* Función para generar el código Huffman recursivamente
def generar_codigos_huffman(arbol, codigo_actual, codigos):
    #* Comparación de si el arbol tiene carácteres
    if arbol.caracter is not None:
        #* Asigna el codigo actual al caracter
        codigos[arbol.caracter] = codigo_actual
        return
    #* Si el nodo actual no tiene un caracter asignado, continúa recursivamente con los nodos izquierdo y derecho
    generar_codigos_huffman(arbol.izquierda, codigo_actual + '0', codigos)
    generar_codigos_huffman(arbol.derecha, codigo_actual + '1', codigos)

#* Función para comprimir el archivo utilizando el árbol de Huffman
def comprimir_archivo(archivo):
    #* Condición si hay un archivo abierto para poder comprimir (en .txt a .bat)
    with open(archivo, 'r') as f:
        #* Lee el archivo
        contenido = f.read()
        #* Diccionario para las frecuencias
        frecuencias = {}
        for caracter in contenido:
            caracter = caracter.lower()
            #* Verifica si el caracter es una letra o un espacio
            if caracter.isalpha() or caracter.isspace():
                #* Si el caracter ya está en el diccionario, incrementa su frecuencia
                if caracter in frecuencias:
                    frecuencias[caracter] += 1
                #* Si no está en el diccionario, lo agrega con frecuencia 1
                else:
                    frecuencias[caracter] = 1
        #* Construye el árbol de Huffman
        arbol = construir_arbol_huffman(frecuencias)
        codigos = {}
        generar_codigos_huffman(arbol, '', codigos)
        #* Agrega la extensión .bat
        archivo_comprimido = archivo + '.bat'
        with open(archivo_comprimido, 'w') as f_comp:
            for caracter in contenido:
                caracter = caracter.lower()
                #* Escribe el contenido en el archivo
                if caracter in codigos:
                    f_comp.write(codigos[caracter])
        return archivo_comprimido

#* Función para descomprimir el archivo comprimido
def descomprimir_archivo(archivo_comprimido):
    #* Condición si hay un archivo abierto para poder descomprimir (en .bat a .txt)
    with open(archivo_comprimido, 'r') as f:
        #* Lectura del contenido del archivo
        contenido = f.read()
        #* Convertir de .bat a .txt
        archivo_descomprimido = archivo_comprimido.replace('.bat', '.txt')
        #* Escribe el contenido en el archivo
        with open(archivo_descomprimido, 'w') as f_descomp:
            f_descomp.write(contenido)
        return archivo_descomprimido

# Función para leer el archivo y contar los caracteres
def leer_archivo(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()
        contar_carcteres(contenido)

# Función para contar cada caracter y mostrar la frecuencia
def contar_carcteres(contenido):
    dic = {}
    for caracter in contenido:
        caracter = caracter.lower()
        if caracter.isalpha() or caracter.isspace():
            if caracter in dic:
                dic[caracter] += 1
            else:
                dic[caracter] = 1
    if dic is not None:
        mostrar_resultados(dic)
    print(dic)

#* Función para mostrar los resultados de la frecuencia de caracteres
#* Se movió a función dependiente, en vez de condición.
def mostrar_resultados(dic):
    res = tk.Tk()
    res.geometry('500x100')
    res.title('Resultados')
    texto = tk.Text(res)
    texto.insert(tk.END, dic)
    texto.pack()
    res.mainloop()

# Frontend
def ventana_main():
    root = tk.Tk()
    root.geometry('300x100')
    #* Cambió el nombre de la ventana a 'Algoritmo Huffman' para la identificación
    root.title('Algoritmo Huffman')

    # Cuando se llama esta funcion abre el file manager para poder selecionar el archivo
    def abrir_filemanager():
        archivo = filedialog.askopenfilename()
        archivo_entry.delete(0, tk.END)
        archivo_entry.insert(0, archivo)
        leer_archivo(archivo) # Pasa como argumento el archivo seleccionado 

    #* Agregado la función comprimir
    def comprimir():
        archivo = archivo_entry.get()
        #* Comparación si hay un archivo cargado
        if archivo:
            #* Llamada a la función de comprimir
            archivo_comprimido = comprimir_archivo(archivo)
            #* Ya no aparece como ventana, si no como mensaje de advertencia con su dirección
            #* (NUEVO)
            tk.messagebox.showinfo("Comprimir", f"Archivo comprimido como: {archivo_comprimido}")

    #* Agregado la función descomprimir
    def descomprimir():
        archivo = archivo_entry.get()
        #* Comparación si hay un archivo cargado y con terminación '.bat'
        if archivo and archivo.endswith('.bat'):
            archivo_descomprimido = descomprimir_archivo(archivo)
            #* Ya no aparece como ventana, si no como mensaje de advertencia con su dirección
            #* (NUEVO)
            tk.messagebox.showinfo("Descomprimir", f"Archivo descomprimido como: {archivo_descomprimido}")

    main_frame = tk.Frame(master=root) # Frame que contiene todo lo que hay en la ventana 
    main_frame.pack(padx=8, pady=8)

    archivo_frame = tk.Frame(master=main_frame) # Frame que contiene el lable y la caja de texto sobre el archivo
    archivo_frame.pack(padx=8, pady=8)

    archivo_lbl = tk.Label(master=archivo_frame, text='Archivo: ')
    archivo_lbl.grid(column=0, row=0)

    archivo_entry = tk.Entry(master=archivo_frame, width=35)
    archivo_entry.grid(column=1, row=0)

    botones_frame = tk.Frame(master=main_frame) # Frame que contiene todos los botones
    botones_frame.pack(padx=8, pady=8)

    #* Cambió el nombre del botón 'examinar' a 'btnExam'
    btnExam = tk.Button(master=botones_frame, text='Examinar', command=abrir_filemanager)
    btnExam.grid(padx=8, pady=4, column=0, row=0)

    #* Cambió el nombre del botón 'comprimir' a 'btnComp' para la función 'comprimir'
    btnComp = tk.Button(master=botones_frame, text='Comprimir', command=comprimir)
    btnComp.grid(padx=8, pady=4, column=1, row=0)

    #* Cambió el nombre del botón 'descomprimir' a 'btnDesc'  para la función 'descomprimir'
    btnDesc = tk.Button(master=botones_frame, text='Descomprimir', command=descomprimir)
    btnDesc.grid(padx=8, pady=4, column=2, row=0)

    root.mainloop()

if __name__ == '__main__':
    ventana_main()
