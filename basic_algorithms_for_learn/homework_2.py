print("##### Problem-1 #####")
print("Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.")

height = float(input("Boyunuzu Giriniz(metre cinsinden ör:1.83):"))
weight = float(input("Kilonuzu Giriniz:"))

vki = weight / height ** 2

if vki < 18.5:
    print(f"VKİ:{vki}.Zayıfsınız.Biraz kilo almalısınız.")
elif 25.00 > vki >= 18.5:
    print(f"VKİ:{vki}.Normal Kilodasınız")
elif 30.00 > vki >= 25.00:
    print(f"VKİ:{vki}.Fazla kilolarınız var")
elif vki > 30.00:
    print(f"VKİ:{vki}.Obezite tehlikesi var. Lütfen tıbbi destek alın.")



print("##### Problem-2 #####")
print("Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.")

num_1 = input("İlk sayıyı giriniz:")
num_2 = input("İkinci sayıyı giriniz:")
num_3 = input("Üçüncü sayıyı giriniz:")

if num_1 > num_2 and num_1 > num_3:
    print(f"En büyük sayı {num_1}")
elif num_2 > num_1 and num_2 > num_3:
    print(f"En büyük sayı {num_2}")
elif num_3 > num_2 and num_3 > num_1:
    print(f"En büyük sayı {num_3}")
else:
    print("Tüm sayılar eşittir...")



print("##### Problem-3 #####")
"""Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""



while True:

    midterm_1 = float(input("1.Vize puanını giriniz:"))
    midterm_2 = float(input("2.Vize puanını giriniz:"))
    final = float(input("Final puanınızı giriniz:"))

    last_point = (midterm_1 * 30 / 100) + (midterm_2 * 30 / 100) + (final * 40 / 100) / 3

    if 100 > last_point > 0:
        print(f"Dönem sonu notunuz:{last_point}")
        break
    else:
        print("Puanınız hesaplanamadı! \nDeğerleri doğru girdiğinizden emin olun")


print("##### Problem-4 #####")
"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz.
"""
while True:
    shape_type = input("Hesaplamak istediğiniz şekili yasınız\nEğer dörtgen ise 'dortgen'\nEğer üçgen ise 'ucgen' yazınız: ")

    if shape_type == "dortgen":
        quadri_edge_up = abs(float(input("Üst kenarı giriniz:")))
        quadri_edge_right = abs(float(input("Sağ kenarı giriniz:")))
        quadri_edge_down = abs(float(input("Alt kenarı giriniz:")))
        quadri_edge_left = abs(float(input("Sol kenarı giriniz:")))

        if quadri_edge_up == 0 or quadri_edge_down == 0 or quadri_edge_right == 0 or quadri_edge_left == 0:
            print("Şekil bir dörtgen belirtmiyor...")
        elif quadri_edge_up == quadri_edge_down == quadri_edge_right == quadri_edge_left:
            print("Girilen şekil bir 'Kare'")
        elif quadri_edge_up == quadri_edge_down and quadri_edge_right == quadri_edge_left:
            print("Girilen şekil bir 'Dikdörtgen'")
        else:
            print("Girilen şekil sıradan bir dikdörtgen")
    elif shape_type == "ucgen":
        triang_edge_1 = abs(float(input("Üçgenin 1.kenar uzunluğu:")))
        triang_edge_2 = abs(float(input("Üçgenin 2.kenar uzunluğu:")))
        triang_edge_3 = abs(float(input("Üçgenin 3.kenar uzunluğu:")))

        if triang_edge_1 == 0 or triang_edge_2 == 0 or triang_edge_3 == 0:
            print("Şekil bir üçgen belirtmiyor.")
        elif triang_edge_1 == triang_edge_2 or triang_edge_2 == triang_edge_3 or triang_edge_1 == triang_edge_3:
            print("Bu bir ikiz kenar üçgendir.")
        elif triang_edge_1 == triang_edge_2 == triang_edge_3:
            print("Bu bir eşkenar üçgendir.")
        else:
            print("Bu bir sıradan üçgendir.")
























