# Sistema de Contas Bancárias em Python

Este projeto demonstra um simples sistema de contas bancárias em Python, utilizando **Programação Orientada a Objetos (POO)**. O código contém uma classe principal (`Conta`) e duas subclasses: `ContaCorrente` e `ContaPoupança`.

## Funcionalidades

* Criar contas bancárias com número, titular e saldo inicial.
* Depositar valores (somente valores positivos).
* Sacar valores com regras:

  * Valor deve ser positivo.
  * Não pode superar o saldo.
  * Limite máximo de saque: **R$ 500,00**.
* Exibir saldo atual.
* Conta Poupança possui rendimento automático de **5%**.

## Estrutura das Classes

### **Classe Conta (classe base)**

Contém os atributos e métodos principais:

* `depositar_valor()`
* `sacar_valor()`
* `exibir_saldo()`

### **ContaCorrente**

Herda todos os métodos da classe `Conta`.

### **ContaPoupança**

Herda `Conta` e adiciona:

* `render_juros()` → aplica 5% de rendimento sobre o saldo.

## Exemplo de Funcionamento

O código cria dois objetos:

* Uma **Conta Corrente** chamada `conta1`.
* Uma **Conta Poupança** chamada `conta2`.

Ambas permitem depósitos, saques e exibição de saldo. A poupança também permite aplicar juros.

## Como executar

Basta rodar o arquivo Python:

```
python ContaBancária.py
```

Os valores de depósito e saque serão solicitados no terminal.

---

Feito de forma simples e didática para aprendizado de POO em Python.
