import os
import json 
from datetime import datetime
from typing import List, Dict, Any


DATA_FILE = 'banco_dados.json'  

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)
        

def load_data() -> List[Dict[str, Any]]:
    """Load data from the JSON file."""
    with open(DATA_FILE, 'r') as file:
        return json.load(file)


def save_data(data: List[Dict[str, Any]]) -> None:
    """Save data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


def depositar(valor: float, descricao: str) -> None:
    """Deposit money into the account."""
    data = load_data()
    data.append({
        'tipo': 'depósito',
        'valor': valor,
        'descricao': descricao,
        'data': datetime.now().isoformat()
    })
    save_data(data)
    print(f'Depósito de R${valor:.2f} realizado com sucesso!')


def sacar(valor: float, descricao: str) -> None:
    """Withdraw money from the account."""
    data = load_data()
    data.append({
        'tipo': 'saque',
        'valor': -valor,
        'descricao': descricao,
        'data': datetime.now().isoformat()
    })
    save_data(data)
    print(f'Saque de R${valor:.2f} realizado com sucesso!')


def extrato() -> None:
    """Print the account statement."""
    data = load_data()
    if not data:
        print("Nenhuma transação registrada.")
        return
    
    print("Extrato:")
    for transacao in data:
        tipo = transacao['tipo']
        valor = transacao['valor']
        descricao = transacao['descricao']
        data_transacao = transacao['data']
        print(f"{data_transacao} - {tipo.capitalize()}: R${valor:.2f} - {descricao}")
   

def main():
    while True:
        print("\nMenu:")
        print("0. Saldo")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Digite o valor do depósito: "))
            if valor <= 0:
                print("Valor de depósito inválido.")
                continue    
            descricao = input("Digite a descrição do depósito: ")
            depositar(valor, descricao)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: "))
            if valor > saldo:
                print("Valor de saque inválido.")
                continue
            descricao = input("Digite a descrição do saque: ")
            sacar(valor, descricao)
        elif opcao == '3':
            extrato()
        elif opcao == '4':
            print("Saindo...")
            break
        elif opcao == '0':
            data = load_data()
            saldo = sum(transacao['valor'] for transacao in data)
            print(f"Saldo atual: R${saldo:.2f}")
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
    
