import tkinter as tk
import tkinter.messagebox as ms
import winsound as ws
import urllib.request as request
import urllib.parse as parse
import os


if not os.path.exists("Kare_kodlar"):
    os.mkdir("Kare_kodlar")
os.chdir("Kare_kodlar")
class pencere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kare kod programı")
        self.geometry("300x350")
        self.baslik = tk.Label(text="Kare kod programı", font=("Open Sans", "12", "bold"))
        self.baslik.grid(row=2, column=2)

        self.uyari = tk.Label(text="Bu işlem için internet bağlantısı gereklidir.")
        self.uyari.grid(row=3, column=2)

        self.tavsiye = tk.Label(text="İçerik:", font=("Open Sans", "10", "bold"))
        self.tavsiye.grid(row=4, column=1)

        self.veri = tk.Entry()
        self.veri.grid(row=4, column=2)

        self.tamam = tk.Button(text="Oluştur", command=self.olustur)
        self.tamam.grid(row=5, column=2)

    def olustur(self):
        try:
            local_veri = self.veri.get()
            veriler = {'size': '150x150',
                   'data': local_veri}
            params = parse.urlencode(veriler)
            api_link = "https://api.qrserver.com/v1/create-qr-code/?"+params
            request.urlretrieve(api_link, local_veri+".png")
        except:
            ws.MessageBeep()
            ms.showerror(title="Hata", message="Bir hata oluştu")
        else:
            self.basarili_mesaj = tk.Label(text="Kare kod oluşturuldu ve aşağıda:")
            self.basarili_mesaj.grid(row=7, column=2)

            self.resimd = tk.PhotoImage(file=local_veri+".png")
            self.resim = tk.Label(image=self.resimd)
            self.resim.grid(row=9, column=2)



nesne = pencere()
nesne.mainloop()
