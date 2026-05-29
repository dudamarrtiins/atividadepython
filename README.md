# 💻 Exercícios em Python 

## Elaboração de exercicios

## 💻 tecnologias usadas
- Linguagem : python
- Google Colab/VS
- Git e Github

## 🌐 Projeto

Essa atividade foi desenvolvida em sala de aula do Senai, visando desenvolver habilidades estudadas em sala de aula.

## Resolução da Atividade

## Exercicio 1️⃣

- Requisitos 

Faça um algoritmo usando o for para mostrar os números pares e impares de 0 a 100. 

- Foram utilizado na estrutura: 

o Laço For com a função Range, estrutura condicional (IF/ELSE) e % 

O For  é utilizado para o limite dos números (0 -100) e o % é utilizado para dividir; a função Range gera uma sequência.

Dentro do laço o número é dividido por dois, se o número for divisível por 2 o If recebe True, se o resto for 1 (False) o Else começa a trabalhar.

<img width="423" height="117" alt="image" src="https://github.com/user-attachments/assets/c64f3a78-f812-40f3-a55b-51dfdccb28dd" />


## Exercicio 2️⃣

- Requisito
  
Escreva um script que leia três números e mostre o maior e o menor deles. Use Lista.


- Foram utilizado na estrutura:
  
Lista

<img width="486" height="331" alt="image" src="https://github.com/user-attachments/assets/5022e77a-841b-4956-bcb2-bab05026eee8" />

## Exercicio 3️⃣

- *Requisito*
  
Faça um algoritmo que imprima o nome digitado pelo usuário na vertical em escada. 

- Foram utilizado na estrutura: 

Fatiamento de String ( [:i]), função len()  e  .upper

 o .upper é utilizado para deixar tudo maiusculo, a função len conta quantas letras o nome tem, a cada volta do laço o print pega a fatia do nome que vai do começo até a posição i

<img width="356" height="123" alt="image" src="https://github.com/user-attachments/assets/07c3badb-e2f1-443d-a8d2-68a8586a8d30" />


## Exercicio 4️⃣

- *Requisito*
  
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... (o próximo termo, a partir do terceiro (número 2), é sempre gerado a partir do somatório dos últimos dois). Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo usuário).

- *Foram utilizado na estrutura:*
  
o laço For roda o número de vezes que o user pediu, o código calcula o próximo valor [ proximo_termo = termo_atual + termo_anterior ] logo após os valores são atualizados; o anterior passa a ser o que estava no atual e o atual passa a ser o proximo 

<img width="658" height="443" alt="image" src="https://github.com/user-attachments/assets/9d0cf252-56be-40a0-9a59-079fceef0436" />


## Exercicio 5️⃣

- *Requisito*
  
Faça um programa que leia e valide as seguintes informações:
- Nome: maior que 3 caracteres;
- Idade: entre 0 e 150;
- Salário: maior que zero;
- Sexo: 'f' ou 'm';
- Estado Civil: 's', 'c', 'v', 'd'; 

- *Foram utilizado na estrutura:*
  
laço de repetição ( while e true), funçoes como; .strip, .lower, len(), in, break

Cada pergunta tem seu proprio bloco ( while, true) o if testa a regra, sendo verdadeira o código le o break que acaba quebrando o while, passando para a proxima pergunta. Se o user errar o if dá false e o break é ignorada e o while força a pergunta a acontecer de novo. 

<img width="707" height="596" alt="image" src="https://github.com/user-attachments/assets/4be85a1b-b011-44e1-adea-8305f88eaef2" />


## Exercicio 6️⃣

- *Requisito*
  
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
Dica: Utilize o operador aritmético `%`, que retorna o resto da divisão de dois números.

- *Foram utilizado na estrutura:*
  
Booleano (True e False), laço for e o operador %
a variavel e_primo vale true, iniciando o laço for que tenta dividir o numero digitado pelo user por 2, se a divição der 0 o numero não é primo e a variavel vai para false, o break encerra o laço.

