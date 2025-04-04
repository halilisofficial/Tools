'''
Maymun sadece 1, 2 veya 3 adım atabilir.

Eğer 0 olan bir yere basarsa oyun biter.

Maksimum muz toplamaya çalışmalıdır.


Örneğin:

[1, 2, 0, 3, 0, 4, 5, 0, 6]

Burada maymun 1'den başlıyor ve dikkatli ilerlemeli:

✅ 1 → 2 → (3 yerine 4’e sıçra) → 5 → 6 (Toplam: 1 + 2 + 4 + 5 + 6 = 18)

Eğer dikkatsizce 1 → 2 → 3 giderse, 3’ten sonra 0’a basarak oyunu kaybeder.

Bu haliyle problem dinamik programlama (DP) veya geri izleme (backtracking) ile çözülebilir. Biraz kurbağa sıçrama (frog jump) problemi gibi oldu! Ne dersin, çözmeyi dener misin? 😃
'''
array=[1, 2, 0, 3, 0, 4, 5, 0, 6]

#maymunun kaç adim atacagini hesapla
def jump_check(array_index):
    if array[array_index+1] != 0:
        return 1
    if array[array_index+2] != 0:
        return 2
    if array[array_index+3] != 0:
        return 3
    return 0

def main():
    i=0 
    if array[0] !=0:
       eaten_banana = array[0]
       i=0
    elif array[1] !=0:
       eaten_banana = array[1]
       i=1
    else:
       eaten_banana = array[2]
       i=2
    while array[i]!=0 and i<len(array)-1:
        #print(eaten_banana)
        #print(i)
        if(jump_check(i)==0):
            break
        eaten_banana+=array[i+jump_check(i)]
        i=i+jump_check(i)
    print(eaten_banana)


main()

