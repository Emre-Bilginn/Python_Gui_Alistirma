from re import S
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QMessageBox, QFileDialog
import sqlite3

class Benim_Benzerlik_Yontemi(QWidget):
    def __init__(self):
        super().__init__()
        self.ozellikEkle()
        self.ekOzellikEkle()

    def ozellikEkle(self):
        self.resize(600,200)
        self.move(700,300)
        self.setWindowTitle("Benim Benzerlik Yöntemi ile Karşılaştırma")
    
    def ekOzellikEkle(self):
        self.metin1_label = QLabel("Birinci Metin",self)
        self.metin1_label.setGeometry(20,20,100,20)

        self.metin1_textbox = QLineEdit(self)
        self.metin1_textbox.setGeometry(120,20,200,20)

        self.metin1_sec_button = QPushButton("Dosya Seç",self)
        self.metin1_sec_button.setGeometry(330,20,70,20)
        self.metin1_sec_button.clicked.connect(self.metin1_sec)


        self.metin1_labe2 = QLabel("İkinci Metin",self)
        self.metin1_labe2.setGeometry(20,50,100,20)

        self.metin2_textbox = QLineEdit(self)
        self.metin2_textbox.setGeometry(120,50,200,20)

        self.metin2_sec_button = QPushButton("Dosya Seç",self)
        self.metin2_sec_button.setGeometry(330,50,70,20)
        self.metin2_sec_button.clicked.connect(self.metin2_sec)

        self.karsilastir_button = QPushButton("Karşılaştır",self)
        self.karsilastir_button.setGeometry(150,90,100,30)
        self.karsilastir_button.clicked.connect(self.karsilastir)

        self.sonuc_label = QLabel("",self)
        self.sonuc_label.setGeometry(20,130,380,50)

    def metin1_sec(self):
        dosya, _ = QFileDialog.getOpenFileName(self, "Metin 1 Dosyası Seç", "", "Metin Dosyaları (*.txt)")
        if dosya:
            self.metin1_textbox.setText(dosya)

    def metin2_sec(self):
        dosya, _ = QFileDialog.getOpenFileName(self, "Metin 2 Dosyası Seç", "", "Metin Dosyaları (*.txt)")
        if dosya:
            self.metin2_textbox.setText(dosya)
    
    def karsilastir(self):
        dosya1 = self.metin1_textbox.text()
        dosya2 = self.metin2_textbox.text()

        if not dosya1 or not dosya2:
            self.sonuc_label.setText("Lütfen iki dosya seçin.")
            return

        with open(dosya1, 'r', encoding='utf-8') as f:
            metin1 = f.read()

        with open(dosya2, 'r', encoding='utf-8') as f:
            metin2 = f.read()
        
        kelime_sayisi_metin1 = len(metin1.split())
        kelime_sayisi_metin2 = len(metin2.split())
        harf_sayisi_metin1 = len(metin1.replace(" ",""))
        harf_sayisi_metin2 = len(metin2.replace(" ",""))

        kelime_orani = min(kelime_sayisi_metin1,kelime_sayisi_metin2)/ max(kelime_sayisi_metin1,kelime_sayisi_metin2)
        harf_orani = min(harf_sayisi_metin1,harf_sayisi_metin2)/ max(harf_sayisi_metin1,harf_sayisi_metin2)

        benzerlik=(kelime_orani+harf_orani)/2

        self.sonuc_label.setText("Benzerlik : {}".format(benzerlik))

