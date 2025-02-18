<b>Como funciona:</b><br>
O Bot utiliza os cargos do discord para fazer um sorteio.<br>
Para utilizalo, adicione ao seu servidor.<br>
Com o bot em execução, em um chat em que ele possuir acesso, digite o comando:<br>
/daily "cargo"<br>
Então ele imprime uma lista de sorteio para as reuniões.
<br><br>
Fique a vontade para alterar o comando e personalizar o texto da forma que melhor agradar.


<b>Como instalar e configurar:</b>
Criar uma nova aplicação no site do discord:<br>
https://discord.com/developers/applications

-> Navegue até installation, copiar o Install Link e abrir no navegador.<br>
-> Autorize o acesso ao bot ao seu discord<br><br>

-> Ainda nas configurações, navegue até a seção Bot<br>
Crie um Token<br>
Em Privileged Gateway Intents marcar os 3 checkbox listados abaixo:<br>
[x] Presence Intent<br>
[x] Server Members Intent<br>
[x] Message Content Intent<br>
<br>
-> O token criado deve ser adicionado ao arquivo .env
<br><br>
Comando de instalação para execução local:
<br>
Instale pip:
<br>
sudo apt install python3-pip
<br>
<br>
Comando instalação das dependencias do discord pelo pip:
<br>
python3 -m pip install -U discord.py
<br>
pip install python-dotenv
<br><br>
Para inicializar o bot: 
<br>
python3 main.py
<br><br>


Para fazer o deploy utilizei (https://railway.com/) com um plano free.
<br>
Iniciei um projeto como Background Worker e adicionei o repositorio.




