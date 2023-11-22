import tkinter as tk
from tkinter import ttk

class MarksCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Notas")
        
        # Estilo
        style = ttk.Style()
        style.theme_use("clam")
        
        # Etiquetas y Entradas de texto
        ttk.Label(root, text="Ingresa las notas de los 6 sujetos", font=("Helvetica", 12)).grid(row=0, column=0, columnspan=2, pady=10)

        self.subject_entries = []
        for i in range(1, 7):
            ttk.Label(root, text=f"Sujeto {i}:").grid(row=i, column=0, pady=5, padx=10, sticky=tk.E)
            entry = ttk.Entry(root)
            entry.grid(row=i, column=1, pady=5, padx=10, sticky=tk.W)
            self.subject_entries.append(entry)
        
        # Botón de calcular
        ttk.Button(root, text="Calcular", command=self.calculate).grid(row=7, column=0, columnspan=2, pady=10)
        
        # Etiqueta de resultado
        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=8, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
            # Obtener las notas de las entradas de texto
            marks = [float(entry.get()) for entry in self.subject_entries]
            
            # Calcular el total y el promedio
            total = sum(marks)
            average = total / len(marks)
            
            # Mostrar el resultado
            result_text = f"Total de Notas: {total:.2f}\nPromedio de Notas: {average:.2f}"
            self.result_label.config(text=result_text)
        except ValueError:
            self.result_label.config(text="Por favor, ingresa valores numéricos válidos para todas las asignaturas")

if __name__ == "__main__":
    root = tk.Tk()
    app = MarksCalculatorApp(root)
    root.mainloop()

