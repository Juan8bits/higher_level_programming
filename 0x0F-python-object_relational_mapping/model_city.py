#!/usr/bin/python3
""" Class definition of a 'city'
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """city Class"""
    __tablename__ = "cities"

    id = Column(Integer, autoincrement="auto",
                unique=True, nullable=False,
                primary_key=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
