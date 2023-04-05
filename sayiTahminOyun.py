from random import randint
r= randint(1,101)
sayac=0
while True:
   sayac+=1
   s = int(input("(Cikmak için->0)\tTahmininiz: "))
   if s==0:
       break
   elif s<r :
       print("Daha buyuk bir sayi giriniz")
       continue
   elif s>r:
       print("Daha kucuk bir sayi giriniz")
       continue
   else:
       print("Buldunuz sayi: {}".format(r))
       print("{} . denemede buldunuz".format(sayac))
       break
