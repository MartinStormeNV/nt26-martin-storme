# Jag gjort övningen först i Cisco Packet Tracer vilket gjort att jag fått "Cisco Systems, Inc" på samtliga MAC-adresser på den hårdvara jag valde.
# För att övningen skulle bli mer varierad letade jag upp på nätet några andra leverantörer och deras tillhörande MAC-adresser (första halvan=vendor-delen).

vendors = {
    "00:11:0A": "Hewlett Packard",
    "00:05:85": "Juniper Networks",
    "00:18:82": "Huawei Technologies",
}

# Adresserna du vill sla upp. Byt ut mot dina egna.
addresses = [
    "00:11:0A:8b:4d:91",
    "00:05:85:de:c9:22",
    "00:18:82:bd:c2:79",
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
