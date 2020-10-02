#!/usr/bin/env python3
import time
import os
import ipaddress

regraMK= "$addNatRules NewChain=cgnat NetworkIP=100.64.200.0/27 IPsPerRule=8 toPublicIP=2.2.2.2 portStart=1025 portsPerAddr=2000"

cgnat = input("Rede IPs CGNAT: ")
publicos = input("Rede IPs Publicos: ")

cgnat = ipaddress.IPv4Network(cgnat, strict=False)
publicos = ipaddress.IPv4Network(publicos, strict=False)

qtdCgnat = 0
qtdCgnatNets = 0

cgnatSubNets = []


for ip in cgnat:
	qtdCgnat+=1
	try:
		newNet = ipaddress.ip_network(str(ip) + '/27')
		if newNet.subnet_of(cgnat):
			cgnatSubNets.append(str(newNet))
			qtdCgnatNets+=1
		
	except Exception as e:
		pass

qtdPublicos = 0

for ipPublico in publicos:
	qtdPublicos += 1

if qtdPublicos >= qtdCgnatNets:
	pass
else:
	print("Poucos IPs Publicos")
	exit()

regras = open("regras-cgnat.txt", "a")
regras.write("""
	:global addNatRules do={
:global srcStart [:pick $NetworkIP 0 [:find $NetworkIP "/"]]
:global srcStart2 $srcStart
:global QtdRegras 0
:global QtdRegras2 0
:global portStop ($portStart + $portsPerAddr - 1)
  /ip firewall nat add chain=srcnat action=jump jump-target=$NewChain comment="CGNAT" src-address="$NetworkIP"
        :log info "O Network é $NetworkIP";
        :log info "Iniciando em $srcStart";
:put "Current IP: $srcStart\r\nTarget: $NetworkIP\r\n"
  :while ($srcStart in $NetworkIP) do={
        :log info "IP atual é $srcStart";
    /ip firewall nat add chain=$NewChain action=jump jump-target="$NewChain-$($QtdRegras)" src-address="$srcStart-$($srcStart + ($IPsPerRule - 1 ))"
        :set QtdRegras ($QtdRegras + 1);
        :set srcStart ($srcStart + $IPsPerRule);
  }
        :log info "Qtd de Regras Jump criadas: $QtdRegras";
  :while ($srcStart2 in $NetworkIP) do={
        :for i from=1 to=$IPsPerRule do={
         /ip firewall nat add chain="$NewChain-$QtdRegras2" action=src-nat comment="CGNAT IP $srcStart2 Porta $portStart - $portStop" protocol=tcp src-address=$srcStart2 to-address=$toPublicIP to-ports="$portStart-$portStop"
         /ip firewall nat add chain="$NewChain-$QtdRegras2" comment="CGNAT IP $srcStart2 Porta $portStart - $portStop" action=src-nat protocol=udp src-address=$srcStart2 to-address=$toPublicIP to-ports="$portStart-$portStop"
        :set srcStart2 ($srcStart2 + 1);
        :set $portStart ($portStop + 1);
        :set $portStop ($portStart + $portsPerAddr - 1);
        :set i ($i + 1)
        }
        :set QtdRegras2 ($QtdRegras2 + 1);
  }
}
	\n\n\n""")

for ipPublico, cgnatSubNet in zip(publicos, cgnatSubNets):

	regras.write("ip address add address="+str(ipPublico)+" interface=loopback\n")
	regras.write("$addNatRules NewChain=cgnat NetworkIP="+cgnatSubNet+" IPsPerRule=8 toPublicIP="+str(ipPublico)+" portStart=1025 portsPerAddr=2000\n")

regras.close()

#print(cgnatSubNets)
print()
print("Foram Geradas "+ str(qtdCgnatNets) +" subnets")