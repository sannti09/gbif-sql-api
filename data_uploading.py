import pandas as pd
import cx_Oracle
from sqlalchemy import create_engine

def get_connection():
    host = 'orion.javeriana.edu.co'
    port = '1521'
    service_name = 'INGSIS'
    database_name = 'LAB'
    username = 'is327200'
    password = 'Ve0ZRVqAmR'
    
    dsn = cx_Oracle.makedsn(host, port, service_name, database_name)
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    
    return connection


df = pd.read_csv('output.csv', dtype=str)


connection = get_connection()
count = 0
size_df = len(df) 
for i, row in df.iterrows():
    count += 1
    if count % 10 == 0:
        print(f"DATOS AGREGADOS: {count}/{size_df}")
    try:
        event_data = {
            'eventID': row['eventID'],
            'eventType': row['type'],
            'parentEventID': row['parentEventID'],
            'eventDate': row['eventDate'],
            'locationID': row['locationID']
        }
        connection.cursor().execute("INSERT INTO Event VALUES (:eventID, :eventType, :parentEventID, :eventDate, :locationID)", **event_data)

        tramp_data = {
            'eventID': row['eventID'],
            'identifiedBy': row['identifiedBy'],
            'samplingProtocol': row['samplingProtocol'],
            'identificationRemarks': row['identificationRemarks'],
            'country': row['country'],
            'publishingCountry': row['publishingCountry']
        }
        connection.cursor().execute("INSERT INTO Tramp VALUES (:eventID, :identifiedBy, :samplingProtocol, :identificationRemarks, :country, :publishingCountry)", **tramp_data)

        taxon_data = {
            'taxonID': row['taxonID'],
            'kingdom': row['kingdom'],
            'scientificName': row['scientificName']
        }
        connection.cursor().execute("INSERT INTO Taxon VALUES (:taxonID, :kingdom, :scientificName)", **taxon_data)

        organism_data = {
            'organismID': row['key'], 
            'organismScope': row['lifeStage'], 
            'sex': row['sex']
        }
        connection.cursor().execute("INSERT INTO Organism VALUES (:organismID, :organismScope, :sex)", **organism_data)

    except Exception as e:
        0
        #print(f"Error insertando fila {i}: {e}")

    finally:
        connection.commit()

connection.close()