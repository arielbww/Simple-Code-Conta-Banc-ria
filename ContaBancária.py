# Classe CONTA criada
class Conta:
    def __init__(self, _numero, _titular, _saldo):
        self._numero = _numero
        self._titular = _titular
        self._saldo = _saldo
# Método para depósito
    def depositar_valor(self):
        deposito = float(input("Quanto você quer depositar? "))
        if deposito <= 0: 
            print("Erro, a quantia de depósito deve ser positiva!")
            return
        
        self._saldo += deposito

        print(f"Depósito de R${deposito:.2f} realizado para {self._titular}.") 
        print(f"Saldo atual: R${self._saldo:.2f}")
# Método para saque
    def sacar_valor(self):
        valor_sacar = float(input("Quanto você quer sacar? "))
        
        if valor_sacar <= 0:
            print("Erro: o valor de saque deve ser positivo!")

        #Valor do saque não deve ser maior que 500 e nem do que o saldo da conta (evita saldo negativo)
        if valor_sacar > self._saldo or valor_sacar > 500:
            print(f"Saque de R${valor_sacar:.2f} inválido.")
            print(f"Você não possui esse saldo. Saldo atual: R${self._saldo:.2f}")
            print("LIMITE PARA SAQUE: R$500,00")

        else:
            self._saldo -= valor_sacar
            print(f"Saque de R${valor_sacar:.2f} concluído com sucesso!")
            print(f"Novo saldo: R${self._saldo:.2f}")
# Método para exibir o saldo atual
    def exibir_saldo(self):
        print("-=" * 20)
        print(f"Olá, {self._titular}")
        print(f"Esse é o seu saldo atual: R${self._saldo:.2f}")

# Subclasse Conta Corrente: HERDA TUDO DA CLASSE PAI(CONTA)
class ContaCorrente(Conta):
    def __init__(self, _numero, _titular, _saldo):
        super().__init__(_numero, _titular, _saldo)

# Subclasse Conta Poupança: TAMBÉM HERDA TUDO DA CLASSE PAI(CONTA)            
class ContaPoupança(Conta):
    def __init__(self, _numero, _titular, _saldo):
        super().__init__(_numero, _titular, _saldo)
        self._rendimento = 0.05
# Método para rendimento de juros de 5%
    def render_juros(self):
        juros = self._saldo * self._rendimento
        self._saldo += juros
        print(f"Juros de R${juros:.2f} aplicados com sucesso!")
        print(f"Saldo atual após o rendimento {self._saldo:.2f}")

#OBJETO CRIADO (Conta Corrente!)
print("---  Conta Corrente  ---")
conta1 = ContaCorrente(123, "Ariel Nunes", 0)
conta1.depositar_valor()
conta1.exibir_saldo()
conta1.sacar_valor() 
conta1.exibir_saldo() 

print("\n" + "-=" * 20 + "\n")

#OUTRO OBJETO CRIADO (Conta Poupança!)
print("--- Conta Poupança ---")
conta2 = ContaPoupança(456, "Ariel Nunes", 0) 
conta2.depositar_valor() 
conta2.render_juros()
conta2.sacar_valor() 
conta2.exibir_saldo()
