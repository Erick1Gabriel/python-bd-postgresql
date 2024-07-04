from conexao import conecta_db


def consultar(conexao):
    cursor = conexao.cursor()
    # Execução do Select no banco de dados
    cursor.execute("select id,login from usuario")
    # Recuperar os registros
    registros = cursor.fetchall()
    print("|-----------------------------------|")
    for registro in registros:
        print(f"| ID ..:  {registro[0]}   - Nome ..:   {registro[1]}")
        print("|-----------------------------------|")

def inserir(conexao):
    cursor = conexao.cursor()
    print = ('Cadastro de usuario') 
    login = input('login:')
    senha = input('senha :')
    admin = input("Admin : (S- Sim) ou (N- Nao)")
    sql_insert = "insert into usuario (login,senha,admin) values ('"+ login +  "','"+ senha +"','"+ senha +"')"
    cursor.execute(sql_insert)
    conexao.commit()
        
def alterar(conexao):
    cursor = conexao.cursor()
    print = ('Cadastro de usuario') 
    login = input('login:')
    senha = input('senha :')
    sql_update = "update usuario set senha  ='" +  senha + "'where login =  '"  + login +  "'"
    cursor.execute(sql_update)
    conexao.commit()


def deletar(conexao):
    cursor = conexao.cursor()
    id = input("Digite o ID: ")
    sql_delete = "delete from  usuario where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()


def menu_usuario_admin(opcao):
    print("|--------------------------------|")
    print("|       Menu -> Usuario          |")
    print("|--------------------------------|")
    print("|     1 - Consultar Usuario      |")
    print("|     2 - Inserir Usuario        |")
    print("|     3 - Alterar Usuario        |")
    print("|     4 - Deletar Usuario        |")
    print("|     5 - Sair do Usuario        |")
    print("|--------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            consultar(conexao)
        elif opcao == "2":
            inserir(conexao)
        elif opcao == "3":
            alterar(conexao)
        elif opcao == "4":
           deletar(conexao)
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")



def menu_usuario_not_admin(opcao):
    print("|--------------------------------|")
    print("|       Menu -> Usuário          |")
    print("|--------------------------------|")
    print("|     3 - Trocar  Senha          |")
    print("|     5 - Sair do Usuário        |")
    print("|--------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")
     
        if opcao == "3":
            alterar(conexao)  
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")

def menu_usuario(opcao,admin):
    if admin == "S":
        menu_usuario_admin(opcao)
    else:
        menu_usuario_not_admin(opcao)


