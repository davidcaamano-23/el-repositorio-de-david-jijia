import tkinter as tk
from PIL import Image, ImageTk
#miscky herramienta misteriosa jejejejxd
class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora del kokun")
        self.root.configure(bg="#f0f0f0")

        self.entrada = tk.Entry(self.root, width=40, borderwidth=5,)
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (texto, fila, columna) in botones:
            if texto == '=':
                tk.Button(self.root, text=texto, padx=30, pady=20, font=("Arial", 14),
                          command=self.calcular).grid(row=fila, column=columna)
            elif texto == 'C':
                tk.Button(self.root, text=texto, padx=30, pady=20, font=("Arial", 14),
                          command=self.limpiar).grid(row=fila, column=columna, columnspan=4)
            else:
                tk.Button(self.root, text=texto, padx=30, pady=20, font=("Arial", 14),
                          command=lambda t=texto: self.agregar(t)).grid(row=fila, column=columna)

    def agregar(self, valor):
        self.entrada.insert(tk.END, valor)

    def limpiar(self):
        self.entrada.delete(0, tk.END)

    def calcular(self):
        try:
            expresion = self.entrada.get()
            resultado = eval(expresion)
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))

            if resultado == 2:
                self.mostrar_imagen("Imagen de WhatsApp 2025-10-13 a las 21.53.07_b55c63f4.jpg", "¡Harvard quiere conocerte!")
        except ZeroDivisionError:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Error")
            self.mostrar_imagen("images.jpeg", "No puedes dividir entre 0")
        except Exception:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "Error")

    def mostrar_imagen(self, ruta, titulo):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)

        try:
            img = Image.open(ruta)
            img = img.resize((400, 200))  # aca se puede ajustar el tamaño profe 
            img = ImageTk.PhotoImage(img)

            etiqueta = tk.Label(ventana, image=img)
            etiqueta.image = img  # Mantener referencia
            etiqueta.pack(padx=10, pady=10)

        except Exception as e:
            tk.Label(ventana, text="PENDEJO").pack(padx=10, pady=10)
            print("Error al cargar imagen:", e)

# POR ALGUNA RAZON NO QUIERE SALIR LA IMAGEN 
root = tk.Tk()
calculadora = Calculadora(root)
root.mainloop()
