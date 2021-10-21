def feladat24():
    szam=float(input("kérek egy számot: "))
    while szam!=0:
        szam=float(input("kérek egy masik számot! kilépés=0: "))

def feladat25():
    szam=float(input("kérek egy pozitiv számot! "))
    while szam<=0:
        szam=float(input("nem pozitív számot adtál, add meg újra!"))

#itt kezdődik a főprogram
#feladat24()
feladat25()

