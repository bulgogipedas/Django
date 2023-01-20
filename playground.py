
def belahKetupat():
    sisi = int(input("Masukkan sisi: "))
    i = 1
    spasi = int(sisi/2)

    while True:
        if(i%2):
            print(" "*spasi,"+"*i)
            spasi -= 1
            i += 1
        else:
            i += 1
            continue

        if i > sisi:
            break
    
    i = (sisi-1)
    spasi = 1

    while True:
        if(i%2):
            print(" "*spasi,"+"*i)
            i -= 1
            spasi += 1
        if i < 1:
            break
        else:
            i -= 1
            continue
            
def belahKetupatFor():
    sisi = int(input("Masukkan input: "))
    spasi = int(sisi/2)
    counter = 1

    for counter in range(sisi):
        if (counter%2):
            print(" "*spasi,"+"*counter)
            counter += 1
            spasi -= 1
        else:
            counter += 1
            continue
        
    counter = (sisi-1)
    spasi = 1

    for i in range (sisi):
        if counter == sisi-1:
            counter -= 1
            spasi += 1
            continue 

        if (counter%2):
            print(" "*spasi,"+"*counter)
            counter -= 1
            spasi += 1
        else:
            counter -= 1
            continue

def loopJumlahAngka():
    jumlahAngka = int(input("Masukkan berapa yang akan dijumlahkan: "))
    jumlah = float(0)

    for i in range(jumlahAngka):
        i += 1
        print("Masukkan angka ke-", i , " = ", end='')
        angka = float(input(""))
        jumlah += angka
   
    print("Jumlahnya adalah ", jumlah )

def faktorial():

    faktor = int (1)
    bilangan = (int(input("Masukkan bilangan bulat: ")))

    if bilangan <= 0:
        print("Maaf input yang kamu masukkan salah")
    else:
        for i in range(bilangan):
            i += 1
            faktor *= i

    print("Hasilnya adalah ", faktor)



def jajarGenjang():
    spasi = 0

    #Input baris dan lebar yang diinginkan
    BL = int(input("Masukkan input: "))

    while True:
        print(" "*spasi,"+"*BL)
        spasi += 1

        if spasi == BL:
            break

def jurang():
    dalam = int(input("Masukkan input: "))
    counter = 1
    lebar = dalam*2
    spasi = 1
    while counter <= dalam:
        print("*"*counter, end='')
        for spasi in range(dalam):
            print(" "*(lebar-2), end='')
            lebar -= 2
            spasi += 1
            break
        print("*"*counter)
        counter += 1
            
        
belahKetupat()

