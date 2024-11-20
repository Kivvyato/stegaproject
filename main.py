import tkinter as tk
import texttobinary
from texttobinary import text_binary
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from texttobinary import array

# Función para convertir un valor RGB a su representación binaria
def rgb_to_bin(r, g, b):
    return format(r, '08b'), format(g, '08b'), format(b, '08b')

# Número de píxeles a procesar
PIXELS_TO_PROCESS = 100

def process_image():
    username = text_entry.get()
    text_binary(username)
    
    if not username:  # Si no se ingresa un nombre
        messagebox.showwarning("Please enter valid text to encode.")
        return
    
    # Abrir un cuadro de diálogo para seleccionar un archivo de imagen
    file_path = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    
    if not file_path:
        messagebox.showwarning("No archive selected.")
        return

    try:
        # Abrir la imagen seleccionada
        image = Image.open(file_path)
        
        # Convertir la imagen a RGB (por si está en otro modo como RGBA, P, etc.)
        image = image.convert('RGB')
        
        # Obtener los datos de los píxeles como una lista de tuplas (R, G, B)
        pixels = list(image.getdata())
        
        # Abrir el archivo de texto para escribir los resultados
        with open("text.txt", "w") as f:
            # Escribir los primeros 100 píxeles en su formato binario y RGB
            for i in range(PIXELS_TO_PROCESS):
                r, g, b = pixels[i]
                r_bin, g_bin, b_bin = rgb_to_bin(r, g, b)
                
                # Eliminar los últimos dos bits de cada componente de color
                r_bin = r_bin[:-2]  # Remover los últimos dos bits
                g_bin = g_bin[:-2]  # Remover los últimos dos bits
                b_bin = b_bin[:-2]  # Remover los últimos dos bits
                
                # Escribir los valores binarios modificados de RGB sin los últimos dos bits
                f.write(f"{i} : R={r_bin} G={g_bin} B={b_bin}")
                f.write(f' R={r}, G={g}, B={b}\n')
                f.write("             \n")  # Espacio adicional como en el original
                # Convertir la imagen a 1-bit (blanco y negro)

        bw_image = image.convert('1')
        
        # Mostrar la imagen original y la imagen en blanco y negro
        bw_image.show()
        image.show()
        
        messagebox.showinfo("Proceso completado")
    
    except Exception as e:
        # Capturar y mostrar errores al abrir la imagen
        messagebox.showerror("Error", f"Error al procesar la imagen: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Procesar Imagen")

# Crear y colocar los widgets
text_label = tk.Label(root, text="Insert text:")
text_label.grid(row=0, column=0, padx=10, pady=10)

text_entry = tk.Entry(root)
text_entry.grid(row=0, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Process Image", command=process_image)
submit_button.grid(row=1, columnspan=2, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()
