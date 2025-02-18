<b>Como funciona:</b><br>
O Bot utiliza os cargos do discord para fazer um sorteio e envia esta lista no chat.<br>
Adicione ao seu servidor.<br>
Em um chat em que ele possuir acesso, digite o comando:<br>
/daily "cargo"<br><br>


<b>Como instalar e configurar:</b>
Criar uma nova aplicação no site do discord:<br>
https://discord.com/developers/applications

-> Navegue até installation, copiar o Install Link e abrir no navegador.<br>
-> Autorize o acesso ao bot ao seu discord<br><br>

-> Navegue até a seção Bot<br>
Crie um Token<br>
Em Privileged Gateway Intents marcar os 3 checkbox listados abaixo:<br>
[x] Presence Intent<br>
[x] Server Members Intent<br>
[x] Message Content Intent<br>
<br>
O token criado deve ser adicionado ao arquivo .env
<br>
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
<br>

<br>
Para inicializar o bot: 
<br>
python3 main.py
<br><br>


Para fazer o deploy utilizei render.com
<br>
Iniciei um projeto como webservice, adicionei o repositorio.
<br>
Build command: pip install discord.py python-dotenv
<br>
Start command: python3 main.py
<br>



