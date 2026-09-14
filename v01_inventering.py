# Inventering av Martin Storme

# Deklarerar variabler av typen strings.
# Uppgift 2) Bytt ut enheterna till de övriga vi har i racket enligt Appendix G i boken.
device_1 = "SW-Nordvik-1"
model_1 = "Cisco 3750G"
role_1 = "Switch, access"

device_2 = "R-Nordvik-1"
model_2 = "Cisco 2951"
role_2 = "Router, lager 3"

# Uppgift 3) Lägger till en tredje enhet som också skrivs ut nedan
device_3 = "FW-Nordvik-1"
model_3 = "Cisco ASA5540"
role_3 = "Brandvägg, lager 4"

print("UTRUSTNINGSLISTA")

# Skriva ut streck för att avgränsa tabellen nedan
print("-" * 52)

# Tecknet <16 i klammern betyder “lägg till mellanslag tills det blir sexton tecken
# brett”. Det är det som gör att kolumnerna hamnar under varandra i stället för
# ojämnt.
print(f"{device_1:<16}{model_1:<20}{role_1}")
print(f"{device_2:<16}{model_2:<20}{role_2}")
print(f"{device_3:<16}{model_2:<20}{role_3}")

print("-" * 52)
# Uppgift 3) Uppdaterat antal enheter i listan
print("Antal enheter: 3")