class Jaccard_Benzerlik(QWidget):
    def __init__(self):
        super().__init__()
        self.ozellikEkle()
        self.ekOzellikEkle()
    
    def ozellikEkle(self):
        self.resize(600,200)
        self.move(700,100)
        self.setWindowTitle("Jaccard ile Karşılaştırma")
    
    def ekOzellikEkle(self):
        self.metin1_label = QLabel("Birinci Metin",self)
        self.metin1_label.setGeometry(20,20,100,20)

        self.metin1_textbox = QLineEdit(self)
        self.metin1_textbox.setGeometry(120,20,200,20)

        self.metin1_sec_button = QPushButton("Dosya Seç",self)
        self.metin1_sec_button.setGeometry(330,20,70,20)
        self.metin1_sec_button.clicked.connect(self.metin1_sec)


        self.metin1_labe2 = QLabel("İkinci Metin",self)
        self.metin1_labe2.setGeometry(20,50,100,20)

        self.metin2_textbox = QLineEdit(self)
        self.metin2_textbox.setGeometry(120,50,200,20)

        self.metin2_sec_button = QPushButton("Dosya Seç",self)
        self.metin2_sec_button.setGeometry(330,50,70,20)
        self.metin2_sec_button.clicked.connect(self.metin2_sec)

        self.karsilastir_button = QPushButton("Karşılaştır",self)
        self.karsilastir_button.setGeometry(150,90,100,30)
        self.karsilastir_button.clicked.connect(self.karsilastir)

        self.sonuc_label = QLabel("",self)
        self.sonuc_label.setGeometry(20,130,380,50)

    def metin1_sec(self):
        dosya, _ = QFileDialog.getOpenFileName(self, "Metin 1 Dosyası Seç", "", "Metin Dosyaları (*.txt)")
        if dosya:
            self.metin1_textbox.setText(dosya)

    def metin2_sec(self):
        dosya, _ = QFileDialog.getOpenFileName(self, "Metin 2 Dosyası Seç", "", "Metin Dosyaları (*.txt)")
        if dosya:
            self.metin2_textbox.setText(dosya)
    
    def karsilastir(self):
        dosya1 = self.metin1_textbox.text()
        dosya2 = self.metin2_textbox.text()

        if not dosya1 or not dosya2:
            self.sonuc_label.setText("Lütfen iki dosya seçin.")
            return

        with open(dosya1, 'r', encoding='utf-8') as f:
            metin1 = f.read()

        with open(dosya2, 'r', encoding='utf-8') as f:
            metin2 = f.read()

        kelimeler_metin1 = metin1.split()
        kelimeler_metin2 = metin2.split()

        ortak_olan_kelimeler=[]

        for kelimeler1 in kelimeler_metin1:
            for kelimeler2 in kelimeler_metin2:
                if kelimeler1 == kelimeler2:
                    ortak_olan_kelimeler.append(kelimeler1)
                    break

        benzerlik = len(ortak_olan_kelimeler) / (len(kelimeler_metin1) + len(kelimeler_metin2) - len(ortak_olan_kelimeler))

        self.sonuc_label.setText("Benzerlik : {}".format(benzerlik))

class Karsilastir_Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.ozellikEkle()
        self.ekOzellikEkle()

    def ozellikEkle(self):
        self.resize(800,200)
        self.move(700,100)
        self.setWindowTitle("Karşılaştırma Menüsü")
    
    def ekOzellikEkle(self):
        self.benzerlik1_button = QPushButton("Jaccard ile karşılaştır",self)
        self.benzerlik1_button.clicked.connect(self.karsilastir1)
        self.benzerlik1_button.setGeometry(60,70,250,40)

        self.benzerlik2_button = QPushButton("Benim benzerlik yöntemi ile karşılaştır",self)
        self.benzerlik2_button.clicked.connect(self.karsilastir2)
        self.benzerlik2_button.setGeometry(400,70,350,40)

    def karsilastir1(self):
        self.jaccard = Jaccard_Benzerlik()
        self.jaccard.show()

    def karsilastir2(self):
        self.benim_benzerlik = Benim_Benzerlik_Yontemi()
        self.benim_benzerlik.show()
    

class Sifre_degistir(QWidget):
    def __init__(self,kullanici_adi):
        super().__init__()
        self.ozellikEkle()
        self.ekOzellikEkle()
        self.kullanici_adi = kullanici_adi

    def ozellikEkle(self):
        self.resize(400,300)
        self.move(700,150)
        self.setWindowTitle("Şifre Değiştir")

    def ekOzellikEkle(self):
        self.eski_sifre_label = QLabel("Eski Sifre",self)
        self.eski_sifre_label.setGeometry(100,30,100,40)

        self.eski_sifre_input = QLineEdit(self)
        self.eski_sifre_input.setGeometry(98,65,200,30)

        self.yeni_sifre_label = QLabel("Yeni Sifre",self)
        self.yeni_sifre_label.setGeometry(100,90,100,40)

        self.yeni_sifre_input = QLineEdit(self)
        self.yeni_sifre_input.setGeometry(98,125,200,30)

        self.kaydet_button = QPushButton("Kaydet",self)
        self.kaydet_button.clicked.connect(self.kaydet)
        self.kaydet_button.setGeometry(150,185,100,40)

    def kaydet(self):
        eski_sifre = self.eski_sifre_input.text()
        yeni_sifre = self.yeni_sifre_input.text()

        database = sqlite3.connect("kullaniciler.db")
        imlec = database.cursor()

        
        imlec.execute("SELECT * FROM kullaniciler WHERE kullaniciadi = ? AND sifre = ?", (self.kullanici_adi, eski_sifre))
        kullanici = imlec.fetchone()
        
        if kullanici:
            imlec.execute("UPDATE kullaniciler SET sifre = ?  WHERE kullaniciadi = ?",(yeni_sifre,self.kullanici_adi))
            database.commit()
            self.close()
        else:
            QMessageBox.critical(self, "Hata","Eski şifre yanlış!")
        
        database.close()

