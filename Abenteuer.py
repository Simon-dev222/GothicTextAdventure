RED = '\033[91m'    # Red color added
GREEN = '\033[92m'  # Green color added
BLUE = '\033[94m'   # Blue color added
RESET = '\033[0m'   # This resets the color back to default

import sys,time,random

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


      
print_slow(f"{GREEN}""Willkommen zu Gothic!")
print_slow(" In diesem Textbasierten Abenteuer wirst du die Welt von Gothic mit all seinen Gefahren,")
print_slow(" Geheimnissen und Mythen kennen lernen. \nLehn dich zurück und tauche ein in die Minenkolonie der Insel Khorinis\n\n\n")

print_slow(f"{RED}""\nDas Königreich Myrtana, wiedervereint durch die Hand König Rhobars II.")
print_slow(" \nIn den langen Jahren seiner Herrschaft war es ihm gelungen, alle Widersacher des Reiches zu bezwingen ... \nBis auf einen.")
print_slow(" \nOrks.\n\n")
print_slow(" \nDer Krieg mit den Orks forderte seinen Tribut ...")
print_slow(" \n... und die Gefangenen des Reiches sollten ihn bezahlen.")
print_slow(" \nDer König brauchte Schwerter für seine Armeen und jeder, \nder sich eines auch noch so geringen Verbrechens schuldig gemacht hatte,"" \nwurde zur Arbeit in den Erzminen von Khorinis gezwungen.\n\n")
print_slow(" \nAus allen Teilen des Landes wurden Gefangene gebracht.")
print_slow(" \nUm jede Flucht unmöglich zu machen, sandte der König die mächtigsten Magier des Reiches aus, \neine magische Barriere um das gesamte Tal zu errichten.")
print_slow(" \nICH war einer der Magier.")
print_slow(" \nWir mussten all unsere Macht bündeln, um die Barriere zu erschaffen, aber etwas störte das gebrechliche Gefüge der Magie.")
print_slow(" \nWir waren nun selbst Gefangene der Barriere.\n\n")
print_slow(" \nMehr als eine Sekunde der Unachtsamkeit brauchten die Gefangenen nicht - als wir zur Festung kamen, \nwar keiner der Wärter mehr am Leben.")
print_slow(" \nUnd obwohl die Aufsässigen nicht wagten uns anzugreifen, waren wir machtlos.")
print_slow(" \nKhorinis, mit all seinen Minen, war nun in den Händen der Gefangenen.")
print_slow(" \nDer König hatte keine Wahl.")
print_slow(" \nEr musste verhandeln, er brauchte das Erz.")
print_slow(" \nAber seine einstigen Sklaven verlangten nun einen hohen Preis.\n\n")
print_slow(" \nMonat für Monat lieferte der König den Gefangenen alles, was sie verlangten, \nMonat für Monat brachten sie dafür das Erz an den Rand der Barriere.")
print_slow(" \nIn all den Jahren wurden viele Versuche unternommen, die magische Barriere zu öffnen, \naber keiner hatte Erfolg.")
print_slow(" \nBis heute!")
print_slow(" \nEin weiterer Verurteilter wurde zur Klippe gebracht. \nEr wusste noch nichts von seinem Schicksal, aber ER sollte alles ändern.\n\n\n\n\n")










print(f"{BLUE}""Du stehst an einer Klippe. Vor dir erstreckt sich eine Kuppel von gigantischem Ausmaß.")
print("Unter dir erblickst du einen kleinen See mit einer Forderanlage.")