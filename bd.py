# Função pegar o nome
def get_nomeprof(cursor, nome):

    cursor.execute(f'select nome from professor where nome="{nome}"')

    nome = cursor.fetchone()

    cursor.close()


    return nome