class Menu(QWidget):
    def __init__(self,kullanici_adi):
        super().__init__()
        self.ozellikEkle()
        self.ekozellikekle()
        self.kullanici_adi=kullanici_adi
    
    def ozellikEkle(self):
        self.resize(500,200)
        self.move(700,100)
        self.setWindowTitle("Menü")

    def ekozellikekle(self):
        self.karsilastir_button = QPushButton("Karşılaştır",self)
        self.karsilastir_button.clicked.connect(self.karsilastir)
        self.karsilastir_button.setGeometry(60,70,100,40)

        self.islemler_button = QPushButton("İşlemler",self)
        self.islemler_button.clicked.connect(self.islemler)
        self.islemler_button.setGeometry(195,70,100,40)

        self.cikis_button = QPushButton("Çıkış",self)
        self.cikis_button.clicked.connect(self.cikis)
        self.cikis_button.setGeometry(330,70,100,40)

    def islemler(self):
        self.sifre_degistir_pencere = Sifre_degistir(self.kullanici_adi)
        self.sifre_degistir_pencere.show()

    def cikis(self):
        app.quit()

    def karsilastir(self):
        self.karsilastir_pencere = Karsilastir_Pencere()
        self.karsilastir_pencere.show()


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.ozellikEkle()
        self.ekOzellikEkle()
        self.veritabani_Olustur()
        self.tablo_Olustur()
        self.menu_goster = False
        
        
    def ozellikEkle(self):
        self.resize(400,300)
        self.move(700,100)
        self.setWindowTitle("Kullanıcı Girişi")
    

    def ekOzellikEkle(self):

        self.kullanici_adi_label = QLabel("Kullanıcı Adı",self)
        self.kullanici_adi_label.setGeometry(100,30,100,40)

        self.kullanici_adi_input = QLineEdit(self)
        self.kullanici_adi_input.setGeometry(98,65,200,30)

        self.sifre_label = QLabel("Şifre",self)
        self.sifre_label.setGeometry(100,90,100,40)

        self.sifre_input = QLineEdit(self)
        self.sifre_input.setGeometry(98,125,200,30)

        self.giris_yap_button = QPushButton("Giriş Yap",self)
        self.giris_yap_button.clicked.connect(self.giris_yap)
        self.giris_yap_button.setGeometry(98,180,80,30)

        self.kayıt_ol_button = QPushButton("Kayıt Ol",self)
        self.kayıt_ol_button.clicked.connect(self.kayit_ol)
        self.kayıt_ol_button.setGeometry(218,180,80,30)
    
    def veritabani_Olustur(self):
        self.database = sqlite3.connect("kullaniciler.db")
        self.imlec = self.database.cursor()

    def tablo_Olustur(self):
        self.imlec.execute('''CREATE TABLE IF NOT EXISTS kullaniciler
                             (kullaniciadi TEXT PRIMARY KEY, sifre TEXT)''')
        self.database.commit()

    def giris_yap(self):
        kullanici_adi = self.kullanici_adi_input.text()
        sifre = self.sifre_input.text()
        
        self.imlec.execute("SELECT *FROM kullaniciler WHERE kullaniciadi =? AND sifre =? ",(kullanici_adi,sifre))
        kullanici = self.imlec.fetchone()

        if kullanici:
            #QMessageBox.information(self, "Başarılı", "Giriş Başarılı!")
            self.menu_goster = True
            self.goster_menu()
        else:
            QMessageBox.critical(self, "Hata", "Kullanıcı Adı veya Şifre Yanlış!")
    
    def kayit_ol(self):
        kullanici_adi = self.kullanici_adi_input.text()
        sifre = self.sifre_input.text()

        
        self.imlec.execute("SELECT *FROM kullaniciler WHERE kullaniciadi =? ",(kullanici_adi,))
        kullanici = self.imlec.fetchone()

        if kullanici:
            QMessageBox.critical(self, "Hata", "Bu kullanıcı adı zaten var!")  
        else:
            self.imlec.execute("INSERT INTO kullaniciler (kullaniciadi,sifre) VALUES (?,?)",(kullanici_adi,sifre))
            self.database.commit()
            QMessageBox.information(self, "Başarılı", "Kayıt Başarılı!")

    def goster_menu(self):
        if self.menu_goster:
            self.menu =Menu(self.kullanici_adi_input.text())
            self.menu.show()

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec_())
    


