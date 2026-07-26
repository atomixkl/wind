import tkinter as tk

root = tk.Tk()
root.title("ABc")
root.geometry("1000x700")

top_label = tk.Label(root, text = "Гарного дня :3", font=("Arial", 20, "bold"))
top_label.pack(side="top", pady=10)

label = tk.Label(root, text = "ПТХ ПНХ", font=("Arial, 16"))
label.pack(pady=(250, 20))

button = tk.Button(root, text = "Запустити ядерку на москву", command = lambda: label.config(text="Ви успішно запустили ядерку на москву", font=("Arial, 16")))
button.pack(pady=0)













root.mainloop()