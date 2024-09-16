#level3
sayi=int(input("sayi gir:"))
if sayi<2:
    print("sayi asal değildir")
    quit()
for bolen in range (2,sayi):
    if(sayi%bolen==0):
        print("sayi asal değildir")
        break
else:
    print("sayi asaldır")