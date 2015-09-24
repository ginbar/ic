#Aplicação para controle de um switch residencial com OpenFlow

O propósito desta aplicação é combinar o uso do protocolo OpenFlow combinado com
um ambiente orientado a eventos, para criar uma solução flexível para definição
de regras de conectividade em um switch.
Ela foi usada junto ao controlador Ryu, o OpenvSwitch e foi embarcada em uma
máquina virtual e uma placa Allwiner CubieTruck com OpenWrt. Toda a aplicação
foi desenvolvida em Python, versão 2.7, a versão do OpenWrt usado foi a 15.04.
Como solução de hotspot para transforma a placa em um acess point foi o
Nodogsplash.
