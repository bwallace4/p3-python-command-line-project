#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pdb
from models import (Review, Director, Movie)

if __name__ == '__main__':
    engine = create_engine("sqlite:///band_lockers.db")
    session = Session(engine, future=True)


    pdb.set_trace()