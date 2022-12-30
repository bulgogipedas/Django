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
        if counter == 9:
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

belahKetupatFor()