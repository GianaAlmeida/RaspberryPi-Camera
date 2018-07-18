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
<i>Imagem extraída de https://i.stack.imgur.com/QGVhr.png </i><br><br>

A corrente sugerida para acionar os pinos de entrada é de 3mA a 5mA. Vamos utilizar a alimentação de 3.3 V (pino 1), o pino de leitura GPIO4 (pino 7). Para representar nosso circuito, desenhei o diagrama abaixo:
<br>
<img src="circuito.JPG"><br>
<i>Circuito desenhado com essa ferramenta: https://easyeda.com/ </i><br> <br>

O botão que ganhamos é do tipo “normalmente fechado”, que quer dizer que passa energia enquanto está desativado, e quando apertarmos o botão, ele desliga. A leitura digital interpreta “tem energia” e “não tem energia”. 
<br><br>
Para garantir que quando apertar o botão o pino realmente vá para 0V, reduzindo riscos de ler flutuação de energia, usamos o resistor na configuração pull-down. 
<br><br>
Sem ele, o pino pode ler ruído e algum resquício de flutuação,de energia confundindo a leitura da raspberry, que poderá interpretar um  “0.9V” como tem energia, por ex e fazer com que o projeto não funcione.
<br><br>

<h3>b) Montagem elétrica da câmera</h3>
<img src="https://www.raspberrypi.org/app/uploads/2017/05/Pi-Camera-attached-1-1390x1080.jpg" alt="Foto da raspberry pi3 com a camera V2" width=70% height=70%>
<i>Imagem extraida de https://www.raspberrypi.org/ </i><br> <br>

A câmera deve ser montada conforme a figura acima, a “fita”possui um lado com contatos (prateado) e outro sem (azul). O lado azul fica voltado para o conector de rede (ethernet). Após conectar a câmera finalmente podemos ligar a raspberry. <br> <br>

<h2>Com a Raspberry ligada:</h2>

