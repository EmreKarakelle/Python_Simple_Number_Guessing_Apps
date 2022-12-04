import random
import pyautogui

char = "0123456789"
char_list = list(char)

password = pyautogui.password("şifre gir")
guess_password = ""

while(guess_password != password):
    guess_password = random.choices(char_list, k=len(password))  
    print( ">>>>>>>>>>" + str(guess_password) +"<<<<<<<<<<")
    if guess_password == list(password):
        print("Kırılan parola: " + "".join(guess_password))
        break

# pyautogui kütüphanesi ile yapılan küçük bir şifre bulma uygulaması

# 5 ve üzeri haneli sayıların bulunması biraz zaman alıyor 