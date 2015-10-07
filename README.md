## Uma aplicação com openflow para uso em switchs resideciais

O código aqui hospedado faz parte de um trabalho de iniciação científica. Consiste em
uma aplicação para o controlador Ryu, fornecendo um serviço restful para inserção
de regras de alto nível em um switch openflow.

Utilizamos Python 2.7 para escrever este código, como já dito, o Ryu como controlador
openflow. Usamos o OpenvSwitch, logo caso queira testar o código conecte o Ryu ao
OpenvSwitch, pois não utilizamos as funcionalidades do Ryu como switch.

Abaixo descrevemos os serviços providos por nossa API:

<table border="1">
	<tr>
			<th>URL</th>
			<th>Método</th>
			<th>Formato do JSON
	</th>
	<tr>
		<td>flows/block/ip</td>
		<td>POST/DELETE</td>
		<td>{"ip" : "&#60target_ip>"}</td>
	</tr>
	<tr>
		<td>flows/block/mac</td>
		<td>POST/DELETE</td>
		<td>{"mac": "&#60target_mac>"}</td>
	</tr>
	<tr>
		<td>flows/block/port</td>
		<td>POST/DELETE</td>
		<td>{"port": "&#60port_number>"}</td>
	</tr>
	<tr>
		<td>flows/block/betweentimes</td>
		<td>POST/DELETE</td>
		<td>{"begin": "&#60begin_time>", "end": "&#60end_time>"}</td>
	</tr>
	<tr>
		<td>flows/nonblock/betweentimes</td>
		<td>POST/DELETE</td>
		<td>{"begin": "&#60begin_time>", "end": "\<end_time\>"}</td>
	</tr>
	<tr>
		<td>flows/block/protocol</td>
		<td>POST/DELETE</td>
		<td>{"protocol": "&#60protocol_name>"}</td>
	</tr>
	<tr>
		<td>flows/block/protocolport</td>
		<td>POST/DELETE</td>
		<td>{"protocol": "&#60protocol_name>", "port": "&#60port_number>"}</td>
	</tr>
	<tr>
		<td>flows/block/list</td>
		<td>GET</td>
		<td></td>
	</tr>
	<tr>
		<td>flows/nonblock/list</td>
		<td>GET</td>
		<td></td>
	</tr>
	<tr>
		<td>flows/block/all</td>
		<td>POST/DELETE</td>
		<td>{"command": "block_all"}</td>
	</tr>
</table>
