import os

import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker

import models

db_ip = os.environ['db_ip']
db_port = os.environ['db_port']
db_name = os.environ['db_name']
db_pwd = os.environ['db_pwd']
db_user = os.environ['db_user']
DSN = f'postgresql://{db_user}:{db_pwd}@{db_ip}:{db_port}/{db_name}'
engine = sq.create_engine(DSN)
models.create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

models.load_data(session)

session.commit()
while True:
    user_input = input('Enter publisher name or ID (or zero to exit): ')
    if user_input == '0':
        session.close()
        exit()
    elif user_input.isdecimal():
        my_records = models.get_by_id(session, int(user_input))
        models.output(my_records)
        # for id, name in my_records.:
        #     print(id, name)
    else:
        my_records = models.get_by_name(session, user_input)
        models.output(my_records)
