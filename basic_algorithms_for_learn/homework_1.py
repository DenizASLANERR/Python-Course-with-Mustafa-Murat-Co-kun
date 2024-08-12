print("""####################
Mustafa Murat Coşkun Python Kursu/ Ödev-1
####################""")
import time

print("####### Problem-1 #######")
print("Kullanıcıdan aldığınız bir sayının mükemmel olup\n "
      "olmadığını bulmaya çalışın.Bir sayının kendi hariç \n"
      "bölenlerinin toplamı kendine eşitse bu sayıya 'mükemmel\n"
      " sayı' denir. Örnek olarak, 6 mükemmel bir sayıdır.\n"
      " (1 + 2 + 3 = 6)")
sums = 0
usr_num = int(input("Bir sayı giriniz:"))
for i in range(1, usr_num):
    if usr_num % i == 0:
        sums += i
if sums == usr_num:
    print(usr_num, "bir 'Mükemmel sayı'dır")
else:
    print(usr_num, "bir 'Mükemmel sayı' değildir.")


print("####### Problem-2 #######")
print("Kullanıcıdan aldığınız bir sayının 'Armstrong' sayısı olup\n"
      " olmadığını bulmaya çalışın. Örnek olarak, Bir sayı eğer\n"
      " 4 basamaklı ise ve oluşturan rakamlardan herbirinin\n"
      " 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti )\n"
      " o sayıya eşitse bu sayıya 'Armstrong' sayısı denir.\n"
      "Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4")
con_num = 0
counter = 0
added_num = input("Sayıyı giriniz:")
controller = int(added_num)
for splited_num in added_num:
    counter += 1
if counter == 4:
    for splited_num in added_num:
        int_num = int(splited_num)
        con_num += int_num ** 4
    print(con_num)
    if controller == con_num:
        print("Bu bir amstrong sayıdır!")
elif counter == 3:
    for splited_num in added_num:
        int_num = int(splited_num)
        con_num += int_num ** 3
    print(con_num)
    if controller == con_num:
        print("Bu bir amstrong sayıdır!")
elif counter == 5:
    for splited_num in added_num:
        int_num = int(splited_num)
        con_num += int_num ** 5
    print(con_num)
    if controller == con_num:
        print("Bu bir amstrong sayıdır!")
elif counter == 2:
    for splited_num in added_num:
        int_num = int(splited_num)
        con_num += int_num ** 2
    print(con_num)
    if controller == con_num:
        print("Bu bir amstrong sayıdır!")
print("####### Problem-3 #######")
print("1'den 10'kadar olan sayılarla ekrana çarpım tablosu \n"
      "bastırmaya çalışın. *İpucu: İç içe 2 tane for döngüsü \n"
      "kullanın. Aynı zamanda sayıları range() fonksiyonunu \n"
      "kullanarak elde edin.*")
for i in range(1, 11):
    print("##########################")
    for j in range(1, 11):
        print(f"{i}*{j}={i * j}")

print("####### Problem-4 #######")
print("Her bir while döngüsünde kullanıcıdan bir sayı alın ve\n"
      "kullanıcının girdiği sayıları 'toplam' isimli bir\n"
      "değişkene ekleyin. Kullanıcı 'q' tuşuna bastığı zaman \n"
      "döngüyü sonlandırın ve ekrana 'toplam değişkenini' \n"
      "bastırın. *İpucu : while döngüsünü sonsuz koşulla \n"
      "başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.*")

last_sums = 0
while True:
    usr_entry = input("Bir sayı giriniz:\nİşlemi sonlandırmak için 'q' harfi giriniz")

    if usr_entry == "q":
        print("İşlem bitti!!!")
        break
    else:
        last_sums += int(usr_entry)
print(f"İşleminizin sonucu:{last_sums}")


print("####### Problem-5 #######")
print("1'den 100'e kadar olan sayılardan sadece 3'e bölünen \n"
      "sayıları ekrana bastırın. Bu işlemi *continue* ile \n"
      "yapmaya çalışın.")
i = 1
while i < 100:
    if i % 3 == 0:
        print(i)
        i += 1
    else:
        i += 1
        continue
print("####### Problem-6 #######")
print("Buradaki problemin çözümünü derslerimizde özellikle \n"
      "öğrenmedik. Burada mantık yürüterek ve list comprehension\n"
      " kullanarak 1'den 100'e kadar olan sayılardan sadece çift \n"
      "sayıları bir listeye atmayı yapmayı çalışın.\n"
      " Not: Programlamada her detayı öğrenemeyiz. \n"
      "Bunun için bazı yerlerde deneme yanılma yoluyla da \n"
      "öğrendiğimiz şeyler olur. Bu problemde deneme yanılma \n"
      "yoluyla list comprehension'ın koşullu durumlarla kullanımını \n"
      "öğreneceksiniz. İpucu: Basit düşünmeye çalışın.")



new_list = [i for i in range(1,101) if i % 2 == 0]
print(new_list)







