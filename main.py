import tkinter as tk

window =tk.Tk()

def fechar(event=None):
    window.destroy()

window.overrideredirect(True)

window.attributes("-topmost", True)
window.geometry("300x100+500+300")

entry = tk.Entry(window)
entry.pack(expand=True, padx=20, pady=20)

entry.focus()

window.bind("<Escape>", fechar)


window.mainloop()