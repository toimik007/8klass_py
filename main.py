#korduste arv:
kordusi = 10
#
ret = 0
#
for nr in range(kordusi):#
    print(nr)#
    jrk = nr+1#
    #järgmine rida teeb mida?
    val = input("Sisesta "+str(jrk)+". number: ")
    # kuna input annab meile tekstilise muutuja, siis peame koverteerima
    val = int(val)
    #
    if val > 1 or val < 100:
            ret = ret+val#
            print(ret)#

#
ret = ret/kordusi
#
print("Antud arvude keskmine on: "+str(ret))
