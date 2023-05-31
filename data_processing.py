import pandas as pd
import json, requests, time

tables_dict = {
    "Event": ["eventID", "eventType", "parentEventID", "eventDate", "locationID"],
    "Tramp": ["eventID", "identifiedBy", "samplingProtocol", "identificationRemarks", "country", "publishingCountry"],
    "Entity": ["entityID", "entityType", "entityCreated"],
    "DigitalEntity": ["digitalEntityID", "digitalEntityType", "format", "accessURI"],
    "Organism": ["organismID", "organismScope", "sex"],
    "EntityEvent": ["entityID", "eventID"],
    "EntityAssertion": ["entityAssertionID", "entityID", "entityAssertionType", "entityAssertionValue", "entityAssertionUnit"],
    "Identification": ["identificationID", "identificationType", "taxaFormula", "verbatimIdentification"],
    "IdentificationEntity": ["identificationID", "entityID"],
    "Taxon": ["taxonID", "kingdom", "scientificName"],
    "TaxonIdentification": ["taxonID", "identificationID", "taxonOrder"],
}

df_occurrence = pd.read_csv('Swedish-Malaise-Trap-Project/occurrence.txt', sep='\t', low_memory=False, nrows=20000)
df_multimedia = pd.read_csv('Swedish-Malaise-Trap-Project/multimedia.txt', sep='\t', low_memory=False, nrows=20000)
df_verbatim = pd.read_csv('Swedish-Malaise-Trap-Project/verbatim.txt', sep='\t', low_memory=False, nrows=20000)

df_occurrence = df_occurrence.dropna(axis=1, how='all')
df_multimedia = df_multimedia.dropna(axis=1, how='all')
df_verbatim = df_verbatim.dropna(axis=1, how='all')

df = pd.merge(df_occurrence, df_multimedia, on='gbifID', how='inner')
df = pd.merge(df, df_verbatim, on='gbifID', how='inner')

df = df.loc[:,~df.columns.duplicated()]
df.columns = [col.replace('_x', '').replace('_y', '') for col in df.columns]


final_df = pd.DataFrame()
unique_occurrenceIDs = set()


for row in df.itertuples(index=False):
    occurrence_id = row.occurrenceID
    if occurrence_id not in unique_occurrenceIDs:
        try:
            response = requests.get(f'https://api.gbif.org/v1/occurrence/search?occurrenceID={occurrence_id}')
            data = response.json()
            time.sleep(0.1)

            if 'results' in data:
                temp_df = pd.DataFrame(data['results'])
                temp_df = temp_df.drop([col for col in temp_df.columns if isinstance(temp_df[col][0], (dict, list))], axis=1)

                final_df = pd.concat([final_df, temp_df], ignore_index=True)
                unique_occurrenceIDs.add(occurrence_id)
                
        except requests.exceptions.RequestException as e:
            print(f"Error al hacer la solicitud a la API: {e}")
            continue

final_df.to_csv('output.csv', index=False)
