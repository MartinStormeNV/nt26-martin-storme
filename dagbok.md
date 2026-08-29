
## ÖVNNG: GÖR DET SJÄLV - Min slutsats 
När man tar ur kabeln och kontakten går ner, så slänger switchen sin anteckning om MAC-adressen till datorn direkt. Aging efter fem minuter gäller alltså inte då.<br><br>
Aging sker bara efter 5 INAKTIVA minuter - dvs<br>
1) så länge länken till datorn är intakt och uppkopplad<br> 
2) och utan att något paket skickas.<br><br>

Om porten försvinner direkt så kan det vara fysiskt fel med t.ex. kabel, avstängd enhet eller aktivt disablad

<br>

## KONTROLLFRÅGOR - ÅTERBLICK

#### 2.14 Vilka tre lägen finns på en Cisco-switch, och hur ser du i prompten vilket du är i?  
"SW-Martin>" användarläge  
"SW-Martin#" Priviligierat läge (enable)  
"SW-Martin(config)#" = konfigurationesläge (configure terminal, eller config t)<br><br>

#### 2.15 Vad händer med din konfiguration om du stänger av switchen utan att spara, och vilket kommando sparar den?  
Alla ändringar du just gjort försvinner. Kommandot: “write memory”<br><br>

#### 2.16 Räkna upp de sju OSI-lagren i ordning. Vilket lager arbetar en switch på?<br>
a) 1 Fysiskt, 2 Datalänk, 3 Nätverk, 4 Transport, 5 Session, 6 Presentation, 7 Applikation<br>
b) En switch arbetar på lager nummer 2, Länklagret.<br><br>
<br>

## OSI-lagren, detaljerad lista
#### 7. Applikation (servrar)**  
Hjälper program att nå nättjänster som ex http/https för webbsidor, smtp för e-post, ftp för filöverföring  
Typiska fel: Servern svarar inte <br><br>

#### 6. Presentation (servrar)**  
Översätta, formatera, kryptera och komprimera data så att den kan förstås av applikationslagret. Teckenkodning ASCII, Unicode, bildformat.  
Typiska fel: Servern svarar inte <br><br>

#### 5. Session (servrar)**  
Starta, styra och avsluta kommunikationssessioner mellan två enheter  
Typiska fel: Servern svarar inte <br><br>

#### 4. Transport (Brandvägg)**  
Delar upp datan och håller reda på vilket program den ska till. Protokoll TCP eller UDP  
Typiska fel: Blockerad port <br><br>

#### 3. Nätverk (Router)**  
IP-adresser och vägval mellan nät  
Typiska fel: Fel nätmask, saknad route <br><br>

#### 2. Datalänk (Switch)**  
Ramar och MAC-adresser inom samma nät  
Typiska fel: Fel VLAN, duplex mismatch <br><br>
 
#### 1. Fysiskt**  
Kablage, patchpanel, kontakter, signaler  
Typiska fel: Trasig kabel, avstängd port



