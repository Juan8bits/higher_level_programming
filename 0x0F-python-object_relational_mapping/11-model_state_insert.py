#!/usr/bin/python3
""" Script that adds the State object Louisiana to a database.
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    new_s = State(name='Louisiana')
    session.add(new_s)
    session.commit()
    print('{}'.format(new_s.id))
    session.close()
