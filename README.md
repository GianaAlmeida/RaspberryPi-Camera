# RaspberryPi

Você já quis que sua raspberry funcionasse como uma câmera?
Para algumas aplicações seria vantajoso, certo?

Esse projeto pretende atender as seguintes necessidades:
- Ao ligar a raspberry, o código já rode em segundo plano (sem eu ter que mandar executar)
- Ao eu apertar um botão a foto seja tirada
- A foto recente não deve substituir a antiga

Vou mostrar como fazer, tudo em Python <3

<h2>Com a Raspberry desligada:</h2>

<h3>a) Montagem elétrica do botão</h3>
  Primeiramente vamos analisar os pinos da raspberry para entender montarmos o diagrama elétrico. Escolhi usar os pinos "1", "7" e "14", para entrada de energia, pino de leitura e pino terra, respectivamente.<br><br>

<img src="https://i.stack.imgur.com/QGVhr.png" alt="Descrição do que faz cada pino da raspberry." width=70% height=70%>
<i>Imagem extraída de https://i.stack.imgur.com/QGVhr.png </i><br>

A corrente sugerida para acionar os pinos de entrada é de 3mA a 5mA. Vamos utilizar a alimentação de 3.3 V (pino 1), o pino de leitura GPIO4 (pino 7). Para representar nosso circuito, desenhei o diagrama abaixo:
<br>
<img src="circuito.JPG">
<i>Circuito desenhado com essa ferramenta: https://easyeda.com/ </i>

O botão que ganhamos é do tipo “normalmente fechado”, que quer dizer que passa energia enquanto está desativado, e quando apertarmos o botão, ele desliga. A leitura digital interpreta “tem energia” e “não tem energia”. 
<br>
Para garantir que quando apertar o botão o pino realmente vá para 0V, reduzindo riscos de ler flutuação de energia, usamos o resistor na configuração pull-down. 
<br>
Sem ele, o pino pode ler ruído e algum resquício de flutuação,de energia confundindo a leitura da raspberry, que poderá interpretar um  “0.9V” como tem energia, por ex e fazer com que o projeto não funcione.
