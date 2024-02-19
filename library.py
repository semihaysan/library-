# -*- coding: utf-8 -*-
"""Library.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nDXLh35QnVyKIVZndcSpjBgenRzOYOul
"""

class Library:

  def __init__(self):
      self.file = open("books.txt", "a+")

  def ekle(self):
    kitap_adi = input('Kitabın adı:')
    yazar = input('Yazarın adı:')
    yayin_yili = int(input('Yayınlanma yılı:'))
    sayfa = int(input('Sayfa sayısı:'))
    k_bilgi = f'{kitap_adi}, {yazar}, {yayin_yili}, {sayfa}'
    with open("books.txt", "a+") as files:
      files.write(k_bilgi + '\n')


  def sil(self):
      silinecek_kitap = input('Silmek istediğiniz kitabın adını girin: ')
      with open("books.txt", "r") as file:
          satirlar = file.readlines()

      yeni_satirlar = []
      for satir in satirlar:
          ilk = satir.strip().split(',')[0].strip()
          if ilk != silinecek_kitap:
              yeni_satirlar.append(satir)

      with open("books.txt", "w") as file:
          for yeni_satir in yeni_satirlar:
              file.write(yeni_satir)

  def listele(self):
       self.file.seek(0)
       books = self.file.read().splitlines()
       for book in books:
        k_bilgi = book.split(',')
        print("Kitap adı:", k_bilgi[0])
        print("Yazarı:", k_bilgi[1])
        print("\n")

  def __del__(self):
      self.file.close()

lib = Library()

while(True):

  girdi = input("***MENU*** \n 1) Kitap Ekle \n 2) Kitapları Listele \n 3) Kitabı Sil \n -Çıkmak için Q'ya basınız.- \n ")
  if girdi == "1":
    lib.ekle()
  elif girdi == "2":
    lib.listele()
  elif girdi == "3":
    lib.sil()
  elif girdi.upper() == "Q":
    break;
  else:
    print("geçerli bir karakter giriniz!!!")