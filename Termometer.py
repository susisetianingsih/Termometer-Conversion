print("===============================================")
print("Ini adalah Sistem Konversi Termometer Sederhana")
print("===============================================")

def exit():
    print("Program Selesai")
    
def suhu(a,b):
    print("Reamur:", (4*b)/a)
    print("Celcius:", (5*b)/a)
    print("Farenheit:", ((9*b)/a)+32)
    print("Kelvin:", ((5*b)/a)+273)
    print("\n")
    termometer()

def termometer():
    print("\n*** SATUAN ***")
    satuan = ["Celcius", "Reamur", "Farenheit", "Kelvin", "Keluar"]
    b = 0
    for i in satuan:
        b=b+1
        print("{}. {}".format(b, i))
    
    x = int(input("Pilih menu:"))
    if x < 5:
        y = float(input("Masukan suhu:"))
    
    print("\n*** HASIL ***")
    if x == 1:
        a = 5
        suhu(a,y)
    elif x == 2:
        a = 4
        suhu(a,y)
    elif x == 3:
        a = 9
        suhu(a,y-32)
    elif x == 4:
        a = 5
        suhu(a,y-273)
    elif x == 5:
        exit()
    else:
        print("Masukan tidak valid")
        print("\n")
        termometer()
            
termometer()
    