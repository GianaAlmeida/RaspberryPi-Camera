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
  Primeiramente vamos analisar os pinos da raspberry para entender montarmos o diagrama elétrico. Escolhi usar os pinos "1", "7" e "14", para entrada de energia, pino de leitura e pino terra, respectivamente.<br>

<img src="https://i.stack.imgur.com/QGVhr.png" alt="Descrição do que faz cada pino da raspberry.">

A corrente sugerida para acionar os pinos de entrada é de 3mA a 5mA. Vamos utilizar a alimentação de 3.3 V (pino 1), o pino de leitura GPIO4 (pino 7). 
