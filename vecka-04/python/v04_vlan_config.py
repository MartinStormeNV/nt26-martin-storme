# En funktion som bygger konfigurationen for ett enda VLAN.
def vlan_config(number, name): # T.ex. 1, NAT01 ...
    rader = [] # skapar tom lista
    rader.append(f"vlan {number}") # Skapar en rad med "vlan" + "1" ...
    rader.append(f" name {name}") # Lägger till ännu en rad i listan med " "name" + "NAT01" ...
    return rader # Returnerar listan med två rader till där funktionen anropades


# Skapa nummer
for number in range(1, 41): # Loopa 40 gånger följande kod
    name = f"NAT{number:02}" # Skapa vlan-namnet genom att stoppa in "NAT" + loop-nummer(ev noll före) i sträng
    for rad in vlan_config(number, name): # Anropa funktionen ovan och skicka med vlan-nummer och namn
        print(rad) # Skriver ut funktionens två rader innan nästa loop går igång.
