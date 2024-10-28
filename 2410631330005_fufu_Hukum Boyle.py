def hitung_p1(V1, P2 , V2):
    """menghitung tekanan awal(P1)menggunakan hukum boyle"""
    P1 =(P2 * V2)/V1
    return P1

def hitung_v1(P1, P2, V2):
    """"menghitung volume awal(V1)menggunakan hukum boyle"""
    V1 = (P2*V2)/P1
    return V1

def hitung_p2(P1, V1, V2):
    """Menghitung tekanan akhir(P2)menggunakan hukum Boyle"""
    P2 = (P1*V1)/V2
    return P2

def hitung_V2(P1,V1,V2):
    """Menghitung volume akhir (V2) menggunakan hukum Boyle"""
    V2 = (P1*V1)/P1
    return V2

def menu():
    print("program untuk menghitung hukum boyle")
    print("1. Hitung tekanan awal (P1 = (P2*V2)/V1)")
    print("2. Hitung volume awal (V1=(P2*V2)/P1)")
    print("3. HItung tekanan akhir (P2=(P1*V1)V2)")
    print("4. HItung volume akhir(V2=(P1*V1)P2)")

    pilihan = input("Masukan pilihan (1/2/3/4): ")

    if pilihan == '1':
        V1 = float(input("Masukan volume awal dalam m**3: "))
        P2 = float(input("Masukan tekanan akhir dalam pa: "))
        V2 = float(input("Masukan volume akhir dalam m**3: "))
        P1 = hitung_p1(V1, P2, V2)
        print(f"tekanan awal(P1): {P1}Pa")

    elif pilihan == '2':
        P1 = float(input("Masukan tekanan awal dalam Pa: "))
        P2 = float(input("Masukan tekanan akhir dalam Pa: "))
        V2 = float(input("Masukan volume akhir dalam m**3: "))
        V1 = hitung_v1 (P1, P2, V2)
        print(f"volume awal(V1):{V1}m**3")

    elif pilihan == '3':
        P1 = float(input("masukan tekanan awal dalam pa: "))
        V1 = float(input("masukan volume awal dalam m**3: "))
        V2 = float(input("masukan volume dalam m**3: "))
        P2 = hitung_p2(P1, V1, V2)
        print(f"Tekanan akhir (P2): {P2}pa")

    elif pilihan == '4':
        P1 = float(input("masukan tekanan awal dalam pa: "))
        V1 = float(input("masukan volume awal dalam m**3: "))
        P2 = float(input("masukan tekanan akhir dalam pa: "))
        V2 = hitung_V2(P1, V1, P2)
        print(f"volume akhir (V2): {V2}m**3")

    else :
        print("pilihan tidak sesuai,silahkan pilih 1/2/3/4")

if __name__=="__main__":
    menu()
