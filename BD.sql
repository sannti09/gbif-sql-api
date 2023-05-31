BEGIN
   FOR v IN (SELECT view_name FROM user_views)
   LOOP
      EXECUTE IMMEDIATE 'DROP VIEW ' || v.view_name;
   END LOOP;
END;
/

BEGIN
   FOR v IN (SELECT table_name FROM user_tables ORDER BY 1 DESC)
   LOOP
      BEGIN
         EXECUTE IMMEDIATE 'DROP TABLE ' || v.table_name || ' CASCADE CONSTRAINTS';
      EXCEPTION
         WHEN OTHERS THEN
            NULL; -- Ignorar cualquier error que pueda ocurrir al eliminar una tabla
      END;
   END LOOP;
END;
/

BEGIN
   FOR v IN (SELECT view_name FROM user_views)
   LOOP
      EXECUTE IMMEDIATE 'DROP VIEW ' || v.view_name;
   END LOOP;
END;
/

BEGIN
   FOR v IN (SELECT table_name FROM user_tables ORDER BY 1 DESC)
   LOOP
      BEGIN
         EXECUTE IMMEDIATE 'DROP TABLE ' || v.table_name || ' CASCADE CONSTRAINTS';
      EXCEPTION
         WHEN OTHERS THEN
            NULL;
      END;
   END LOOP;
END;
/

-- Crear tabla Deployment
CREATE TABLE Deployment (
  deploymentID VARCHAR(100) PRIMARY KEY,
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  locationID VARCHAR(100)
);

-- Crear tabla Observation
CREATE TABLE Observation (
  observationID VARCHAR(100),
  mediaID VARCHAR(100),
  sequenceID VARCHAR(100),
  scientificName VARCHAR(100),
  count INT,
  countNew INT,
  lifeStage VARCHAR(100),
  classificationMethod VARCHAR(100),
  PRIMARY KEY(observationID)
);

-- Crear tabla Media
CREATE TABLE Media (
  deploymentID VARCHAR(100),
  mediaID VARCHAR(100),
  sequenceID VARCHAR(100),
  timestamp TIMESTAMP,
  filePath VARCHAR(100),
  PRIMARY KEY (mediaID),
  CONSTRAINT fk_Deployment FOREIGN KEY (deploymentID) REFERENCES Deployment(deploymentID)
);

-- TABLE Event
CREATE TABLE Event (
    eventID VARCHAR(100) PRIMARY KEY,
    eventType VARCHAR(100),
    parentEventID VARCHAR(100),
    eventDate VARCHAR(100),
    locationID VARCHAR(100),
    habitatType VARCHAR(100)
);

-- TABLE Tramp
CREATE TABLE Tramp (
    eventID VARCHAR(100) PRIMARY KEY,
    identifiedBy VARCHAR(100),
    samplingProtocol VARCHAR(100),
    identificationRemarks VARCHAR(100),
    country VARCHAR(100),
    publishingCountry VARCHAR(100),
    cameraInstallDetails VARCHAR(100)
);

-- TABLE Entity
CREATE TABLE Entity (
    entityID VARCHAR(100) PRIMARY KEY,
    entityType VARCHAR(100),
    entityCreated DATE,
    commonName VARCHAR(100),
    scientificName VARCHAR(100)
);

-- TABLE DigitalEntity
CREATE TABLE DigitalEntity (
    digitalEntityID VARCHAR(100) PRIMARY KEY,
    digitalEntityType VARCHAR(100),
    format VARCHAR(100),
    accessURI VARCHAR(100),
    entityID VARCHAR(100),
    FOREIGN KEY (entityID) REFERENCES Entity(entityID)
);

-- TABLE Organism
CREATE TABLE Organism (
    organismID VARCHAR(100) PRIMARY KEY,
    organismScope VARCHAR(100),
    sex VARCHAR(100),
    country VARCHAR(100)
);

-- TABLE EntityEvent
CREATE TABLE EntityEvent (
    entityID VARCHAR(100),
    eventID VARCHAR(100),
    FOREIGN KEY (entityID) REFERENCES Entity(entityID),
    FOREIGN KEY (eventID) REFERENCES Event(eventID)
);

-- TABLE EntityAssertion
CREATE TABLE EntityAssertion (
    entityAssertionID VARCHAR(100) PRIMARY KEY,
    entityID VARCHAR(100),
    entityAssertionType VARCHAR(100),
    entityAssertionValue VARCHAR(100),
    entityAssertionUnit VARCHAR(100),
    FOREIGN KEY (entityID) REFERENCES Entity(entityID)
);

-- TABLE Identification
CREATE TABLE Identification (
    identificationID VARCHAR(100) PRIMARY KEY,
    identificationType VARCHAR(100),
    taxaFormula VARCHAR(100),
    verbatimIdentification VARCHAR(100)
);

-- TABLE IdentificationEntity
CREATE TABLE IdentificationEntity (
    identificationID VARCHAR(100),
    entityID VARCHAR(100),
    FOREIGN KEY (identificationID) REFERENCES Identification(identificationID),
    FOREIGN KEY (entityID) REFERENCES Entity(entityID)
);

-- TABLE Taxon
CREATE TABLE Taxon (
    taxonID VARCHAR(100) PRIMARY KEY,
    kingdom VARCHAR(100),
    scientificName VARCHAR(100)
);

-- TABLE TaxonIdentification
CREATE TABLE TaxonIdentification (
    taxonID VARCHAR(100),
    identificationID VARCHAR(100),
    taxonOrder VARCHAR(100),
    FOREIGN KEY (taxonID) REFERENCES Taxon(taxonID),
    FOREIGN KEY (identificationID) REFERENCES Identification(identificationID)
);
