from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


base=declarative_base()
engine=create_engine('postgresql://postdb:postdb616@localhost:5432/btech')


Sessions=sessionmaker(bind=engine,autoflush=False)
