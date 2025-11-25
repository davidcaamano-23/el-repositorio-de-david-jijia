import tkinter as tk
from tkinter import ttk, messagebox
import calendar

def generar_turnos():
    lista.delete(0, tk.END)
    try:
        año = int(año_box.get())
        mes = mes_box.current() + 1
        inicio = int(inicio_entry.get())
        termino = int(termino_entry.get())
        modalidad = modo_box.get()

        # Definir los dias de trabajo 
        if modalidad == "4x4": t, d = 4, 4
        elif modalidad == "7x7": t, d = 7, 7
        elif modalidad == "14x14": t, d = 14, 14
        else: return messagebox.showerror("Error", "Modalidad inválida")

        dia_actual = inicio
        trabajando = True
        while dia_actual <= termino:
            rango = t if trabajando else d
            for _ in range(rango):
                if dia_actual > termino: break
                tipo = "TRABAJO" if trabajando else "DESCANSO"
                lista.insert(tk.END, f"{dia_actual:02d}/{mes:02d}/{año} - {tipo}")
                dia_actual += 1
            trabajando = not trabajando
    except:
        messagebox.showerror("Error", "Ingrese valores válidos")

# --- principal ventana aca xd ---
v = tk.Tk()
v.title("Planificador de Turnos")
v.geometry("400x500")
v.configure(bg="gold")  # fondo rarito jejejeje

fuente = ("Roma", 12)  # Fuente Roma

# los meses y los años 
tk.Label(v, text="Mes:", bg="skyblue", font=fuente).pack()
mes_box = ttk.Combobox(v, values=list(calendar.month_name[1:]), width=10, font=fuente)
mes_box.current(0); mes_box.pack()

tk.Label(v, text="Año:", bg="white", font=fuente).pack()
año_box = ttk.Combobox(v, values=[2024,2025,2026], width=6, font=fuente)
año_box.set(2025); año_box.pack()

# desde el dia 1 hasta el dia del termino como dijo mi abuelito 
tk.Label(v, text="Día de inicio del turno:", bg="pink", font=fuente).pack()
inicio_entry = tk.Entry(v, width=5, font=fuente); inicio_entry.insert(0,"1"); inicio_entry.pack()

tk.Label(v, text="Día de término del turno:", bg="blue", font=fuente).pack()
termino_entry = tk.Entry(v, width=5, font=fuente); termino_entry.insert(0,"30"); termino_entry.pack()

# Modalidad
tk.Label(v, text="Modalidad de turno:", bg="yellow", font=fuente).pack()
modo_box = ttk.Combobox(v, values=["4x4","7x7","14x14"], width=6, font=fuente)
modo_box.current(0); modo_box.pack()

# el poderosisimo boton 
tk.Button(v, text="Generar Turnos", command=generar_turnos, bg="orange", font=fuente).pack(pady=10)

# Listbox para mostrar resultados, profe sin este espoiler estaba perdido que nos dios en la clase :)
lista = tk.Listbox(v, width=40, height=15, font=fuente)
lista.pack(pady=10)

# Botón salir
tk.Button(v, text="Salir", command=v.destroy, bg="red", font=fuente).pack(pady=5)
#es muy basico si el planificador profe xD
v.mainloop()


