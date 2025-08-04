import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import obtener_conexion
from query import ordenes_cliente

def buscar(event=None):
    nombre = entry.get().strip()
    try:
        conn = obtener_conexion()
        df = ordenes_cliente(conn, nombre)
        tree.delete(*tree.get_children()) 
        for _, row in df.iterrows():
            tree.insert("", "end", values=(row.EMAIL, row.FCLIENTE, row.Cuit, row.Fecha, row.Factura, row.Total))
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

#INTERFAZ TKINTER
root = tk.Tk()
root.title("Órdenes del Cliente")
root.geometry("800x300")


tk.Label(root, text="Nombre del cliente:").pack(pady=5)

entry = tk.Entry(root, width=25, font=("Arial",12))
entry.pack()
entry.bind("<Return>", buscar)

tk.Button(root, text="Buscar", command=buscar).pack(pady=5)

columns = ["Email", "Cliente", "Cuit", "Fecha", "Factura", "Total"]

tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    
tree.pack(fill=tk.BOTH, expand=True)

root.mainloop()
