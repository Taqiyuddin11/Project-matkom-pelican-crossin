import tkinter as tk  

def ubah_lampu():
    global lampu_sekarang, override
    if override:  
        canvas.itemconfig(lampu_merah, fill="red")
        canvas.itemconfig(lampu_hijau, fill="gray")
        canvas.itemconfig(lampu_kuning, fill="gray")
        root.after(15000, reset_override)  
    else:  
        if lampu_sekarang == "merah":
            canvas.itemconfig(lampu_merah, fill="gray")
            canvas.itemconfig(lampu_hijau, fill="green")
            lampu_sekarang = "hijau"
        elif lampu_sekarang == "hijau":
            canvas.itemconfig(lampu_hijau, fill="gray")
            canvas.itemconfig(lampu_kuning, fill="yellow")
            lampu_sekarang = "kuning"
        elif lampu_sekarang == "kuning":
            canvas.itemconfig(lampu_kuning, fill="gray")
            canvas.itemconfig(lampu_merah, fill="red")
            lampu_sekarang = "merah"
        root.after(5000, ubah_lampu)  

def reset_override():
    global override
    override = False  
    canvas.itemconfig(lampu_kuning, fill="gray")
    canvas.itemconfig(lampu_merah, fill="red")
    lampu_sekarang = "merah"
    root.after(5000, ubah_lampu)  

def penyebrangan():
    global override
    override = True
    ubah_lampu()

root = tk.Tk()
root.title("Lampu Lalu Lintas")

canvas = tk.Canvas(root, width=200, height=400, bg="white")
canvas.pack()

canvas.create_rectangle(50, 50, 150, 350, fill="black")  
lampu_merah = canvas.create_oval(60, 60, 140, 140, fill="red")
lampu_kuning = canvas.create_oval(60, 160, 140, 240, fill="gray")
lampu_hijau = canvas.create_oval(60, 260, 140, 340, fill="gray")

lampu_sekarang = "merah"  
override = False  

tombol_penyebrangan = tk.Button(root, text="Penyebrangan", command=penyebrangan)
tombol_penyebrangan.pack(pady=20)

root.after(5000, ubah_lampu)
root.mainloop()