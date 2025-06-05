from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)  
banner = pyfiglet.figlet_format("X O R C R Y P T\nScorpionMT", font="slant")
print(Fore.GREEN + Style.BRIGHT + banner)

plainT = input(Fore.GREEN + "Veuillez entrer votre Texte : ")
CypherT = 1010

crypted = ''.join([chr(ord(c) ^ CypherT) for c in plainT])

print(Fore.CYAN + "\nTexte chiffré (brut) :")
print(crypted)
