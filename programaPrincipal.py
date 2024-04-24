import tkinter as tk
from tkinter import filedialog
from collections import Counter     #Librería para contador de carácteres

def examinar():
    def abrir():
        file_path = tk.filedialog.askopenfilename()     #Función para leer el archivo seleccionado
        if file_path:                                   #Comparación si el archivo puede ser leído
            analizar(file_path)                         #Si se puede leer, pasa a la función analizar.
    
    def analizar(file_path):
        try:
            with open(file_path, 'r') as file:
                contenido = file.read()                     #Lee todo el contenido del archivo en una cadena
                frecuencia = calcuFrecuencia(contenido)     #Calcula la frecuencia de caracteres en el contenido
                mostrarResultados(frecuencia)               #Muestra los resultados de frecuencia
        except FileExistsError:                             #Función si se produjo un error al momento de leer el archivo.
            print("Archivo no encontrado")
    
    def calcuFrecuencia(contenido):
        contador = Counter(contenido.lower())               #Cuenta la frecuencia de cada carácter del contenido
        frecuencia = sorted(contador.items())               #Ordena los elementos contados en orden alfabético
        return frecuencia                                   #Devuelvas la lista de frecuencia
    
    def mostrarResultados(frecuencia):
        winRes = tk.Tk()
        winRes.title("Resultados obtenidos")
        winRes.geometry('500x700')

        texto = tk.Label(winRes, text="Frecuencia de carácteres:", font="arial 14 bold")
        texto.pack(padx=20,pady=20)
        
        for letra, frec in frecuencia:
            texto = tk.Label(winRes, text=f"{letra}: {frec}", font="arial 10")          #Ciclo para imprimir todas las letras que hay en la cadena y cuantas hay.
            texto.pack()

        winRes.mainloop()
    
    winArch = tk.Tk()
    winArch.title("Abrir archivo")
    winArch.geometry('500x300')

    texto = tk.Label(winArch, text="Abrir y Examinar tu cadena de texto", font="arial 14 bold")
    texto.pack(padx=20,pady=20)
    texto = tk.Label(winArch, text="Selecciona tu archivo", font="arial 11 bold italic")
    texto.pack(pady=10)

    btnAbrir = tk.Button(winArch, text="Abrir archivo", bg="#53d1e6" , font="arial 10",  command=abrir)     #Botón para llamar a 'abrir' archivo.
    btnAbrir.pack(pady=10)

    winArch.mainloop()

    

def comprimir():        #Se puede poner aqui la parte de comprimir del algoritmo Backend
    def saveComp():
        compFile = tk.filedialog.asksaveasfile()    #Funcion para guardar archivo (incompleto)
    winComp = tk.Tk()
    winComp.title("Comprimir cadena")
    winComp.geometry('500x300')

    texto = tk.Label(winComp, text="Comprimir cadena de texto", font="arial 14 bold")
    texto.pack(padx=20,pady=20)
    texto = tk.Label(winComp, text="Elige tu ubicación y nombre para el archivo", font="arial 11 bold italic")
    texto.pack(pady=10)

    btnComp = tk.Button(winComp, text="Guardar", font="arial 10", command=saveComp)     #Botón para llamar a salvar archivo comprimido
    btnComp.pack(pady=5)

    winComp.mainloop()

def descomprimir():         #Se puede poner aqui la parte de descomprimir del algoritmo Backend
    def saveDesc():
        descFile = tk.filedialog.asksaveasfile()        #Funcion para guardar archivo (incompleto)

    winDesc = tk.Tk()
    winDesc.title("Descomprimir Cadena")
    winDesc.geometry('500x300')

    texto = tk.Label(winDesc, text="Descomprimir cadena de texto", font="arial 14 bold")
    texto.pack(padx=20,pady=20)
    texto = tk.Label(winDesc, text="Elige tu ubicación y nombre para el archivo", font="arial 11 bold italic")
    texto.pack(pady=10)

    btnDesc = tk.Button(winDesc, text="Guardar", font="arial 10", command=saveDesc)     #Botón para llamar a salvar archivo descomprimido
    btnDesc.pack(pady=5)

    winDesc.mainloop()

def main():             #Funcion principal o main
    winPrin = tk.Tk()
    winPrin.title("Act 7 - Compresión de Huffman")
    winPrin.geometry('500x300')
    
    texto = tk.Label(winPrin, text="Algoritmo de Huffman", font="arial 14 bold")
    texto.pack(padx=20,pady=20)
    texto = tk.Label(winPrin, text="¿Que quieres hacer?", font="arial 11 bold italic")
    texto.pack(pady=10)

    botonAbrir = tk.Button(winPrin, text="Examinar", font="arial 10" , bg="#53d1e6", command=examinar)       #Botón que llama a 'examinar'
    botonAbrir.pack(pady=5)

    botonComprimir = tk.Button(winPrin, text="Comprimir", font="arial 10" , bg="#343951", fg="white" , command=comprimir)       #Botón que llama a 'comprimir'
    botonComprimir.pack(pady=5)

    botonDescomprimir = tk.Button(winPrin, text="Descomprimir", font="arial 10" , bg="#343951", fg="white" , command=descomprimir)      #Botón que llama a 'descomprimir'
    botonDescomprimir.pack(pady=5)

    winPrin.mainloop()

if __name__ == "__main__":
    main()