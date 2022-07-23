from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from dotenv import get_key
from pathlib import Path

def conexao():
    bd_path = Path('./docker/env/bd')
    BD_USUARIO = get_key(dotenv_path=bd_path,key_to_get='POSTGRES_USER')
    BD_SENHA = get_key(dotenv_path=bd_path,key_to_get='POSTGRES_PASSWORD')
    print(BD_USUARIO)
    print(BD_SENHA)
    if not (BD_USUARIO and BD_SENHA):
        raise ValueError('Conexão à base de dados não definida pelo ambiente')
    
    uri = f'postgresql://{BD_USUARIO}:{BD_SENHA}@localhost:5429/postgres'
    
    return sessionmaker(bind=create_engine(uri, poolclass=NullPool))()
