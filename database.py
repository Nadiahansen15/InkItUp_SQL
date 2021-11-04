from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
'''
SQLALCHEMY_DATABASE_URL = "mysql://pybc3f8ti1yuwjx9:dgk2n1lj37mqnzjj@c8u4r7fp8i8qaniw.chr7pe7iynqr.eu-west-1.rds.amazonaws.com:3306/b2sjcwjexw158glf"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

engine = create_engine('mysql://pybc3f8ti1yuwjx9:dgk2n1lj37mqnzjj@c8u4r7fp8i8qaniw.chr7pe7iynqr.eu-west-1.rds.amazonaws.com:3306/b2sjcwjexw158glf')
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
'''

import io
import sys
from sqlalchemy import create_engine, MetaData
from sqlacodegen.codegen import CodeGenerator

def generate_model(host, user, password, database, outfile = None):
    engine = create_engine(f'mysql://{user}:{password}@{host}:3306/{database}')
    metadata = MetaData(bind=engine)
    metadata.reflect()
    outfile = io.open(outfile, 'w', encoding='utf-8') if outfile else sys.stdout
    generator = CodeGenerator(metadata)
    generator.render(outfile)

if __name__ == '__main__':
    generate_model('c8u4r7fp8i8qaniw.chr7pe7iynqr.eu-west-1.rds.amazonaws.com', 'pybc3f8ti1yuwjx9', 'dgk2n1lj37mqnzjj', 'b2sjcwjexw158glf', 'InkItUpDB.py')