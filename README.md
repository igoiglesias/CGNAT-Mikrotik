# CGNAT-Mikrotik
<h2>Gerador de Configuração Para CGNAT Mikrotik</h2>

Scritp escrito em python, responssavel por gerar as configurações necessarias para fazer CGNAT em routers Mikrotik.

<h3>Como Funciona?</h3>

<p>Execute o script</p>

<code>python cgnat-mikrotik.py</code></br>

<p>Ao executar o script vai pedir apenas duas informações, o bloco de IPs para CGNAT (Ex.:100.64.32.0/19) e o bloco de IPs públicos (Ex.: 200.45.3.0/24).</p>

![image](https://user-images.githubusercontent.com/2658126/94922296-5868d880-0490-11eb-9bdb-8ebbb4bba09c.png)

<p>Após isso o script vai criar um arquivo de texto chamdado <b>regras-cgnat</b>, esse arquivo conterá todas as configurações que dever ser executadas no router Mikrotik.

![image](https://user-images.githubusercontent.com/2658126/94922520-c1e8e700-0490-11eb-8956-c6719b7d0467.png)
 
</br></br><h3>Créditos</h3>
<a href="https://under-linux.org/showthread.php?t=189391">Andriopj</>
