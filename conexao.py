import psycopg2

def conecta_db():
    con = psycopg2.connect(host="localhost",
                           database="mercearia",
                           user="postgres",
                           password="postgres",
                           port=5432)
    return con 


def consultar (conexao):
  cursor = conexao.cursor()
  # Execucao do select no banco de dados 
  cursor.execute("select id , nome from categoria")
  # Recuperar os registros
  registros = cursor.fetchall() 
  print ("|---------------------------------|")
  for registro in registros:
      print(f"|ID..:  {registro[0]} - Nome ..:  {registro[1]}")
      print("----------------------------------|")

def inserir(conexao):
    cursor = conexao.cursor()
    nome_categoria = input ('Digite o nome da categoria:')
    sql_insert = "'inset into categoria (nome ) values ('" + nome_categoria +"')"
    cursor.execute(sql_insert)
    conexao.commit()

def alterar (conexao):
   cursor = conexao.cursor()
   id = input("Digite o ID:")
   nome_categoria = input('Digite o nome da categoria:')
   sql_delete = "delete from categoria where id = " + id 
   cursor.execute(sql_delete)
   conexao.commit()  


def deletar (conexao):
   cursor = conexao.cursor()
   id = input("Digite o ID:")
   nome_categoria = input('Digite o nome da categoria:')
   sql_update = "update categoria set nome ='"+ nome_categoria + "' where id =" + id 
   cursor.execute(sql_update)
   conexao.commit()  
   
if __name__ == "__main__":

    print("|------------------------------------|")
    print("|     Menu-> Categoria               |")
    print("|------------------------------------|")
    print("|    1- Consultar Categoria          |")
    print("|    2- Inserir Categoria            |")
    print("|    3- Alterar Categoria            |")
    print("|    4- Deletar Categoria            |")
    print("|    5- Sair do  Sistemas            |")  

    conexao = conecta_db()
    while True: 
        opcao = input ("Escolha uma opcao:")
        if opcao == "1":
            consultar(conexao)
        elif opcao == "2":
            inserir(conexao)
        elif opcao =="3":
            alterar(conexao)
        elif opcao == "4":
            deletar(conexao)
        elif opcao == "5":
           break
        else:
          print ("Opcao invalida, tente novamente")

     
        


     

        


    

  