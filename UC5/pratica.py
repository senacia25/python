import pymysql

conexao = pymysql.connect(
    host = "localhost",
    user = "root", 
    password = "123456",
    database = "sistema_escolar",
    charset = "utf8mb4",
    cursorclass = pymysql.cursors.DictCursor
)

# with conexao.cursor() as cursor:
#     cursor.execute("SELECT * FROM alunos")
#     alunos = cursor.fetchall()
    
#     for aluno in alunos:
#         print(f"Aluno: {aluno["nome"]} - Email: {aluno["email"]} - Semestre: {aluno["semestre_atual"]} - Status: {aluno["status_aluno"]}")


# try:
# with conexao.cursor() as cursor:
#     nome = input("Digite o nome do aluno:")
#     email = input("Digite o email:")
#     telefone = input("Digite o telefone:")
#     data_nasc = input("Digite a data de nascimento:")
#     curso_id = input("Digite o curso id:")
#     semestre_atual = input("Digite o semestre atual:")
#     status_aluno = input("Digite o status do aluno:")
#     data_matricula = input("Digite a data da matricula:")
        
#     sql = "INSERT INTO alunos (nome, email, telefone, data_nascimento, curso_id, semestre_atual, status_aluno, data_matricula) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#     cursor.execute(sql,(nome, email, telefone, data_nasc, curso_id, semestre_atual, status_aluno, data_matricula))
#     conexao.commit()
#     print("Aluno cadastrado com sucesso!!")
# except Exception as erro:
#     print("Deu um erro no banco:", erro)

# finally:            #executa se der erro ou não
#     conexao.close()



