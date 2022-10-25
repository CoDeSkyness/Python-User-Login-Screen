
# (TR) -PYTHON İLE KULLANICI GİRİŞ DOĞRULAMA PROGRAMI
# (EN) Making a user login screen over the form with Python language

import tkinter as tk  # Arayüz Kütüphanesi

arayuz = tk.Tk()
arayuz.title("Kullanıcı Giriş Ekranı")  # Arayüzün Görünen İsmini Değiştirir.
arayuz.geometry("300x200")  # Oluşturulan Arayüzün Boyutunu Belirler.

isim = "Python"  # Username
sifre = "123"  # Password


# arayüze label ekler ve label'a isim verir.
kullanıcı = tk.Label(text="Kullanıcı Adı: ")
kullanıcı.place(x=10, y=10)  # arayüze eklenen label'in konumunu belirler.

kulladi = tk.StringVar()  # textbox a string atar
# TextBox Ekler ve String Ekler.
kullanıcı_giris = tk.Entry(textvariable=kulladi)
kullanıcı_giris.place(x=100, y=10)  # TextBoxun Konumunu Belirler.


kullanıcı = tk.Label(text="Şifre Giriniz: ")
kullanıcı.place(x=10, y=40)

ksifre = tk.StringVar()
kullanıcı_giris = tk.Entry(textvariable=ksifre)
kullanıcı_giris.place(x=100, y=40)


giris_kontrol = tk.Label(text="Kontrol", font="Verdana 10 bold")
giris_kontrol.place(x=10, y=160)


def giris_komut():  # Kullanıcı Giriş Fonksiyonu
    kulad = kulladi.get()
    sif = ksifre.get()
    # Kullanıcı Adı Ve Şifreyi Yazdırır.
    print("Kullanıcı Adı: "+kulad, "\n", "Şifre: "+sif)
    if kulad == isim and sif == sifre:
        giris_kontrol.config(text="Giriş Başarılı...", fg="green")
    else:
        giris_kontrol.config(
            text="Hatalı Kullanıcı Adı veya Şifre..", fg="red")


# arayüze buton ekler ve isimlendirir.
giris = tk.Button(text="Giriş Yap", command=giris_komut)
giris.place(x=150, y=80)  # butonun konumunu belirler.


arayuz.mainloop()  # Arayüz
