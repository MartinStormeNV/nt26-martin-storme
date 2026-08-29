# OBS! Har gjort övningen i Packet Tracer vilket gjort att jag fått "Cisco Systems, Inc" på samtliga MAC-adresser nedan.
# ...Även om MAC-adresserna är olika i de första sex sifforna, så hör samtliga enligt "MAC Address Lookup" till leverantören Cisco.

vendors = {
    "00:02:16": "Cisco Systems, Inc",
    "00:60:5c": "Cisco Systems, Inc",
    "00:d0:ff": "Cisco Systems, Inc",
}

# Adresserna du vill sla upp. Byt ut mot dina egna.
addresses = [
    "00:02:16:8b:4d:91",
    "00:60:5c:de:c9:22",
    "00:d0:ff:bd:c2:79",
]

for address in addresses:
    # De forsta atta = tillverkarprefixet.
    prefix = address[0:8]

    # Finns prefixet finns i tabellen så spara det i variabeln "name".
    # Om prefixet inte finns i tabellen så spara istället "okand tillverkar" i variabeln "name"
    if prefix in vendors:
        name = vendors[prefix]
    else:
        name = "okand tillverkare"

    # Skriv ut 
    print(f"{address} -> {name}")
