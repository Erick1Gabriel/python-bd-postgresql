from conexao import conecta_db
from datetime import datetime

def insert_venda(conexao, venda):
    cursor = conexao.cursor()
    sql_insert = """
        insert into venda (cliente_id,numero_venda,data_venda,valor_venda)
        values (%s, %s, %s, %s) RETURNING id;
        """
    cursor.execute(sql_insert,venda)
    venda_id =cursor.fetchone()[0]
    conexao.commit()
    return venda_id


    
    
        

def consultar(conexao):
    print("consultar")

def criar_venda(conexao):
    venda = alimentar_venda()
    itens_venda = alimentar_itens()
    print(venda)
    print(itens_venda)

    venda_id =insert_venda(conexao,venda)
    print(venda_id)


def alimentar_venda():
    id_cliente = input("Digite o id do cliente")
    numero_venda = 0
    data_venda = datetime.now()
    valor_venda = 0 #Calcular o total dos itens
    return(id_cliente,numero_venda,data_venda,valor_venda)

def alimentar_itens():
    itens_venda = []
    while(True):
        produto_id = int(input("Digite o id do produto :"))
        quantidade  = int(input("Digite a quantidade : "))
        preco_unitario = float(input("Digite o preco Unitario :"))
        itens_venda.append({"produto_id":produto_id,"quantidade":quantidade,"preco_uniatrio":preco_unitario})

        continua = input("Deseja adicionar outro item ? (S/N):")
        if continua == "N":
            break

    return itens_venda
                        
def menu_vendas(opcao):
    print("|--------------------------------|")
    print("|       Menu -> Vendas           |")
    print("|--------------------------------|")
    print("|     1 - Consutar Vendas        |")
    print("|     2 - Inserir Vendas         |")
    print("|     2 - Sair do  Usuario       |")
    print("|--------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")
     
        if opcao == "1":
            consultar(conexao)  
        if opcao == "2":
            criar_venda(conexao)
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")

