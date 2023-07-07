# projeto-banco

Este projeto foi feito para o Bootcamp: Potência Tech powered by iFood | Ciências de Dados com Python do DIO.me

## FUNÇÕES

No menu principal, você poderá escolher entre:

| NUMERO | FUNÇÃO |
|:-------:|-----------|
| [1] | Realizar um depósito|
| [2] | Realizar um saque|
| [3] | Extrato bancário|
| [0] | Encerrar o programa.|

---

## INFORMAÇÕES SOBRE SAQUE

Ao optar pela opção saque, você poderá subtrair do saldo perante as seguintes condições:
* O saldo deve ser positivo (Realizar um depósito caso saldo seja igual a 0 (zero));
* Um saque individual não pode ser superior que R$500 (quinhentos reais);
* O usuário está limitado a 3 (três) saques diários.


# Informações sobre funcionamento
## Depósito

* Exige depósito maior que 0 (zero);

## Saque

* Exige saldo maior do que 0 (zero);
* Se Recusa sacar um valor maior que o saldo atual;
* Se recusa a sacar além do limite de 3 (três) saques diários
* Se recusa a sacar um valor superior a 500 (quinhentos) reais.

## Extrato

* Depósitos e saques são adicionados a uma lista de operações;
* Tal lista é imprimida juntamente ao saldo no momento do extrato.
