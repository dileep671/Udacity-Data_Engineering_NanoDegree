import cassandra
from cassandra.cluster import Cluster
from cql_queries import create_table_queries, drop_table_queries

def create_database():
    """
    - Creates the database
    - Returns the connection and cursor
    """
    
    # connect to default database
    cluster = Cluster(['127.0.0.1']) #If you have a locally installed Apache Cassandra instance
    session = cluster.connect()

    
    # Drop sparkifydb database if already exists, or create sparkify database with UTF8 encoding
    session.execute("""DROP KEYSPACE IF EXISTS sparkify;""")
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS sparkify
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }""")
    
    # Set the keyspace to sparkify
    session.set_keyspace('sparkify')
   
    return cluster, session


def drop_tables(session):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print("Error: Dropping table")
            print(e)


def create_tables(session):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    create_table_queries
    for query in create_table_queries:
        try:
            session.execute(query)
        except Exception as e:
            print("Error: Creating table")
            print(e)

def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it. 
    
    - Drops all the tables.
    drop_tables()
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    print(" Create database sparkify ")
    cluster, session = create_database()
    
    print("Drop tables if already exists ")
    drop_tables(session)

    print("Create tables ")
    create_tables(session)


if __name__ == "__main__":
    main()