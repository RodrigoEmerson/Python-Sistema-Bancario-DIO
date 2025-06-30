# Python-Sistema-Bancario-DIO

## Descrição

Este projeto é um sistema bancário simples desenvolvido em Python, como desafio da Digital Innovation One (DIO). O sistema permite realizar operações básicas como **depósito**, **saque** e **extrato** de uma conta bancária fictícia via terminal.

## Funcionalidades

- Realizar depósitos na conta
- Realizar saques com limite de valor e quantidade diária
- Visualizar extrato das operações realizadas

## Pré-requisitos

- Python 3.8 ou superior instalado em sua máquina

## Instalação

Não há dependências externas.

## Como Executar

Execute o arquivo principal do sistema (por exemplo, `main.py`):

```bash
python main.py
```

Siga as instruções exibidas no terminal para realizar as operações bancárias.

## Exemplo de Uso

Ao executar o programa, será exibido um menu semelhante a este:

```
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> 
```

- Para depositar, digite `1` e informe o valor.
- Para sacar, digite `2` e informe o valor (respeitando os limites).
- Para ver o extrato, digite `3`.
- Para sair, digite `4`.

## Observações

- O sistema utiliza um arquivo JSON para armazenar e persistir os dados das operações bancárias.
- Limites de saque e quantidade diária podem ser configurados no código.

## Autor

Desenvolvido por [Rodrigo](https://github.com/RodrigoEmerson) para o bootcamp da Digital Innovation One.

## Licença

Este projeto está licenciado sob a licença MIT.
