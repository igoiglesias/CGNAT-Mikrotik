# CGNAT-Mikrotik
<h2>Gerador de Configuração Para CGNAT Mikrotik</h2>

Scritp escrito em python que dera as configurações necessarias para fazer CGNAT em routers Mikrotik.

<h3>Como Funciona</h3>

<p>Execute o script</p>

<code>python cgnat-mikrotik.py</code></br>

<p>Ao executar o script vai pedir apenas duas informações, o bloco de IPs para CGNAT (Ex.:100.64.32.0/19) e o bloco de IPs públicos (Ex.: 200.45.3.0/24).</p>

<p>Após isso o script vai criar um arquivo de texto chamdado <b>regras-cgnat</b>, esse arquivo conterá todas as configurações que dever ser executadas no router Mikrotik.
  
 
<h3>Créditos</h3>
<a href="https://under-linux.org/showthread.php?t=189391">Andriopj</>
