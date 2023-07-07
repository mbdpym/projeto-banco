import sys

menu = 1
saldo = 0
SAQUES_DIARIOS = 0
voltar = 0
exit_input = False
operacoes = []
n = 0

while menu:
    print(
        """

$-----BANCO IMAGINÁRIO-----$
#                          #
#      [1] - Depósito      #
#      [2] - Saque         #
#      [3] - Extrato       #
#      [0] - Cancelar      #
#                          #
$--------------------------$

"""
    )

    user_input = input("Por favor, escolha uma opção: ")

    while user_input not in ["1", "2", "3", "0"]:
        print("Opção inválida.")
        user_input = input("Por favor, escolha novamente: ")

    if user_input == "1":
        print("$-----DEPÓSITO-----$")
        continuar = 1
        deposit_input = 0
        while continuar == 1:
            deposit_input = int(input("Digite o valor a ser depositado: "))
            while deposit_input < 0:
                deposit_input = int(
                    input("Valor inválido. Digite um valor acima de 0 (zero): ")
                )

            operacoes.append(f"+ R$ {deposit_input}")
            n += 1
            saldo += deposit_input
            deposit_input = 0

            print(f"seu saldo atual é {saldo}")
            continuar = int(
                input(
                    """Você deseja realizar mais um depósito?

[1] Sim
[0] Não

"""
                )
            )

            while continuar > 1 and continuar < 0:
                continuar = int(
                    input(
                        """Você deseja realizar mais um depósito?
                                      
[1] Sim
[0] Não

"""
                    )
                )

    elif user_input == "2":
        print("$-----SAQUE-----$")
        continuar = 1
        
        if(saldo == 0):
            print("Você não tem saldo! Por favor, realize um depósito primeiro.")
            exit_input = input("Digite qualquer valor para sair...")
        else:
            if SAQUES_DIARIOS == 3:
                voltar = 1
                exit = input(
                    "Você atingiu o limite máximo de três saques diários. Digite qualquer valor para continuar"
                )

            while continuar == 1 and voltar != 1:
                saque_input = int(input("Digite o valor a sacar:"))
                while saque_input < 0 or saque_input > 500:
                    saque_input = int(
                        input(
                            "Valor inválido. Digite um valor entre 0 (zero) e 500 (quinhentos): "
                        )
                    )
                while(saque_input > saldo):
                        print(f"Saldo atual: {saldo}")
                        input(
                            "Digite um valor inferior ao seu saldo atual: "
                        )

                operacoes.append(f"- R$ {saque_input}")
                n += 1
                saldo = saldo - saque_input
                print(f"seu saldo atual é {saldo}")

                SAQUES_DIARIOS += 1

                if SAQUES_DIARIOS == 3:
                    voltar = 1
                    exit_input = input(
                        "Você atingiu o limite máximo de três saques diários. Digite qualquer valor para continuar..."
                    )

                elif SAQUES_DIARIOS < 3:
                    continuar = int(
                        input(
                            """Você deseja realizar mais um saque?

    [1] Sim
    [0] Não


    """
                        )
                    )
                while continuar > 1 and continuar < 0:
                    continuar = int(
                        input(
                            """Você deseja realizar mais um saque?
                                        
[1] Sim
[0] Não


"""
                        )
                    )

    elif user_input == "3":
        print("$-----EXTRATO-----$")
        for element in operacoes:
            print(element)

        print(f"Seu saldo atual é de {saldo}")
        exit_input = input("Digite qualquer valor para voltar...")

    else:
        print("CANCELAR")
        sys.exit()
