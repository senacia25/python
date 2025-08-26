import pymysql



conexao = pymysql.connect(
    host = "localhost",   #endereço do banco     host endereco de algma coisa pode sr ip
    user = "root",        #usuário
    password = "123456",   #senha do MySQL
    database = "sistema_escolar",   #nome do banco
    charset = "utf8mb4",    #padrão de acentuação
    cursorclass = pymysql.cursors.DictCursor   #retorna linhas como dicionário (chave:coluna)
) 

# print("Conectado com sucesso")
# conexao.close()  # sempre tem que fechar o bc


# #enviando um select para o banco de dados
# with conexao.cursor() as cursor:
#     cursor.execute("SELECT * FROM alunos")
#     alunos = cursor.fetchall() #retornar todos os alunos
    
#     #mostrar os dados
#     for aluno in alunos:
#         print(f"Aluno: {aluno["nome"]} - Email: {aluno["email"]} - Semestre: {aluno["semestre_atual"]}")


#codigo inserir um novo usuario
# with conexao.cursor() as cursor:
#     sql = "INSERT INTO alunos (nome, email, telefone, data_nascimento, curso_id, semestre_atual, status_aluno, data_matricula) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" # %s ajuda na segurança
    
#     valores = ("LUciana Souza", "Luciana@luciana@gmail.com", "4999999999", "2001-03-12", 1, 2, "Ativo", "2024-08-01")
#     cursor.execute(sql,valores)
#     conexao.commit() #salvando banco


#Atualizar um usuário
# with conexao.cursor() as cursor:
#     sql = "UPDATE alunos SET telefone = %s WHERE aluno_id = %s"
#     valores = ("(49) 9958-5487", 601)
#     cursor.execute(sql,valores)
#     conexao.commit()


# Deletar dados do banco de dados
# try:
#     with conexao.cursor() as cursor:   #CURSOR PERMITIR ESCREVER SQL
#         sql = "DELETE FROM alunos WHERE aluno_id = %s" # %s questão de segurança
#         valores = (601)
#         cursor.execute(sql,valores) #(sql,601 elimina variavel valores)
#         conexao.commit() # confirma a mudança
# except Exception as erro:
#     print("Deu um erro no banco:", erro)

# finally:            #executa se der erro ou não
#     conexao.close()


