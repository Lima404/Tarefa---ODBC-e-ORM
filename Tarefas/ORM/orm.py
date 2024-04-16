from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('postgresql://postgres:postgres@172.18.0.2:5432/atividade_db')

metadata = MetaData()
metadata.reflect(bind=engine)

tabela_projeto = Table('projeto', metadata, autoload_with=engine)
tabela_atividade = Table('atividade', metadata, autoload_with=engine)

stmt1 = tabela_atividade.insert().values(descricao='ES - Atividade 3', projeto=4, data_inicio='2018-06-27', data_fim='2018-07-31')

stmt2 = tabela_projeto.update().\
            where(tabela_projeto.c.codigo == 4).\
            values(responsavel=2)

with engine.connect() as connection:
    result = connection.execute(stmt1)

    result = connection.execute(stmt2)

    result = connection.execute(tabela_projeto.select())
    for row in result:
        print(row)

    result = connection.execute(tabela_atividade.select())
    for row in result:
        print(row)