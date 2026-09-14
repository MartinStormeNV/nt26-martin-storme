# Gör det själv uppgift vecka 03
  
## Svar:  
💡 ***Gateway'en* kan inte nås via `ping` när jag behöll ip-adress men ändrade subnätmask till `255.255.255.0`.  
Orsaken till detta är att min dator och gatewayen hamnade i olika subnät när jag bytte masken. Subnätmasken ändrar vilka ip-adresser min dator anser vara i samma nät.  
  
💡 Så länge en ***filservern*** ligger i samma nät som datorn så når datorn den oavsett om det finns en gateway eller ej. Till gatewayen skickas endast när den som söks inte finns i samma nät.  
  
💡 ***Internet*** ligger inte i samma nät, så utan en gateway nås internet inte av datorn.  


# Återblick - svar:  

3.17 Running-config visar vilken konfiguration jag har skrivit in sedan senast jag sparade.  
Startup-config visar endast de förändringar jag aktivt har sparat med tex `write memory`.  
  
3.18 ***Switchen*** arbetar på lager 2. ***Routern*** arbetar på lager 3.  
  
3.19 Min dator frågar endast efter ***gatewayens(routerns)*** MAC-adress, genom att skicka ut ett ARP-anrop på det lokala nätet.  
Switchen forwardar frames till routern. Routern skickar sedan över internet via mottagarens IP-adress.
