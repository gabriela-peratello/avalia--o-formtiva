from database.conexao import conectar

# DEF SALVAR CADASTRAR
def cadastrar_requsito(desc:str, nivel: str, val:float):
    try:
        conexao, cursor = conectar()
        cursor.execute("""
                            INSERT INTO db_formativa (desc, nivel, val)
                            VALUES (%s, %s, %s)
                            """,
                            (desc, nivel, val)
                       )
        # Confirmando INSERT
        conexao.commit()
        conexao.close()

        return True
    except:
        return False