from datetime import date

def formatar_nome(nome):
    return nome.strip().title()

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            if preco < 0:
                print("O preço não pode ser negativo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o preço.")
            
    categoria = input("Digite a categoria do produto: ")
    return (formatar_nome(nome), preco, categoria)

def salvar_produtos(produto):
    with open("produtos.txt", "a", encoding="utf-8") as arquivo:
        linha = f"{produto[0]};{produto[1]:.2f};{produto[2]}\n" 
        arquivo.write(linha)

def listar_produtos():
    print("\n--- Produtos Cadastrados (Função Original) ---")
    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            tem_produtos = False
            for linha in arquivo:
                partes = linha.strip().split(";")
                if len(partes) == 3:
                    nome, preco_str, categoria = partes
                    preco = float(preco_str) 
                    print(f"Produto: {nome} | Preço: R${preco:.2f} | Categoria: {categoria}")
                    tem_produtos = True
            
            if not tem_produtos:
                print("O arquivo de produtos está vazio ou não possui entradas válidas.")
                
    except FileNotFoundError:
        print("Nenhum produto cadastrado ainda.")
    print("--------------------------------------------\n")

def calcular_idade():
    """Calcula a idade de uma pessoa pedindo o ano de nascimento."""
    print("\n--- 1. Calcular Idade ---")
    while True:
        try:
            ano_nascimento = int(input("Digite o ano em que você nasceu): "))
            
            ano_atual = date.today().year
            
            if ano_nascimento > ano_atual or ano_nascimento < 1900:
                print(f"Ano de nascimento inválido. Deve ser entre 1900 e {ano_atual}.")
                continue
                
            idade = ano_atual - ano_nascimento
            print(f"\nSua idade é de aproximadamente: {idade} anos.")
            break
            
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def calcular_preco_compra():
    """Calcula o preço total da compra baseado no preço unitário e quantidade."""
    print("\n--- 2. Calcular Preço da Compra ---")
    
    while True:
        try:
            preco_unitario = float(input("Digite o preço unitário do item (R$): "))
            if preco_unitario < 0:
                print("O preço unitário não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Entrada inválida para o preço. Digite um número.")
            
    while True:
        try:
            quantidade = int(input("Digite a quantidade de itens comprados: "))
            if quantidade <= 0:
                print("A quantidade deve ser um número inteiro positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida para a quantidade. Digite um número inteiro.")
            
    preco_total = preco_unitario * quantidade
    
    print(f"\n--- Resultado da Compra ---")
    print(f"Preço Unitário: R${preco_unitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço Total da Compra: R${preco_total:.2f}")
    print("----------------------------")
    

def menu():
    """Função principal que exibe o menu solicitado."""
    while True:
        print("\n===============================")
        print("     menu do meu programa    ")
        print("===============================")
        print("1 - Calcular Idade")
        print("2 - Calcular Preço da Compra")
        print("3 - Sair")
        print("===============================")
        
        escolha = input("Escolha uma opção (1, 2 ou 3): ")
        
        if escolha == '1':
            calcular_idade()
        elif escolha == '2':
            calcular_preco_compra()
        elif escolha == '3':
            print("Você acabou de sair, obrigado pela participação.")
            break
        else:
            print("Erro, você tem que escolher outras opçoẽs para continuar o programa.")

# Executa o menu quando o script é iniciado
if __name__ == "__main__":
    menu()