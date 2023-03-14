def pagar_vertikal(n):
    for i in range(n):
        print("#")

def pagar_horizontal(n):
    for i in range(n):
        print("#",end="")

def persegi (n):
    for i in range(n):
        print("0"*n)

def persegi_bolong (n):
    for baris in range(1,n+1):
        if i==1 or i==n:
            print('#',end='')
        else:
            s= n-2
            print("#",end='')
            for i in range(s):
                print(' ',end='')
            print('#',end='')
        print()
    print()


def huruf_x(n):
    print("#"*n)
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if baris == kolom:
                print("#",end='')
            if baris+kolom==n+1:
                print("#",end='')
            else:
                print(' ',end='')
        print()
    print("#"*n)

def huruf_z(n):
    print("#"*n)
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if baris+kolom==n+1:
                print("#",end='')
            else:
                print(' ',end='')
        print()
    print("#"*n)

def huruf_n(n):
    for baris in range(1,n+1):
        for kolom in range (1,n+1):
            if kolom==1 or kolom==n:
                print('#',end='')
            elif baris== kolom:
                print('#',end='')
            else:
                print(' ',end='')
        print()
    print()
def tambah(n):
    tengah=1+(n//2)
    for baris in range(1,n+1):
        for kolom in range (1,n+1):
            if baris==tengah or kolom==tengah:
                print('#',end='')
            else:
                print(' ',end="")
        print()
    print()

def segitiga_kiri(n):
    for i in range(n):
        print("#"*i)

def segitiga_kanan(n):
    for baris in range(1,n+1):
        pagar=baris
        spasi=n-pagar
        for kolom in range (spasi):
            print(' ',end="")
        for kolom in range(pagar):
            print('#',end='')
        print()
    print()
def segitiga_tengah(n):
    for baris in range(1,n+1):
        spasi= n - baris
        pagar= 2*baris-1
        for i in range(spasi):
            print(' ',end="")
        for i in range(pagar):
            print("#",end="")
        print()
    print()


def zig_zag(n):
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if baris%2==1:
                print('#', end='')
            elif baris % 4 == 0:
                print('#',end="")
            else:
                if kolom == n:
                    print("#",end='')
                else:
                    print(" ",end='')
        print()
    print()
            
n=int(input("N:"))
zig_zag(n)

