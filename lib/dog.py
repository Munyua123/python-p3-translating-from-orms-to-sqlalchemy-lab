from models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_table(Base, engine):
    engine = create_engine('sqlite:///dogs.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
    
def save(session, dog):
    dog = Dog (
        name = "joey",
        breed = "cocker spaniel"
    )
    session.add(dog)
    session.commit()
    

def get_all(session):
    dog_1 = Dog(
        name = "fanny",
        breed = "cockapoo"
    )
    dog_2 = Dog(
        name = 'conan',
        breed = 'chihuahua'
    )
    session.bulk_save_objects([dog_1,dog_2])
    session.commit()
    
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()
    

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name = name, breed = breed).first()
    

def update_breed(session, dog, breed):
    return session.query(Dog).filter_by(name = dog.name).update({Dog.breed : "bulldog"})
    