
users = {
    "salam123": "1234",
    "user1": "abcd",
    "admin": "admin123"
}

attempts = 3

while attempts > 0:
    istifadeci_adi = input("İstifadəçi adını daxil edin: ")
    istifadeci_sifresi = input("İstifadəçi şifrəsini daxil edin: ")
    if istifadeci_adi in users and users[istifadeci_adi] == istifadeci_sifresi:
        print("✅ Xoş gəldiniz, " + istifadeci_adi + "!")
        break  
    else:
        attempts -= 1
        print("❌ Yanlış giriş. Qalan cəhd sayı: " + str(attempts))
if attempts == 0:
    print("⛔ Çox cəhd etdiniz! Giriş bloklandı.")

