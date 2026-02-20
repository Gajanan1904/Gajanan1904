# orm :((object relational maping)) is the translator between python and sql 
# sql        python
# table--> class
# row --> object
# column --> variable

#import create_engine to connect the database

from sqlalchemy import create_engine
engine=create_engine("sqlite:////school.db")

# sqlite database
# filename is school.db
# will be created if not exist

print("database connected")

