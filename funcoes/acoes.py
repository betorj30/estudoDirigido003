from interfaces import produtos

# =============================
# incluir produto
# =============================
def adicionarProduto():
    print("\n\n========== ADICIONAR PRODUTO ==========")
    nome = input("\nDigite o nome do produto: ")
    codigo = input("Digite o codigo ou RFID do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    minimo_estoque = int(input("Digite o estoque mínimo: "))

    if minimo_estoque <= 0 or quantidade <= 0:
        print("Estoque minimo ou quantidade inválidos. Tente novamente.")
        return

    produto_id = str(len(produtos) + 1)
    produtos[produto_id] = {
        "nome": nome,
        "codigo": codigo,
        "quantidade": quantidade,
        "minimo_estoque": minimo_estoque
    }
    print(f"\n\nProduto {nome} adicionado com sucesso!")

# =============================
# listar produto
# =============================
def listarProdutos():
    print("\n\n========== LISTA DE PRODUTOS ==========")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("+-----+--------------------------------------------------+----------+----------+----------+")
    print("| ID  | NOME                                             | CODIGO   | QTD      | EST MIN  |")
    print("+-----+--------------------------------------------------+----------+----------+----------+")

    for item in produtos:
        p = produtos[item]
        print(f"| {item:^3} | {p['nome']:48} | {p['codigo']:8} | {p['quantidade']:>8} | {p['minimo_estoque']:>8} |")
    
    print("+-----+--------------------------------------------------+----------+----------+----------+")

# =============================
# Atualizar produto
# =============================
def atualizarProduto():
    print("\n\n========== ATUALIZAR PRODUTO ==========")
    listarProdutos()
    produto_id = input("\nDigite o ID do produto que deseja atualizar: ")

    if produto_id not in produtos:
        print("Produto não encontrado.")
        return

    nome = input("Digite o novo nome do produto (deixe vazio para manter o atual): ")
    codigo = input("Digite o novo codigo ou RFID do produto (deixe vazio para manter o atual): ")
    quantidade = input("Digite a nova quantidade em estoque (deixe vazio para manter o atual): ")
    minimo_estoque = input("Digite o novo estoque mínimo (deixe vazio para manter o atual): ")

    if nome:
        produtos[produto_id]['nome'] = nome
    if codigo:
        produtos[produto_id]['codigo'] = codigo
    if quantidade:
        quantidade = int(quantidade)
        if quantidade > 0:
            produtos[produto_id]['quantidade'] = quantidade
        else:
            print("Quantidade inválida. Mantendo valor atual.")
    if minimo_estoque:
        minimo_estoque = int(minimo_estoque)
        if minimo_estoque > 0:
            produtos[produto_id]['minimo_estoque'] = minimo_estoque
        else:
            print("Estoque mínimo inválido. Mantendo valor atual.")

    print(f"\n\nProduto {produto_id} atualizado com sucesso!")

# =============================
# remover produto
# =============================
def removerProduto():
    print("\n\n========== REMOVER PRODUTO ==========")
    listarProdutos()
    produto_id = input("\nDigite o ID do produto que deseja remover: ")

    if produto_id not in produtos:
        print("Produto não encontrado.")
        return

    confirm = input(f"Tem certeza que deseja remover o produto {produtos[produto_id]['nome']}? (s/n): ")
    if confirm.lower() == 's':
        del produtos[produto_id]
        print("Produto removido com sucesso!")
    else:
        print("Remoção cancelada.")

# =============================
# listar estoque baixo de produto
# =============================
def listarEstoqueBaixo():
    print("\n\n========== PRODUTOS COM ESTOQUE BAIXO ==========")
    baixo_estoque = [p for p in produtos.values() if p['quantidade'] <= p['minimo_estoque']]

    if not baixo_estoque:
        print("Nenhum produto com estoque baixo.")
        return

    print("+-----+--------------------------------------------------+----------+----------+----------+")
    print("| ID  | NOME                                             | CODIGO   | QTD      | EST MIN  |")
    print("+-----+--------------------------------------------------+----------+----------+----------+")

    for item in produtos:
        p = produtos[item]
        if p['quantidade'] <= p['minimo_estoque']:
            print(f"| {item:^3} | {p['nome']:48} | {p['codigo']:8} | {p['quantidade']:>8} | {p['minimo_estoque']:>8} |")
    
    print("+-----+--------------------------------------------------+----------+----------+----------+")