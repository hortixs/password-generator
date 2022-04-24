# Import
import random
import time
import os

userName = os.getlogin()
numbers = '0123456789'
abc = 'abcdefghijklmnopqrstuvwxyz'
all = numbers + abc
passList = []
_b = 0



# Pervent ValueError:
print("\n\n[+] Veuillez entrer seulement un nombre")
while True:
  try:
    times = int(input('[?] Combien de mots de passe >> '))
    break
  except:
    print("[+] Veuillez entrer seulement un nombre")
while True:
  try:
    chr = int(input('[?] Combien de caractères >> '))
    break
  except:
    print("[+] Veuillez entrer seulement un nombre")

print("\n")
for i in range(times):
  password = "".join(random.sample(all, chr))
  passList.append(password)
  print(f"[>] {password}")
print("\n")
for i in passList:
  i = i + "\n"
  #Modifier en fonction de votre répertoire >
  with open(f'C:\\Users\\{userName}\\Desktop\\password.txt', 'a') as f:
    f.write(i)
input("[+] Listes sauvegardées : (password.txt) survotre bureau.\n\nAppuyez sur la touche Enter pour quitter . . .")
# exit()
