import sqlalchemy
import databases


DATABASE_URL = "sqlite:///./nvish.db"
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
employee_table = sqlalchemy.Table("employee",
                                  metadata,
                                  sqlalchemy.Column("empid", sqlalchemy.Integer, primary_key=True),
                                  sqlalchemy.Column("name", sqlalchemy.String)
                                  )

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
