# Krabbafel 1)<br>
<br>
1. Observation:<br>
Datorer i samma VLAN når varandra inom en switch men inte mellan switcharna. Andra VLAN fungerar.<br>
<br>
3. Hypotes:<br>  
Troligen missat att tillåta vlan'et på trunken på någon av switcharna på vardera sida om trunken.<br>
<br><br>
5. Test:<br>
Körde "show interfaces trunk" på båda switcharna och kolla att vlan-nummret står med över allowed vlan's.<br>
<br>
7. Slutsats:<br>
Jag har själv missat detta på ena switchen när jag labbat och det visade sig vara just detta felet. Symtomet är ganska tydligt när lan’et funkar på den egna switchen men inte på andra sidan trunken.<br>
<br>
9. Åtgärd:<br>
Kör "switchport trunk allowed vlan add <nummer>". Obs, alternativet  "switchport trunk allowed vlan <lista>" ersätter helt samtliga tidigare tillåtna vlan.<br>
<br>
<br>
  
# Krabbafel 2)  
1. Observation:<br>
Två VLAN slutar fungera över trunken medan de andra fungerar. Felmeddelande RECV_PVID_ERR eller NATIVE_VLAN_MISMATCH<br>
<br>
3. Hypotes:<br>
Olika nativ vlan på olika switchar.<br>
<br>
5. Test:<br>
Kör `show interfaces trunk` och kolla vilket vlan som står under “Native vlan”<br>
<br>
7. Slutsats:<br>
Har testat i CPT med att ändra på ena sidan, och “NATIVE_VLAN_MISMATCH” är exakt vad som hände.<br>
<br>
9. Åtgärd:<br>
Sätt samma native vlan (lämpligen 999) på båda switcharnas trunkport genom `switchport trunk native vlan 999`
