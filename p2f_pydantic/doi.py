from pydantic import BaseModel
from pydantic import HttpUrl, Base64Str
from typing import Literal, List, Optional, Union
from datetime import date, datetime

class DataCiteDOI_DATA_CREATORS(BaseModel):
    name: str
    givenName: str
    familyName: str
    affiliation: List[str]
    nameIdentifiers: List[str]

class DataCiteDOI_DATA_TITLES(BaseModel):
    title: str

class DataCiteDOI_DATA_SUBJECTS(BaseModel):
    subject: str
    schemeUri: HttpUrl
    subjectScheme: str
    classificationCode: str

class DataCiteDOI_DATA_DATES(BaseModel):
    date: Union[date, datetime]
    dateType: str

class DataCiteDOI_DATA_TYPES(BaseModel):
    ris: str
    bibtex: str
    citeproc: str
    schemaOrg: str
    resourceType: str
    resourceTypeGeneral: str

class DataCiteDOI_DATA_RELATEDIDENTIFIERS(BaseModel):
    relationType: str
    relatedIdentifier: str
    relatedIdentifierType: str

class DataCiteDOI_DATA_FUNDINGREFERENCES(BaseModel):
    schemeUri: HttpUrl
    awardTitle: str
    funderName: str
    awardNumber: str
    funderIdentifier: Union[str, HttpUrl]
    funderIdentifierType: str

class DataCiteDOI_DATA_DESCRIPTIONS(BaseModel):
    description: str

class DataCiteDOI_DATA_ATTRIBUTES(BaseModel):
    doi: str 
    prefix: str 
    suffix:  str 
    # identifiers: [] # []
    # alternateIdentifiers: [] # []
    creators: List[DataCiteDOI_DATA_CREATORS] 
    titles: List[DataCiteDOI_DATA_TITLES] 
    publisher: str 
    # container:  # {}
    publicationYear: int 
    subjects: List[DataCiteDOI_DATA_SUBJECTS] 
    # contributors:  # []
    dates: List[DataCiteDOI_DATA_DATES] 
    language: Optional[str] = None # None
    types: DataCiteDOI_DATA_TYPES
    relatedIdentifiers: List[DataCiteDOI_DATA_RELATEDIDENTIFIERS] 
    # relatedItems:  # []
    sizes: List[str] 
    # formats:  # []
    version: Optional[str] = None # None
    rightsList: List[dict] 
    descriptions: List[DataCiteDOI_DATA_DESCRIPTIONS] 
    # geoLocations:  # []
    fundingReferences: List[DataCiteDOI_DATA_FUNDINGREFERENCES] 
    xml: Base64Str 
    url: HttpUrl 
    contentUrl: Optional[HttpUrl] = None 
    metadataVersion: Optional[Union[str, int]] = None
    schemaVersion: HttpUrl

class DataCiteDOI_DATA_RELATIONSHIP(BaseModel):
    id: str
    type: str

class DataCiteDOI_DATA_RELATIONSHIP_DATA(BaseModel):
    data: Union[DataCiteDOI_DATA_RELATIONSHIP, List[DataCiteDOI_DATA_RELATIONSHIP], list] = []

class DataCiteDOI_DATA_RELATIONSHIPS(BaseModel):
    client: DataCiteDOI_DATA_RELATIONSHIP_DATA # {'data': {'id': 'figshare.ars', 'type': 'clients'}}
    provider: DataCiteDOI_DATA_RELATIONSHIP_DATA # {'data': {'id': 'otjm', 'type': 'providers'}}
    media: DataCiteDOI_DATA_RELATIONSHIP_DATA # {'data': {'id': '10.6084/m9.figshare.29497142.v1', 'type': 'media'}}
    references: DataCiteDOI_DATA_RELATIONSHIP_DATA # {'data': []}
    citations: DataCiteDOI_DATA_RELATIONSHIP_DATA # {'data': [{'id': '10.1038/s41467-025-62446-x', 'type': 'dois'}]}
    parts: DataCiteDOI_DATA_RELATIONSHIP_DATA # {'data': []}
    partOf: DataCiteDOI_DATA_RELATIONSHIP_DATA # {'data': []}
    versions: DataCiteDOI_DATA_RELATIONSHIP_DATA # {'data': []}
    versionOf: DataCiteDOI_DATA_RELATIONSHIP_DATA # {'data': []}

class DataCiteDOI_DATA(BaseModel):
    attributes: DataCiteDOI_DATA_ATTRIBUTES
    id: str
    relationships: DataCiteDOI_DATA_RELATIONSHIPS
    type: Literal["dois"]

class DataCiteDOI(BaseModel):
    data: DataCiteDOI_DATA