import pymysql

conexao = pymysql.connect(
    host = "localhost",
    user = "root", 
    password = "123456",
    database = "sistema_escolar",
    charset = "utf8mb4",
    cursorclass = pymysql.cursors.DictCursor
)

#EXERCICIO 1

# def listar_disciplinas(conexao):
#     try:
#         with conexao.cursor() as cursor:
#             cursor.execute("""
#                 SELECT
#                     d.disciplina_id,
#                     d.nome_disciplina,
#                     d.carga_horaria,
#                     COUNT(m.matricula_id) AS total_alunos
#                 FROM disciplinas d
#                 LEFT JOIN turmas t
#                     ON d.disciplina_id = t.disciplina_id
#                 LEFT JOIN matriculas m
#                     ON t.turma_id = m.turma_id
#                     AND m.status_matricula = 'Matriculado'
#                 GROUP BY d.disciplina_id, d.nome_disciplina, d.carga_horaria
#                 ORDER BY total_alunos DESC
#             """)
            
#             resultados = cursor.fetchall()
            
#             # print("ID | Nome da Disciplina | Carga Horária | Nº de Alunos Matriculados")
#             # print("-" * 70)
#             for row in resultados:
#                 print(f"{row['disciplina_id']} | {row['nome_disciplina']} | {row['carga_horaria']}h | {row['total_alunos']} alunos")
    
#     except Exception as e:
#         print("Erro ao listar disciplinas:", e)
# listar_disciplinas(conexao)
# conexao.close()


#EXERCICIO 2

# def relatorio_turmas(conexao):
#     try:
#         with conexao.cursor() as cursor:
#             cursor.execute("""
#                 SELECT
#                     t.turma_id,
#                     d.nome_disciplina,
#                     p.nome AS nome_professor,
#                     CONCAT(t.ano, '/', t.semestre) AS semestre,
#                     COUNT(DISTINCT m.matricula_id) AS total_alunos,
#                     ROUND(AVG(n.nota), 2) AS media_turma
#                 FROM turmas t
#                 LEFT JOIN disciplinas d ON t.disciplina_id = d.disciplina_id
#                 LEFT JOIN professores p ON t.professor_id = p.professor_id
#                 LEFT JOIN matriculas m ON t.turma_id = m.turma_id
#                     AND m.status_matricula = 'Matriculado'
#                 LEFT JOIN notas n ON m.matricula_id = n.matricula_id
#                 GROUP BY t.turma_id, d.nome_disciplina, p.nome, t.ano, t.semestre
#                 ORDER BY t.ano DESC, t.semestre DESC
#             """)
            
#             resultados = cursor.fetchall()
            
#             print("Turma | Disciplina | Professor | Semestre | Nº Alunos | Média da Turma")
#             print("-" * 80)
#             for row in resultados:
#                 media = row['media_turma'] if row['media_turma'] is not None else "N/A"
#                 print(f"{row['turma_id']} | {row['nome_disciplina']} | {row['nome_professor']} | {row['semestre']} | {row['total_alunos']} alunos | Média: {media}")
    
#     except Exception as e:
#         print("Erro ao gerar relatório de turmas:", e)

# relatorio_turmas(conexao)
# conexao.close()


# def relatorio_turmas(conexao):
#     try:
#         with conexao.cursor() as cursor:
#             cursor.execute("""
#                 SELECT
#                     t.turma_id,
#                     d.nome_disciplina,
#                     p.nome AS nome_professor,
#                     CONCAT(t.ano, '/', t.semestre) AS semestre,
#                     COUNT(DISTINCT m.matricula_id) AS total_alunos,
#                     ROUND(SUM(n.nota * n.peso) / NULLIF(SUM(n.peso), 0), 2) AS media_turma
#                 FROM turmas t
#                 LEFT JOIN disciplinas d ON t.disciplina_id = d.disciplina_id
#                 LEFT JOIN professores p ON t.professor_id = p.professor_id
#                 LEFT JOIN matriculas m ON t.turma_id = m.turma_id
#                     AND m.status_matricula = 'Matriculado'
#                 LEFT JOIN notas n ON m.matricula_id = n.matricula_id
#                 GROUP BY t.turma_id, d.nome_disciplina, p.nome, t.ano, t.semestre
#                 ORDER BY t.ano DESC, t.semestre DESC
#             """)
            
#             resultados = cursor.fetchall()
            
#             print("Turma | Disciplina | Professor | Semestre | Nº Alunos | Média da Turma")
#             print("-" * 90)
#             for row in resultados:
#                 media = row['media_turma'] if row['media_turma'] is not None else "N/A"
#                 print(f"{row['turma_id']} | {row['nome_disciplina']} | {row['nome_professor']} | {row['semestre']} | {row['total_alunos']} alunos | Média: {media}")
    
#     except Exception as e:
#         print("Erro ao gerar relatório de turmas:", e)
        
# relatorio_turmas(conexao)
# conexao.close()


# EXERCICIO 3
