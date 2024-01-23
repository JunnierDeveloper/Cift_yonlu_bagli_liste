import tkinter as tk
from tkinter import messagebox

class Dugum:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None
        self.onceki = None

bas = None

def basa_ekle(deger):
    global bas
    if bas is None:
        bas = Dugum(deger)
    else:
        yeni_dugum = Dugum(deger)
        yeni_dugum.sonraki = bas
        bas.onceki = yeni_dugum
        bas = yeni_dugum

def sona_ekle(deger):
    global bas
    if bas is None:
        bas = Dugum(deger)
    else:
        temp = bas
        yeni_dugum = Dugum(deger)
        while temp.sonraki is not None:
            temp = temp.sonraki
        yeni_dugum.onceki = temp
        temp.sonraki = yeni_dugum

def belirli_konuma_ekle(deger, konum):
    global bas
    temp = bas
    i = 1
    while i < konum and temp is not None:
        temp = temp.sonraki
        i += 1
    if temp is not None:
        deger.onceki = temp
        deger.sonraki = temp.sonraki
        if temp.sonraki is not None:
            temp.sonraki.onceki = deger
        temp.sonraki = deger

def cift_bagli_listeden_sil(deger):
    global bas
    temp = bas
    while temp is not None and temp.veri != deger:
        temp = temp.sonraki
    if temp is not None:
        if temp.onceki is not None:
            temp.onceki.sonraki = temp.sonraki
        if temp.sonraki is not None:
            temp.sonraki.onceki = temp.onceki
        if temp == bas:
            bas = temp.sonraki

def bul(veri):
    global bas
    bulunan_dugum = None
    temp = bas
    while temp is not None:
        if temp.veri == veri:
            bulunan_dugum = temp
            break
        temp = temp.sonraki
    return bulunan_dugum

def uye_mi(diger_dugum):
    global bas
    temp = bas
    while temp is not None and temp != diger_dugum:
        temp = temp.sonraki
    return temp == diger_dugum

def listeyi_yazdir():
    global bas
    temp = bas
    while temp is not None:
        listbox.insert(tk.END, temp.veri)
        temp = temp.sonraki

def onayla(secim):
    if secim == 1:
        deger = int(entry_deger.get())
        basa_ekle(deger)
    elif secim == 2:
        deger = int(entry_deger.get())
        sona_ekle(deger)
    elif secim == 3:
        deger = int(entry_deger.get())
        konum = int(entry_konum.get())
        belirli_konuma_ekle(Dugum(deger), konum)
    elif secim == 4:
        deger = int(entry_deger.get())
        cift_bagli_listeden_sil(deger)
    elif secim == 5:
        deger = int(entry_deger.get())
        sonuc = bul(deger)
        if sonuc is not None:
            messagebox.showinfo("Bulundu", f"{deger} bulundu.")
        else:
            messagebox.showinfo("Bulunamadı", f"{deger} bulunamadı.")
    elif secim == 6:
        listbox.delete(0, tk.END)  # Listbox'u temizle
        listeyi_yazdir()
    elif secim == 7:
        bas = None  # Tüm listeyi sil
        listbox.delete(0, tk.END)  # Listbox'u temizle
    elif secim == 0:
        root.destroy()

# Ana pencere oluşturma
root = tk.Tk() 
root.title("Çift Bağlı Liste Uygulaması")

root.configure(bg="black")


# Widget'ları oluşturma
label_deger = tk.Label(root, text="Değer:",bg="Blue",fg="White" ,)
entry_deger = tk.Entry(root)

label_konum = tk.Label(root, text="Konum:",bg="Blue",fg="White" ,)
entry_konum = tk.Entry(root)

button_basa_ekle = tk.Button(root, text="1 - Başa Ekle", bg="Blue",fg="White" ,command=lambda: onayla(1))
button_sona_ekle = tk.Button(root, text="2 - Sona Ekle",bg="Blue",fg="White" , command=lambda: onayla(2))
button_konuma_ekle = tk.Button(root, text="3 - Konuma Ekle", bg="Blue",fg="White" ,command=lambda: onayla(3))
button_sil = tk.Button(root, text="4 - Sil", bg="Blue",fg="White" ,command=lambda: onayla(4))
button_ara = tk.Button(root, text="5 - Ara",bg="Blue",fg="White" , command=lambda: onayla(5))
button_listeyi_goster = tk.Button(root, text="6- Listeyi Göster",bg="Blue",fg="White" , command=lambda: onayla(6))
button_tum_listeyi_sil = tk.Button(root, text="7 - Tüm Listeyi Sil",bg="Blue",fg="White" , command=lambda: onayla(7))
button_cikis = tk.Button(root, text="0 - Çıkış",bg="Blue",fg="White" , command=lambda: onayla(0))

# Listbox oluşturma
listbox = tk.Listbox(root, width=30, height=10)

# Widget'ları pencereye yerleştirme
label_deger.grid(row=1, column=0, padx=10, pady=5)
entry_deger.grid(row=1, column=1, padx=10, pady=5)
label_konum.grid(row=2, column=0, padx=10, pady=5)
entry_konum.grid(row=2, column=1, padx=10, pady=5)

button_basa_ekle.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
button_sona_ekle.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
button_konuma_ekle.grid(row=5, column=0, sticky="ew", padx=10, pady=5)
button_sil.grid(row=6, column=0, sticky="ew", padx=10, pady=5)
button_ara.grid(row=7, column=0, sticky="ew", padx=10, pady=5)
button_listeyi_goster.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
button_tum_listeyi_sil.grid(row=10, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
button_cikis.grid(row=11, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

listbox.grid(row=12, column=0, columnspan=2, pady=5)

root.mainloop()
