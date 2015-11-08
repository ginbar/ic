	## Uma aplicação com openflow para uso em switchs resideciais

	O código aqui hospedado faz parte de um trabalho de iniciação científica. Consiste em
	uma aplicação para o controlador Ryu, fornecendo um serviço restful para inserção
	de regras de alto nível em um switch openflow.

	Utilizamos Python 2.7 para escrever este código, e como já dito, o Ryu como controlador
	openflow. Usamos o OpenvSwitch, logo caso queira testar o código conecte o Ryu ao
	OpenvSwitch, pois não utilizamos as funcionalidades do Ryu como switch.

	Abaixo descrevemos os serviços providos por nossa API:

	<table border="1">
		<tr>
				<th>URL</th>
				<th>Método</th>
				<th>Formato do JSON</th>
		</tr>
		<tr>
			<td>/add_by_ip</td>
			<td>POST</td>
			<td>{"ip" : "&#60target_ip>"}</td>
		</tr>
		<tr>
			<td>/delete_by_ip</td>
			<td>POST</td>
			<td>{"ip" : "&#60target_ip>"}</td>
		</tr>
		<tr>
			<td>/add_by_mac</td>
			<td>POST</td>
			<td>{"mac": "&#60target_mac>"}</td>
		</tr>
		<tr>
			<td>/delete_by_mac</td>
			<td>POST</td>
			<td>{"mac": "&#60target_mac>"}</td>
		</tr>
		<tr>
			<td>/add_by_port</td>
			<td>POST</td>
			<td>{"port": "&#60port_number>"}</td>
		</tr>
		<tr>
			<td>/delete_by_port</td>
			<td>POST</td>
			<td>{"port": "&#60port_number>"}</td>
		</tr>
		<tr>
			<td>/add_blockbetweentimes</td>
			<td>POST</td>
			<td>{"ip" : "&#60target_ip>", "begin": "&#60begin_time>", "end": "&#60end_time>"}</td>
		</tr>
		<tr>
			<td>/delete_blockbetweentimes</td>
			<td>POST</td>
			<td>{"ip" : "&#60target_ip>", "begin": "&#60begin_time>", "end": "&#60end_time>"}</td>
		</tr>
		<tr>
			<td>/add_nonblockbetweentimes</td>
			<td>POST</td>
			<td>{"ip" : "&#60target_ip>", "begin": "&#60begin_time>", "end": "&#60end_time>"}</td>
		</tr>
		<tr>
			<td>/delete_nonblockbetweentimes</td>
			<td>POST</td>
			<td>{"ip" : "&#60target_ip>", "begin": "&#60begin_time>", "end": "&#60end_time>"}</td>
		</tr>
		<tr>
			<td>/add_by_protocol</td>
			<td>POST</td>
			<td>{"protocol": "&#60protocol_name>"}</td>
		</tr>
		<tr>
			<td>/delete_by_protocol</td>
			<td>POST</td>
			<td>{"protocol": "&#60protocol_name>"}</td>
		</tr>
		<tr>
			<td>/add_by_protocolport</td>
			<td>POST</td>
			<td>{"protocol": "&#60protocol_name>", "port": "&#60port_number>"}</td>
		</tr>
		<tr>
			<td>/delete_by_protocolport</td>
			<td>POST</td>
			<td>{"protocol": "&#60protocol_name>", "port": "&#60port_number>"}</td>
		</tr>
		<tr>
			<td>/list</td>
			<td>GET</td>
			<td></td>
		</tr>
		<tr>
			<td>/lock</td>
			<td>PUT</td>
			<td>{"command": "block_all"}</td>
		</tr>
		<tr>
			<td>/unlock</td>
			<td>PUT</td>
			<td>{"command": "block_all"}</td>
		</tr>
	</table>
