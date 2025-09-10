from interfaces import produtos
from funcoes.acoes import adicionarProduto, listarProdutos, atualizarProduto, removerProduto, listarEstoqueBaixo

# =============================
# MENU PRINCIPAL
# =============================
def main():

    while True:
        print("\n\n========== MENU DE PRODUTOS ==========")
        print("1 - Listar produtos")
        print("2 - Adicionar produto")
        print("3 - Atualizar produto")
        print("4 - Remover produto")
        print("5 - Listar produtos com estoque baixo")
        print("0 - Sair")
        escolha = input("\nEscolha: ")
        
        if escolha == "1": listarProdutos()
        elif escolha == "2": adicionarProduto()
        elif escolha == "3": atualizarProduto()
        elif escolha == "4": removerProduto()
        elif escolha == "5": listarEstoqueBaixo()
        elif escolha == "0":
            print("\nSaindo...")
            break
        else:
            print("Opção inválida!")

                                                                         
if __name__ == "__main__":
    main()