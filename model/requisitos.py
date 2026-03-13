from database.conexao import conectar

# DEF RECUPERAR TAREFAS
def recuperar_tarefas(ativos:bool=False):
    conexao, cursor = conectar()

    if ativos == False:
        cursor.execute("SELECT cod_requsito, descricao, nivel, valor, situacao ")
    else:
        cursor.execute("SELECT cod_requisito, descricao, nivel, valor, situacao")

    requisitos = cursor.fetchall()
    conexao.close()
    return requisitos

# DEF SALVAR CADASTRAR
def cadastrar_requsito(descricao:str, nivel: str, valor:float):

    try:
        conexao, cursor = conectar()
        cursor.execute("""
                            INSERT INTO db_formativa (desc, nivel, val)
                            VALUES (%s, %s, %s)
                            """,
                            (descricao, nivel, valor)
                       )
        # Confirmando INSERT
        conexao.commit()
        conexao.close()

        return True
    except:
        return False
    

# DEF APAGAR TAREFA
def excluir(cod_requisito:int):
    conexao, cursor = conectar()
    try:
        cursor.execute("""
                        DELETE FROM tb_requisitos WHERE cod_requisio = %s
                       """,
                       [cod_requisito])
        
        conexao.commit()
        conexao.close()

        return True
    except:
        return False