<img width="592" height="341" alt="image" src="https://github.com/user-attachments/assets/e5e5847b-2c31-4f20-9b22-27e2874ecbc3" />


## Exercicio 7️⃣

- *Requisito*
  
Faça um algoritmo utilizando o laço FOR que descreva o Fatorial de um número digitado pelo usuário.
Fatorial é a multiplicação de um número por seus antecessores até o número 1
	ex: 4! = 4.3.2.1 = 24
	
- *Foram utilizado na estrutura:*
  
Laço `for` com operador acumulador de multiplicação (`*=`). O código inicia uma variável com o valor 1. O laço `for` realiza uma contagem que vai de 1 até o número que o usuário digitou, multiplicando e acumulando o valor atual pelos seus antecessores a cada volta do laço. 

<img width="632" height="220" alt="image" src="https://github.com/user-attachments/assets/283f58c3-5fca-45ab-8f2d-ae478a3cadf4" />


## Exercicio 8️⃣

- *Requisito*
  
Dada a lista
L = [5, 7, 2, 9, 4, 1, 3]
Escreva um programa que imprima as seguintes informações:
a) tamanho da lista.
b) maior valor da lista.
c) menor valor da lista.
d) soma de todos os elementos da lista.
e) lista em ordem crescente.
f) lista em ordem decrescente. 

- *Foram utilizado na estrutura:*
  
laço for, acumuladores matematicos (+=) if funçoes como .copy() e .sort()
o laço for passa por cada elemento que esta na lista.
o laço for passa por cada elemento da lista, assim a cada item ele passa adicionando 1 em uma variável de contagem para achar o tamanho, e adiciona o valor do próprio número na variável soma.
o maior e menor valor da lista funciona da mesma forma de estrutura do exercício 2 (dois)
a ordenação funciona através da cópia da lista com a função .copy() - afim de proteger a lista original. Após isso chama a função .sort() para alinhar os números em ordem crescente e .sort(reverse=true) para colocar em decrescente. 

<img width="553" height="561" alt="image" src="https://github.com/user-attachments/assets/ffd7e1f3-d661-47b2-a895-23cddc551699" />


## Exercicio 9️⃣

- *Requisito*

Dada a tabela em anexo , crie um dicionário que a represente.  

- *Foram utilizado na estrutura:*
  
Dentro do dicionário criado o produto é colocado como chave e o preço como valor, para printar a chave e o valor ao mesmo tempo existe o f”{produto}: R$ {preco:.2f}” 

tabela utilizada:


<img width="338" height="236" alt="image" src="https://github.com/user-attachments/assets/6e3dd4a8-7ed3-47a8-b2f1-19d46c11a775" />


<img width="480" height="238" alt="image" src="https://github.com/user-attachments/assets/05cb06cc-3db0-47de-b2cf-84a77205faae" />


## Exercicio 🔟

- *Requisito*
  
Utilizando o laço While faça um programa que peça uma senha ao usuário, e que imprima "Acesso liberado" apenas se o usuário digitar a senha corretamente. A senha devera ser a seguinte senha númerica : "676767".

- *Foram utilizado na estrutura:*
  
a cada volta do laço o input pede a senha, o if realiza uma checagem com a senha definida. se for identica retorna true, o print sai na tela e o break encerra, mas se for errada o if é ignorado, o programa printa e o while recomeça.

<img width="539" height="195" alt="image" src="https://github.com/user-attachments/assets/cfd8b3d0-8a21-4379-9751-7fc1ca1fec8a" />



## Exercicio 1️⃣1️⃣

- Requisito
  
Escreva um programa que peça um número de 1 a 10, e mostre a tabuada desse número. 

- Foram utilizado na estrutura:
  
o laço while confere o número escolhido pelo user (entre 1 a 10) com o número dentro desse intervalo o código multiplica o resultado vezes o número (numero * i)

<img width="597" height="197" alt="image" src="https://github.com/user-attachments/assets/63d24261-7cce-425f-84cb-bece730adb5b" />

