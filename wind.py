import tkinter as tk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(BASE_DIR, "icon", "1388012245161869312.png")

root = tk.Tk()
root.title("Симулятор знищення москви")
root.geometry("1000x700")
root.config(bg="#070707")

icon = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon)

clicks = 0

def launch():
    global clicks
    clicks += 1
    label.config(text=f"Ви успішно запустили ядерку на москву x{clicks} раз(-ів)!", font=("Arial", 16,), fg="white", bg="#070707")

top_label = tk.Label(root, text = "Гарного дня :3", font=("Arial", 20, "bold"), fg="white", bg="#070707")
top_label.pack(side="top", pady=10)

label = tk.Label(root, text = "ПТХ ПНХ", font=("Arial, 16"), fg="white", bg="#070707")
label.pack(pady=(250, 20))

button = tk.Button(root, text = "Запустити ядерку на москву", bg="red", fg="white", command=launch)
button.pack(pady=0)













root.mainloop()