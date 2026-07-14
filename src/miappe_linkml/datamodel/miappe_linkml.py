# Auto generated from miappe_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-14T16:28:27
# Schema: miappe-linkml
#
# id: https://w3id.org/sierra-moxon/miappe-linkml
# description: A LinkML representation of the MIAPPE (Minimum Information About a Plant Phenotyping Experiment) v1.1 checklist and data model. The structure follows the MIAPPE entity relationship diagram (Investigation > Study > Observation Unit > Sample) together with the supporting entities (Person, Publication, Biological Material, Environment Parameter, Experimental Factor, Event, Data File and Observed Variable). Each slot records its MIAPPE "codename" in a comment, and enumerations are derived from the MIAPPE checklist and its appendices.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import DateOrDatetime, Float, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE

metamodel_version = "1.11.0"
version = None

# Namespaces
CO_322 = CurieNamespace('CO_322', 'http://www.cropontology.org/rdf/CO_322_')
CO_715 = CurieNamespace('CO_715', 'http://www.cropontology.org/rdf/CO_715_')
EO = CurieNamespace('EO', 'http://purl.obolibrary.org/obo/EO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PO = CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_')
TO = CurieNamespace('TO', 'http://purl.obolibrary.org/obo/TO_')
XEO = CurieNamespace('XEO', 'http://purl.obolibrary.org/obo/XEO_')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIAPPE_LINKML = CurieNamespace('miappe_linkml', 'https://w3id.org/sierra-moxon/miappe-linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MIAPPE_LINKML


# Types

# Class references
class InvestigationInvestigationId(URIorCURIE):
    pass


class StudyStudyId(URIorCURIE):
    pass


class BiologicalMaterialBiologicalMaterialId(URIorCURIE):
    pass


class ObservationUnitObservationUnitId(URIorCURIE):
    pass


class SampleSampleId(URIorCURIE):
    pass


class ObservedVariableVariableId(URIorCURIE):
    pass


@dataclass(repr=False)
class Investigation(YAMLRoot):
    """
    Investigations are research programmes with defined aims. They can exist at various scales (for example, they
    could encompass a grant-funded programme of work, the various components comprising a peer-reviewed publication,
    or a single experiment). One investigation is expected per MIAPPE submission.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["Investigation"]
    class_class_curie: ClassVar[str] = "miappe_linkml:Investigation"
    class_name: ClassVar[str] = "Investigation"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.Investigation

    investigation_id: Union[str, InvestigationInvestigationId] = None
    investigation_title: str = None
    miappe_version: str = None
    studies: Union[dict[Union[str, StudyStudyId], Union[dict, "Study"]], list[Union[dict, "Study"]]] = empty_dict()
    investigation_description: Optional[str] = None
    submission_date: Optional[Union[str, str]] = None
    public_release_date: Optional[Union[str, str]] = None
    license: Optional[Union[str, "LicenseEnum"]] = None
    associated_publications: Optional[Union[Union[dict, "Publication"], list[Union[dict, "Publication"]]]] = empty_list()
    persons: Optional[Union[Union[dict, "Person"], list[Union[dict, "Person"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.investigation_id):
            self.MissingRequiredField("investigation_id")
        if not isinstance(self.investigation_id, InvestigationInvestigationId):
            self.investigation_id = InvestigationInvestigationId(self.investigation_id)

        if self._is_empty(self.investigation_title):
            self.MissingRequiredField("investigation_title")
        if not isinstance(self.investigation_title, str):
            self.investigation_title = str(self.investigation_title)

        if self._is_empty(self.miappe_version):
            self.MissingRequiredField("miappe_version")
        if not isinstance(self.miappe_version, str):
            self.miappe_version = str(self.miappe_version)

        if self._is_empty(self.studies):
            self.MissingRequiredField("studies")
        self._normalize_inlined_as_list(slot_name="studies", slot_type=Study, key_name="study_id", keyed=True)

        if self.investigation_description is not None and not isinstance(self.investigation_description, str):
            self.investigation_description = str(self.investigation_description)

        if self.submission_date is not None and not isinstance(self.submission_date, str):
            self.submission_date = str(self.submission_date)

        if self.public_release_date is not None and not isinstance(self.public_release_date, str):
            self.public_release_date = str(self.public_release_date)

        if self.license is not None and not isinstance(self.license, LicenseEnum):
            self.license = LicenseEnum(self.license)

        if not isinstance(self.associated_publications, list):
            self.associated_publications = [self.associated_publications] if self.associated_publications is not None else []
        self.associated_publications = [v if isinstance(v, Publication) else Publication(**as_dict(v)) for v in self.associated_publications]

        self._normalize_inlined_as_list(slot_name="persons", slot_type=Person, key_name="person_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(YAMLRoot):
    """
    A study (or experiment) comprises a series of assays (or measurements) of one or more types, undertaken to answer
    a particular biological question. At least one study is expected per investigation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["Study"]
    class_class_curie: ClassVar[str] = "miappe_linkml:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.Study

    study_id: Union[str, StudyStudyId] = None
    study_title: str = None
    study_start_date: Union[str, str] = None
    contact_institution: str = None
    location_country: str = None
    site_name: str = None
    experimental_design_description: str = None
    observation_unit_description: str = None
    growth_facility_description: str = None
    observation_units: Union[dict[Union[str, ObservationUnitObservationUnitId], Union[dict, "ObservationUnit"]], list[Union[dict, "ObservationUnit"]]] = empty_dict()
    observed_variables: Union[dict[Union[str, ObservedVariableVariableId], Union[dict, "ObservedVariable"]], list[Union[dict, "ObservedVariable"]]] = empty_dict()
    study_description: Optional[str] = None
    study_end_date: Optional[Union[str, str]] = None
    location_latitude: Optional[float] = None
    location_longitude: Optional[float] = None
    location_altitude: Optional[str] = None
    experimental_design_type: Optional[Union[str, URIorCURIE]] = None
    observation_unit_level_hierarchy: Optional[str] = None
    growth_facility_type: Optional[Union[str, URIorCURIE]] = None
    cultural_practices: Optional[str] = None
    experimental_design_map: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    persons: Optional[Union[Union[dict, "Person"], list[Union[dict, "Person"]]]] = empty_list()
    data_files: Optional[Union[Union[dict, "DataFile"], list[Union[dict, "DataFile"]]]] = empty_list()
    biological_materials: Optional[Union[dict[Union[str, BiologicalMaterialBiologicalMaterialId], Union[dict, "BiologicalMaterial"]], list[Union[dict, "BiologicalMaterial"]]]] = empty_dict()
    environment_parameters: Optional[Union[Union[dict, "EnvironmentParameter"], list[Union[dict, "EnvironmentParameter"]]]] = empty_list()
    experimental_factors: Optional[Union[Union[dict, "ExperimentalFactor"], list[Union[dict, "ExperimentalFactor"]]]] = empty_list()
    events: Optional[Union[Union[dict, "Event"], list[Union[dict, "Event"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.study_id):
            self.MissingRequiredField("study_id")
        if not isinstance(self.study_id, StudyStudyId):
            self.study_id = StudyStudyId(self.study_id)

        if self._is_empty(self.study_title):
            self.MissingRequiredField("study_title")
        if not isinstance(self.study_title, str):
            self.study_title = str(self.study_title)

        if self._is_empty(self.study_start_date):
            self.MissingRequiredField("study_start_date")
        if not isinstance(self.study_start_date, str):
            self.study_start_date = str(self.study_start_date)

        if self._is_empty(self.contact_institution):
            self.MissingRequiredField("contact_institution")
        if not isinstance(self.contact_institution, str):
            self.contact_institution = str(self.contact_institution)

        if self._is_empty(self.location_country):
            self.MissingRequiredField("location_country")
        if not isinstance(self.location_country, str):
            self.location_country = str(self.location_country)

        if self._is_empty(self.site_name):
            self.MissingRequiredField("site_name")
        if not isinstance(self.site_name, str):
            self.site_name = str(self.site_name)

        if self._is_empty(self.experimental_design_description):
            self.MissingRequiredField("experimental_design_description")
        if not isinstance(self.experimental_design_description, str):
            self.experimental_design_description = str(self.experimental_design_description)

        if self._is_empty(self.observation_unit_description):
            self.MissingRequiredField("observation_unit_description")
        if not isinstance(self.observation_unit_description, str):
            self.observation_unit_description = str(self.observation_unit_description)

        if self._is_empty(self.growth_facility_description):
            self.MissingRequiredField("growth_facility_description")
        if not isinstance(self.growth_facility_description, str):
            self.growth_facility_description = str(self.growth_facility_description)

        if self._is_empty(self.observation_units):
            self.MissingRequiredField("observation_units")
        self._normalize_inlined_as_list(slot_name="observation_units", slot_type=ObservationUnit, key_name="observation_unit_id", keyed=True)

        if self._is_empty(self.observed_variables):
            self.MissingRequiredField("observed_variables")
        self._normalize_inlined_as_list(slot_name="observed_variables", slot_type=ObservedVariable, key_name="variable_id", keyed=True)

        if self.study_description is not None and not isinstance(self.study_description, str):
            self.study_description = str(self.study_description)

        if self.study_end_date is not None and not isinstance(self.study_end_date, str):
            self.study_end_date = str(self.study_end_date)

        if self.location_latitude is not None and not isinstance(self.location_latitude, float):
            self.location_latitude = float(self.location_latitude)

        if self.location_longitude is not None and not isinstance(self.location_longitude, float):
            self.location_longitude = float(self.location_longitude)

        if self.location_altitude is not None and not isinstance(self.location_altitude, str):
            self.location_altitude = str(self.location_altitude)

        if self.experimental_design_type is not None and not isinstance(self.experimental_design_type, URIorCURIE):
            self.experimental_design_type = URIorCURIE(self.experimental_design_type)

        if self.observation_unit_level_hierarchy is not None and not isinstance(self.observation_unit_level_hierarchy, str):
            self.observation_unit_level_hierarchy = str(self.observation_unit_level_hierarchy)

        if self.growth_facility_type is not None and not isinstance(self.growth_facility_type, URIorCURIE):
            self.growth_facility_type = URIorCURIE(self.growth_facility_type)

        if self.cultural_practices is not None and not isinstance(self.cultural_practices, str):
            self.cultural_practices = str(self.cultural_practices)

        if not isinstance(self.experimental_design_map, list):
            self.experimental_design_map = [self.experimental_design_map] if self.experimental_design_map is not None else []
        self.experimental_design_map = [v if isinstance(v, URI) else URI(v) for v in self.experimental_design_map]

        self._normalize_inlined_as_list(slot_name="persons", slot_type=Person, key_name="person_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="data_files", slot_type=DataFile, key_name="data_file_link", keyed=False)

        self._normalize_inlined_as_list(slot_name="biological_materials", slot_type=BiologicalMaterial, key_name="biological_material_id", keyed=True)

        self._normalize_inlined_as_list(slot_name="environment_parameters", slot_type=EnvironmentParameter, key_name="environment_parameter_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="experimental_factors", slot_type=ExperimentalFactor, key_name="experimental_factor_type", keyed=False)

        self._normalize_inlined_as_list(slot_name="events", slot_type=Event, key_name="event_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    A human involved in the investigation or specifically any of its studies. At least one person is expected per
    investigation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["Person"]
    class_class_curie: ClassVar[str] = "miappe_linkml:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.Person

    person_name: str = None
    person_roles: Union[str, list[str]] = None
    person_affiliations: Union[str, list[str]] = None
    person_email: Optional[str] = None
    person_id: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.person_name):
            self.MissingRequiredField("person_name")
        if not isinstance(self.person_name, str):
            self.person_name = str(self.person_name)

        if self._is_empty(self.person_roles):
            self.MissingRequiredField("person_roles")
        if not isinstance(self.person_roles, list):
            self.person_roles = [self.person_roles] if self.person_roles is not None else []
        self.person_roles = [v if isinstance(v, str) else str(v) for v in self.person_roles]

        if self._is_empty(self.person_affiliations):
            self.MissingRequiredField("person_affiliations")
        if not isinstance(self.person_affiliations, list):
            self.person_affiliations = [self.person_affiliations] if self.person_affiliations is not None else []
        self.person_affiliations = [v if isinstance(v, str) else str(v) for v in self.person_affiliations]

        if self.person_email is not None and not isinstance(self.person_email, str):
            self.person_email = str(self.person_email)

        if self.person_id is not None and not isinstance(self.person_id, URIorCURIE):
            self.person_id = URIorCURIE(self.person_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Publication(YAMLRoot):
    """
    A literature publication where the investigation is described. Use of DOIs is recommended.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["Publication"]
    class_class_curie: ClassVar[str] = "miappe_linkml:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.Publication

    associated_publication: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.associated_publication is not None and not isinstance(self.associated_publication, URIorCURIE):
            self.associated_publication = URIorCURIE(self.associated_publication)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataFile(YAMLRoot):
    """
    A file or digital object holding observation data recorded during one or more assays of the study, typically in
    tabular form.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["DataFile"]
    class_class_curie: ClassVar[str] = "miappe_linkml:DataFile"
    class_name: ClassVar[str] = "DataFile"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.DataFile

    data_file_link: Union[str, URI] = None
    data_file_description: str = None
    data_file_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.data_file_link):
            self.MissingRequiredField("data_file_link")
        if not isinstance(self.data_file_link, URI):
            self.data_file_link = URI(self.data_file_link)

        if self._is_empty(self.data_file_description):
            self.MissingRequiredField("data_file_description")
        if not isinstance(self.data_file_description, str):
            self.data_file_description = str(self.data_file_description)

        if self.data_file_version is not None and not isinstance(self.data_file_version, str):
            self.data_file_version = str(self.data_file_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiologicalMaterial(YAMLRoot):
    """
    The biological material being studied (e.g. plants grown from a certain bag or seed, or plants grown in a
    particular field). The original source of that material is called the material source.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["BiologicalMaterial"]
    class_class_curie: ClassVar[str] = "miappe_linkml:BiologicalMaterial"
    class_name: ClassVar[str] = "BiologicalMaterial"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.BiologicalMaterial

    biological_material_id: Union[str, BiologicalMaterialBiologicalMaterialId] = None
    organism: Union[str, URIorCURIE] = None
    biological_material_external_ids: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    genus: Optional[str] = None
    species: Optional[str] = None
    infraspecific_name: Optional[str] = None
    biological_material_preprocessing: Optional[Union[str, list[str]]] = empty_list()
    material_source: Optional[Union[dict, "MaterialSource"]] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[str] = None
    coordinates_uncertainty: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.biological_material_id):
            self.MissingRequiredField("biological_material_id")
        if not isinstance(self.biological_material_id, BiologicalMaterialBiologicalMaterialId):
            self.biological_material_id = BiologicalMaterialBiologicalMaterialId(self.biological_material_id)

        if self._is_empty(self.organism):
            self.MissingRequiredField("organism")
        if not isinstance(self.organism, URIorCURIE):
            self.organism = URIorCURIE(self.organism)

        if not isinstance(self.biological_material_external_ids, list):
            self.biological_material_external_ids = [self.biological_material_external_ids] if self.biological_material_external_ids is not None else []
        self.biological_material_external_ids = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.biological_material_external_ids]

        if self.genus is not None and not isinstance(self.genus, str):
            self.genus = str(self.genus)

        if self.species is not None and not isinstance(self.species, str):
            self.species = str(self.species)

        if self.infraspecific_name is not None and not isinstance(self.infraspecific_name, str):
            self.infraspecific_name = str(self.infraspecific_name)

        if not isinstance(self.biological_material_preprocessing, list):
            self.biological_material_preprocessing = [self.biological_material_preprocessing] if self.biological_material_preprocessing is not None else []
        self.biological_material_preprocessing = [v if isinstance(v, str) else str(v) for v in self.biological_material_preprocessing]

        if self.material_source is not None and not isinstance(self.material_source, MaterialSource):
            self.material_source = MaterialSource(**as_dict(self.material_source))

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.altitude is not None and not isinstance(self.altitude, str):
            self.altitude = str(self.altitude)

        if self.coordinates_uncertainty is not None and not isinstance(self.coordinates_uncertainty, str):
            self.coordinates_uncertainty = str(self.coordinates_uncertainty)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialSource(YAMLRoot):
    """
    An identifier for the source of the biological material (commonly called germplasm, accession, genotype or
    variety), together with any repository accession information and provenance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["MaterialSource"]
    class_class_curie: ClassVar[str] = "miappe_linkml:MaterialSource"
    class_name: ClassVar[str] = "MaterialSource"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.MaterialSource

    material_source_id: Optional[Union[str, URIorCURIE]] = None
    material_source_doi: Optional[Union[str, URIorCURIE]] = None
    material_source_accession_number: Optional[str] = None
    material_source_accession_name: Optional[str] = None
    material_source_institute_code: Optional[str] = None
    material_source_institute_name: Optional[str] = None
    material_source_other_ids: Optional[str] = None
    material_source_description: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[str] = None
    coordinates_uncertainty: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.material_source_id is not None and not isinstance(self.material_source_id, URIorCURIE):
            self.material_source_id = URIorCURIE(self.material_source_id)

        if self.material_source_doi is not None and not isinstance(self.material_source_doi, URIorCURIE):
            self.material_source_doi = URIorCURIE(self.material_source_doi)

        if self.material_source_accession_number is not None and not isinstance(self.material_source_accession_number, str):
            self.material_source_accession_number = str(self.material_source_accession_number)

        if self.material_source_accession_name is not None and not isinstance(self.material_source_accession_name, str):
            self.material_source_accession_name = str(self.material_source_accession_name)

        if self.material_source_institute_code is not None and not isinstance(self.material_source_institute_code, str):
            self.material_source_institute_code = str(self.material_source_institute_code)

        if self.material_source_institute_name is not None and not isinstance(self.material_source_institute_name, str):
            self.material_source_institute_name = str(self.material_source_institute_name)

        if self.material_source_other_ids is not None and not isinstance(self.material_source_other_ids, str):
            self.material_source_other_ids = str(self.material_source_other_ids)

        if self.material_source_description is not None and not isinstance(self.material_source_description, str):
            self.material_source_description = str(self.material_source_description)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.altitude is not None and not isinstance(self.altitude, str):
            self.altitude = str(self.altitude)

        if self.coordinates_uncertainty is not None and not isinstance(self.coordinates_uncertainty, str):
            self.coordinates_uncertainty = str(self.coordinates_uncertainty)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentParameter(YAMLRoot):
    """
    An environmental parameter that was kept constant throughout the study and did not change between observation
    units or assays.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["EnvironmentParameter"]
    class_class_curie: ClassVar[str] = "miappe_linkml:EnvironmentParameter"
    class_name: ClassVar[str] = "EnvironmentParameter"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.EnvironmentParameter

    environment_parameter_name: str = None
    environment_parameter_value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.environment_parameter_name):
            self.MissingRequiredField("environment_parameter_name")
        if not isinstance(self.environment_parameter_name, str):
            self.environment_parameter_name = str(self.environment_parameter_name)

        if self._is_empty(self.environment_parameter_value):
            self.MissingRequiredField("environment_parameter_value")
        if not isinstance(self.environment_parameter_value, str):
            self.environment_parameter_value = str(self.environment_parameter_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentalFactor(YAMLRoot):
    """
    A condition that varies between observation units, which may be biotic (pest, disease interaction) or abiotic
    (treatment and cultural practice) in nature. The object of a study is to ascertain the impact of one or more
    factors on the biological material.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["ExperimentalFactor"]
    class_class_curie: ClassVar[str] = "miappe_linkml:ExperimentalFactor"
    class_name: ClassVar[str] = "ExperimentalFactor"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.ExperimentalFactor

    experimental_factor_type: Union[str, "ExperimentalFactorTypeEnum"] = None
    experimental_factor_description: Optional[str] = None
    experimental_factor_values: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.experimental_factor_type):
            self.MissingRequiredField("experimental_factor_type")
        if not isinstance(self.experimental_factor_type, ExperimentalFactorTypeEnum):
            self.experimental_factor_type = ExperimentalFactorTypeEnum(self.experimental_factor_type)

        if self.experimental_factor_description is not None and not isinstance(self.experimental_factor_description, str):
            self.experimental_factor_description = str(self.experimental_factor_description)

        if not isinstance(self.experimental_factor_values, list):
            self.experimental_factor_values = [self.experimental_factor_values] if self.experimental_factor_values is not None else []
        self.experimental_factor_values = [v if isinstance(v, str) else str(v) for v in self.experimental_factor_values]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Event(YAMLRoot):
    """
    An event is a discrete occurrence at a particular time in the experiment (which can be natural, such as rain, or
    unnatural, such as planting, watering, etc).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["Event"]
    class_class_curie: ClassVar[str] = "miappe_linkml:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.Event

    event_type: str = None
    event_dates: Union[Union[str, str], list[Union[str, str]]] = None
    event_accession_number: Optional[Union[str, URIorCURIE]] = None
    event_description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.event_type):
            self.MissingRequiredField("event_type")
        if not isinstance(self.event_type, str):
            self.event_type = str(self.event_type)

        if self._is_empty(self.event_dates):
            self.MissingRequiredField("event_dates")
        if not isinstance(self.event_dates, list):
            self.event_dates = [self.event_dates] if self.event_dates is not None else []
        self.event_dates = [v if isinstance(v, str) else str(v) for v in self.event_dates]

        if self.event_accession_number is not None and not isinstance(self.event_accession_number, URIorCURIE):
            self.event_accession_number = URIorCURIE(self.event_accession_number)

        if self.event_description is not None and not isinstance(self.event_description, str):
            self.event_description = str(self.event_description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservationUnit(YAMLRoot):
    """
    Observation units are objects that are subject to instances of observation and measurement. An observation unit
    comprises one or more plants, and/or their environment. (Synonym: Experimental unit)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["ObservationUnit"]
    class_class_curie: ClassVar[str] = "miappe_linkml:ObservationUnit"
    class_name: ClassVar[str] = "ObservationUnit"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.ObservationUnit

    observation_unit_id: Union[str, ObservationUnitObservationUnitId] = None
    observation_unit_type: Union[str, "ObservationUnitTypeEnum"] = None
    observation_unit_external_ids: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    spatial_distribution: Optional[Union[str, list[str]]] = empty_list()
    observation_unit_factor_values: Optional[Union[str, list[str]]] = empty_list()
    biological_material: Optional[Union[Union[str, BiologicalMaterialBiologicalMaterialId], list[Union[str, BiologicalMaterialBiologicalMaterialId]]]] = empty_list()
    samples: Optional[Union[dict[Union[str, SampleSampleId], Union[dict, "Sample"]], list[Union[dict, "Sample"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.observation_unit_id):
            self.MissingRequiredField("observation_unit_id")
        if not isinstance(self.observation_unit_id, ObservationUnitObservationUnitId):
            self.observation_unit_id = ObservationUnitObservationUnitId(self.observation_unit_id)

        if self._is_empty(self.observation_unit_type):
            self.MissingRequiredField("observation_unit_type")
        if not isinstance(self.observation_unit_type, ObservationUnitTypeEnum):
            self.observation_unit_type = ObservationUnitTypeEnum(self.observation_unit_type)

        if not isinstance(self.observation_unit_external_ids, list):
            self.observation_unit_external_ids = [self.observation_unit_external_ids] if self.observation_unit_external_ids is not None else []
        self.observation_unit_external_ids = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.observation_unit_external_ids]

        if not isinstance(self.spatial_distribution, list):
            self.spatial_distribution = [self.spatial_distribution] if self.spatial_distribution is not None else []
        self.spatial_distribution = [v if isinstance(v, str) else str(v) for v in self.spatial_distribution]

        if not isinstance(self.observation_unit_factor_values, list):
            self.observation_unit_factor_values = [self.observation_unit_factor_values] if self.observation_unit_factor_values is not None else []
        self.observation_unit_factor_values = [v if isinstance(v, str) else str(v) for v in self.observation_unit_factor_values]

        if not isinstance(self.biological_material, list):
            self.biological_material = [self.biological_material] if self.biological_material is not None else []
        self.biological_material = [v if isinstance(v, BiologicalMaterialBiologicalMaterialId) else BiologicalMaterialBiologicalMaterialId(v) for v in self.biological_material]

        self._normalize_inlined_as_list(slot_name="samples", slot_type=Sample, key_name="sample_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(YAMLRoot):
    """
    A sample is a portion of plant tissue harvested, non-harvested or extracted from an observation unit for the
    purpose of sub-plant observations and/or molecular studies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["Sample"]
    class_class_curie: ClassVar[str] = "miappe_linkml:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.Sample

    sample_id: Union[str, SampleSampleId] = None
    anatomical_entity: Union[str, URIorCURIE] = None
    collection_date: Union[str, str] = None
    development_stage: Optional[Union[str, URIorCURIE]] = None
    sample_description: Optional[str] = None
    sample_external_ids: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, SampleSampleId):
            self.sample_id = SampleSampleId(self.sample_id)

        if self._is_empty(self.anatomical_entity):
            self.MissingRequiredField("anatomical_entity")
        if not isinstance(self.anatomical_entity, URIorCURIE):
            self.anatomical_entity = URIorCURIE(self.anatomical_entity)

        if self._is_empty(self.collection_date):
            self.MissingRequiredField("collection_date")
        if not isinstance(self.collection_date, str):
            self.collection_date = str(self.collection_date)

        if self.development_stage is not None and not isinstance(self.development_stage, URIorCURIE):
            self.development_stage = URIorCURIE(self.development_stage)

        if self.sample_description is not None and not isinstance(self.sample_description, str):
            self.sample_description = str(self.sample_description)

        if not isinstance(self.sample_external_ids, list):
            self.sample_external_ids = [self.sample_external_ids] if self.sample_external_ids is not None else []
        self.sample_external_ids = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.sample_external_ids]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservedVariable(YAMLRoot):
    """
    An observed variable describes how a measurement has been made. It typically takes the form of a measured
    characteristic of the observation unit (plant or environmental trait), associated to the method and unit of
    measurement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["ObservedVariable"]
    class_class_curie: ClassVar[str] = "miappe_linkml:ObservedVariable"
    class_name: ClassVar[str] = "ObservedVariable"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.ObservedVariable

    variable_id: Union[str, ObservedVariableVariableId] = None
    variable_name: Optional[str] = None
    variable_accession_number: Optional[Union[str, URIorCURIE]] = None
    trait: Optional[Union[dict, "Trait"]] = None
    method: Optional[Union[dict, "Method"]] = None
    scale: Optional[Union[dict, "Scale"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.variable_id):
            self.MissingRequiredField("variable_id")
        if not isinstance(self.variable_id, ObservedVariableVariableId):
            self.variable_id = ObservedVariableVariableId(self.variable_id)

        if self.variable_name is not None and not isinstance(self.variable_name, str):
            self.variable_name = str(self.variable_name)

        if self.variable_accession_number is not None and not isinstance(self.variable_accession_number, URIorCURIE):
            self.variable_accession_number = URIorCURIE(self.variable_accession_number)

        if self.trait is not None and not isinstance(self.trait, Trait):
            self.trait = Trait(**as_dict(self.trait))

        if self.method is not None and not isinstance(self.method, Method):
            self.method = Method(**as_dict(self.method))

        if self.scale is not None and not isinstance(self.scale, Scale):
            self.scale = Scale(**as_dict(self.scale))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Trait(YAMLRoot):
    """
    The (plant or environmental) trait under observation, optionally described by the entity it is measured on and its
    characteristic.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["Trait"]
    class_class_curie: ClassVar[str] = "miappe_linkml:Trait"
    class_name: ClassVar[str] = "Trait"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.Trait

    trait_name: str = None
    trait_entity: Optional[str] = None
    trait_entity_accession_number: Optional[Union[str, URIorCURIE]] = None
    trait_characteristic: Optional[str] = None
    trait_characteristic_accession_number: Optional[Union[str, URIorCURIE]] = None
    trait_accession_number: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.trait_name):
            self.MissingRequiredField("trait_name")
        if not isinstance(self.trait_name, str):
            self.trait_name = str(self.trait_name)

        if self.trait_entity is not None and not isinstance(self.trait_entity, str):
            self.trait_entity = str(self.trait_entity)

        if self.trait_entity_accession_number is not None and not isinstance(self.trait_entity_accession_number, URIorCURIE):
            self.trait_entity_accession_number = URIorCURIE(self.trait_entity_accession_number)

        if self.trait_characteristic is not None and not isinstance(self.trait_characteristic, str):
            self.trait_characteristic = str(self.trait_characteristic)

        if self.trait_characteristic_accession_number is not None and not isinstance(self.trait_characteristic_accession_number, URIorCURIE):
            self.trait_characteristic_accession_number = URIorCURIE(self.trait_characteristic_accession_number)

        if self.trait_accession_number is not None and not isinstance(self.trait_accession_number, URIorCURIE):
            self.trait_accession_number = URIorCURIE(self.trait_accession_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Method(YAMLRoot):
    """
    The method of observation used to record an observed variable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["Method"]
    class_class_curie: ClassVar[str] = "miappe_linkml:Method"
    class_name: ClassVar[str] = "Method"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.Method

    method_name: str = None
    method_accession_number: Optional[Union[str, URIorCURIE]] = None
    method_description: Optional[str] = None
    method_reference: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.method_name):
            self.MissingRequiredField("method_name")
        if not isinstance(self.method_name, str):
            self.method_name = str(self.method_name)

        if self.method_accession_number is not None and not isinstance(self.method_accession_number, URIorCURIE):
            self.method_accession_number = URIorCURIE(self.method_accession_number)

        if self.method_description is not None and not isinstance(self.method_description, str):
            self.method_description = str(self.method_description)

        if self.method_reference is not None and not isinstance(self.method_reference, URIorCURIE):
            self.method_reference = URIorCURIE(self.method_reference)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Scale(YAMLRoot):
    """
    The scale (unit of measurement) associated with an observed variable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["Scale"]
    class_class_curie: ClassVar[str] = "miappe_linkml:Scale"
    class_name: ClassVar[str] = "Scale"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.Scale

    scale_name: str = None
    scale_accession_number: Optional[Union[str, URIorCURIE]] = None
    time_scale: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.scale_name):
            self.MissingRequiredField("scale_name")
        if not isinstance(self.scale_name, str):
            self.scale_name = str(self.scale_name)

        if self.scale_accession_number is not None and not isinstance(self.scale_accession_number, URIorCURIE):
            self.scale_accession_number = URIorCURIE(self.scale_accession_number)

        if not isinstance(self.time_scale, list):
            self.time_scale = [self.time_scale] if self.time_scale is not None else []
        self.time_scale = [v if isinstance(v, str) else str(v) for v in self.time_scale]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeoReferenced(YAMLRoot):
    """
    A mixin providing decimal geographic coordinates (latitude, longitude, altitude) plus a circular coordinate
    uncertainty, as used for in situ biological material and material sources in MIAPPE.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MIAPPE_LINKML["GeoReferenced"]
    class_class_curie: ClassVar[str] = "miappe_linkml:GeoReferenced"
    class_name: ClassVar[str] = "GeoReferenced"
    class_model_uri: ClassVar[URIRef] = MIAPPE_LINKML.GeoReferenced

    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[str] = None
    coordinates_uncertainty: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.altitude is not None and not isinstance(self.altitude, str):
            self.altitude = str(self.altitude)

        if self.coordinates_uncertainty is not None and not isinstance(self.coordinates_uncertainty, str):
            self.coordinates_uncertainty = str(self.coordinates_uncertainty)

        super().__post_init__(**kwargs)


# Enumerations
class LicenseEnum(EnumDefinitionImpl):
    """
    License for the reuse of the data associated with an investigation. The Creative Commons licenses are recommended.
    """
    cc_by_4_0 = PermissibleValue(
        text="cc_by_4_0",
        description="Creative Commons Attribution 4.0 International.")
    cc_by_sa_4_0 = PermissibleValue(
        text="cc_by_sa_4_0",
        description="Creative Commons Attribution-ShareAlike 4.0 International.")
    cc_by_nc_4_0 = PermissibleValue(
        text="cc_by_nc_4_0",
        description="Creative Commons Attribution-NonCommercial 4.0 International.")
    cc_by_nd_4_0 = PermissibleValue(
        text="cc_by_nd_4_0",
        description="Creative Commons Attribution-NoDerivatives 4.0 International.")
    cc0_1_0 = PermissibleValue(
        text="cc0_1_0",
        description="Creative Commons Public Domain Dedication.")
    unreported = PermissibleValue(
        text="unreported",
        description="The license was not reported.")

    _defn = EnumDefinition(
        name="LicenseEnum",
        description="""License for the reuse of the data associated with an investigation. The Creative Commons licenses are recommended.""",
    )

class ObservationUnitTypeEnum(EnumDefinitionImpl):
    """
    Type of observation unit. Use of other observation unit types is possible but not recommended.
    """
    study = PermissibleValue(
        text="study",
        description="The whole study as an observation unit.")
    block = PermissibleValue(
        text="block",
        description="A block in the experimental design.")
    sub_block = PermissibleValue(
        text="sub_block",
        description="A sub-block in the experimental design.")
    plot = PermissibleValue(
        text="plot",
        description="A plot in the experimental design.")
    sub_plot = PermissibleValue(
        text="sub_plot",
        description="A sub-plot in the experimental design.")
    pot = PermissibleValue(
        text="pot",
        description="A pot containing one or more plants.")
    plant = PermissibleValue(
        text="plant",
        description="An individual plant.")

    _defn = EnumDefinition(
        name="ObservationUnitTypeEnum",
        description="Type of observation unit. Use of other observation unit types is possible but not recommended.",
    )

class ExperimentalFactorTypeEnum(EnumDefinitionImpl):
    """
    Non-exhaustive list of experimental factor types, from MIAPPE Appendix II. Most map to the Plant Environment
    Ontology (EO).
    """
    seasonal_environment = PermissibleValue(
        text="seasonal_environment",
        description="A plant treatment involving an exposure to given conditions of regional seasons.",
        meaning=EO["0007038"])
    air_treatment_regime = PermissibleValue(
        text="air_treatment_regime",
        description="Exposure to wind/air with varying degree of temperature.",
        meaning=EO["0007161"])
    soil_temperature_regime = PermissibleValue(
        text="soil_temperature_regime",
        description="Exposure to varying degree of soil temperature.",
        meaning=EO["0007161"])
    soil_treatment_regime = PermissibleValue(
        text="soil_treatment_regime",
        description="Growing plants and exposing them to soil growth media with varying contents.",
        meaning=EO["0007161"])
    antibiotic_regime = PermissibleValue(
        text="antibiotic_regime",
        description="A chemical treatment involving the use of antibiotics.",
        meaning=EO["0007041"])
    chemical_administration = PermissibleValue(
        text="chemical_administration",
        description="An abiotic plant treatment involving the application of chemicals.",
        meaning=EO["0007189"])
    biotic_treatment = PermissibleValue(
        text="biotic_treatment",
        description="Application of a biotic factor such as a microbe, insect, animal or plant.",
        meaning=EO["0007357"])
    fertilizer_regime = PermissibleValue(
        text="fertilizer_regime",
        description="A plant nutrient treatment involving the use of a fertilizer.",
        meaning=EO["0007085"])
    fungicide_regime = PermissibleValue(
        text="fungicide_regime",
        description="Application of a fungicide.",
        meaning=EO["0007268"])
    gaseous_regime = PermissibleValue(
        text="gaseous_regime",
        description="Application of a gas or a combination of gasses.",
        meaning=EO["0007023"])
    gravity = PermissibleValue(
        text="gravity",
        description="Use of gravity to study responses in presence, absence or modified levels of gravity.",
        meaning=EO["0007146"])
    plant_hormone_regime = PermissibleValue(
        text="plant_hormone_regime",
        description="Use of growth hormones.",
        meaning=EO["0007165"])
    herbicide_regime = PermissibleValue(
        text="herbicide_regime",
        description="Application of a herbicide.",
        meaning=EO["0007183"])
    mechanical_treatment = PermissibleValue(
        text="mechanical_treatment",
        description="Application of a mechanical force.",
        meaning=EO["0007373"])
    chemical_regime = PermissibleValue(
        text="chemical_regime",
        description="Application of inorganic chemicals, nutriment or organic chemicals as a supplement.",
        meaning=EO["0007044"])
    humidity_regimen = PermissibleValue(
        text="humidity_regimen",
        description="Exposure to varying degree of humidity.",
        meaning=EO["0007359"])
    radiation_regime = PermissibleValue(
        text="radiation_regime",
        description="Exposure to a radiation type, intensity or quantity (light, UV-B, X-ray).",
        meaning=EO["0007151"])
    rainfall_regime = PermissibleValue(
        text="rainfall_regime",
        description="Exposure to a given amount of rainfall.",
        meaning=EO["0007181"])
    salt_regime = PermissibleValue(
        text="salt_regime",
        description="Use of salts as a supplement to growth media.",
        meaning=EO["0007185"])
    watering_regime = PermissibleValue(
        text="watering_regime",
        description="Exposure to watering frequencies.",
        meaning=EO["0007383"])
    water_temperature_regime = PermissibleValue(
        text="water_temperature_regime",
        description="Exposure to water with varying degree of temperature.",
        meaning=EO["0007160"])
    standing_water_regime = PermissibleValue(
        text="standing_water_regime",
        description="Exposure to standing water during a plant's life span.",
        meaning=EO["0007282"])
    pesticide_regime = PermissibleValue(
        text="pesticide_regime",
        description="Application of a pesticide.",
        meaning=EO["0007167"])
    ph_regime = PermissibleValue(
        text="ph_regime",
        description="Exposure to varying levels of pH of the growth media.",
        meaning=EO["0007171"])
    other_perturbation = PermissibleValue(
        text="other_perturbation",
        description="Any other perturbation not covered by the listed factor types.")

    _defn = EnumDefinition(
        name="ExperimentalFactorTypeEnum",
        description="""Non-exhaustive list of experimental factor types, from MIAPPE Appendix II. Most map to the Plant Environment Ontology (EO).""",
    )

# Slots
class slots:
    pass

slots.investigation_id = Slot(uri=SCHEMA.identifier, name="investigation_id", curie=SCHEMA.curie('identifier'),
                   model_uri=MIAPPE_LINKML.investigation_id, domain=None, range=URIRef)

slots.investigation_title = Slot(uri=DCTERMS.title, name="investigation_title", curie=DCTERMS.curie('title'),
                   model_uri=MIAPPE_LINKML.investigation_title, domain=None, range=str)

slots.investigation_description = Slot(uri=DCTERMS.description, name="investigation_description", curie=DCTERMS.curie('description'),
                   model_uri=MIAPPE_LINKML.investigation_description, domain=None, range=Optional[str])

slots.submission_date = Slot(uri=MIAPPE_LINKML.submission_date, name="submission_date", curie=MIAPPE_LINKML.curie('submission_date'),
                   model_uri=MIAPPE_LINKML.submission_date, domain=None, range=Optional[Union[str, str]])

slots.public_release_date = Slot(uri=MIAPPE_LINKML.public_release_date, name="public_release_date", curie=MIAPPE_LINKML.curie('public_release_date'),
                   model_uri=MIAPPE_LINKML.public_release_date, domain=None, range=Optional[Union[str, str]])

slots.license = Slot(uri=MIAPPE_LINKML.license, name="license", curie=MIAPPE_LINKML.curie('license'),
                   model_uri=MIAPPE_LINKML.license, domain=None, range=Optional[Union[str, "LicenseEnum"]])

slots.miappe_version = Slot(uri=MIAPPE_LINKML.miappe_version, name="miappe_version", curie=MIAPPE_LINKML.curie('miappe_version'),
                   model_uri=MIAPPE_LINKML.miappe_version, domain=None, range=str)

slots.associated_publications = Slot(uri=MIAPPE_LINKML.associated_publications, name="associated_publications", curie=MIAPPE_LINKML.curie('associated_publications'),
                   model_uri=MIAPPE_LINKML.associated_publications, domain=None, range=Optional[Union[Union[dict, Publication], list[Union[dict, Publication]]]])

slots.associated_publication = Slot(uri=MIAPPE_LINKML.associated_publication, name="associated_publication", curie=MIAPPE_LINKML.curie('associated_publication'),
                   model_uri=MIAPPE_LINKML.associated_publication, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.study_id = Slot(uri=SCHEMA.identifier, name="study_id", curie=SCHEMA.curie('identifier'),
                   model_uri=MIAPPE_LINKML.study_id, domain=None, range=URIRef)

slots.study_title = Slot(uri=DCTERMS.title, name="study_title", curie=DCTERMS.curie('title'),
                   model_uri=MIAPPE_LINKML.study_title, domain=None, range=str)

slots.study_description = Slot(uri=DCTERMS.description, name="study_description", curie=DCTERMS.curie('description'),
                   model_uri=MIAPPE_LINKML.study_description, domain=None, range=Optional[str])

slots.study_start_date = Slot(uri=MIAPPE_LINKML.study_start_date, name="study_start_date", curie=MIAPPE_LINKML.curie('study_start_date'),
                   model_uri=MIAPPE_LINKML.study_start_date, domain=None, range=Union[str, str])

slots.study_end_date = Slot(uri=MIAPPE_LINKML.study_end_date, name="study_end_date", curie=MIAPPE_LINKML.curie('study_end_date'),
                   model_uri=MIAPPE_LINKML.study_end_date, domain=None, range=Optional[Union[str, str]])

slots.contact_institution = Slot(uri=MIAPPE_LINKML.contact_institution, name="contact_institution", curie=MIAPPE_LINKML.curie('contact_institution'),
                   model_uri=MIAPPE_LINKML.contact_institution, domain=None, range=str)

slots.location_country = Slot(uri=MIAPPE_LINKML.location_country, name="location_country", curie=MIAPPE_LINKML.curie('location_country'),
                   model_uri=MIAPPE_LINKML.location_country, domain=None, range=str)

slots.site_name = Slot(uri=MIAPPE_LINKML.site_name, name="site_name", curie=MIAPPE_LINKML.curie('site_name'),
                   model_uri=MIAPPE_LINKML.site_name, domain=None, range=str)

slots.location_latitude = Slot(uri=MIAPPE_LINKML.location_latitude, name="location_latitude", curie=MIAPPE_LINKML.curie('location_latitude'),
                   model_uri=MIAPPE_LINKML.location_latitude, domain=None, range=Optional[float])

slots.location_longitude = Slot(uri=MIAPPE_LINKML.location_longitude, name="location_longitude", curie=MIAPPE_LINKML.curie('location_longitude'),
                   model_uri=MIAPPE_LINKML.location_longitude, domain=None, range=Optional[float])

slots.location_altitude = Slot(uri=MIAPPE_LINKML.location_altitude, name="location_altitude", curie=MIAPPE_LINKML.curie('location_altitude'),
                   model_uri=MIAPPE_LINKML.location_altitude, domain=None, range=Optional[str])

slots.experimental_design_description = Slot(uri=MIAPPE_LINKML.experimental_design_description, name="experimental_design_description", curie=MIAPPE_LINKML.curie('experimental_design_description'),
                   model_uri=MIAPPE_LINKML.experimental_design_description, domain=None, range=str)

slots.experimental_design_type = Slot(uri=MIAPPE_LINKML.experimental_design_type, name="experimental_design_type", curie=MIAPPE_LINKML.curie('experimental_design_type'),
                   model_uri=MIAPPE_LINKML.experimental_design_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.observation_unit_level_hierarchy = Slot(uri=MIAPPE_LINKML.observation_unit_level_hierarchy, name="observation_unit_level_hierarchy", curie=MIAPPE_LINKML.curie('observation_unit_level_hierarchy'),
                   model_uri=MIAPPE_LINKML.observation_unit_level_hierarchy, domain=None, range=Optional[str])

slots.observation_unit_description = Slot(uri=MIAPPE_LINKML.observation_unit_description, name="observation_unit_description", curie=MIAPPE_LINKML.curie('observation_unit_description'),
                   model_uri=MIAPPE_LINKML.observation_unit_description, domain=None, range=str)

slots.growth_facility_description = Slot(uri=MIAPPE_LINKML.growth_facility_description, name="growth_facility_description", curie=MIAPPE_LINKML.curie('growth_facility_description'),
                   model_uri=MIAPPE_LINKML.growth_facility_description, domain=None, range=str)

slots.growth_facility_type = Slot(uri=MIAPPE_LINKML.growth_facility_type, name="growth_facility_type", curie=MIAPPE_LINKML.curie('growth_facility_type'),
                   model_uri=MIAPPE_LINKML.growth_facility_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.cultural_practices = Slot(uri=MIAPPE_LINKML.cultural_practices, name="cultural_practices", curie=MIAPPE_LINKML.curie('cultural_practices'),
                   model_uri=MIAPPE_LINKML.cultural_practices, domain=None, range=Optional[str])

slots.experimental_design_map = Slot(uri=MIAPPE_LINKML.experimental_design_map, name="experimental_design_map", curie=MIAPPE_LINKML.curie('experimental_design_map'),
                   model_uri=MIAPPE_LINKML.experimental_design_map, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.person_id = Slot(uri=MIAPPE_LINKML.person_id, name="person_id", curie=MIAPPE_LINKML.curie('person_id'),
                   model_uri=MIAPPE_LINKML.person_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.person_name = Slot(uri=SCHEMA.name, name="person_name", curie=SCHEMA.curie('name'),
                   model_uri=MIAPPE_LINKML.person_name, domain=None, range=str)

slots.person_email = Slot(uri=SCHEMA.email, name="person_email", curie=SCHEMA.curie('email'),
                   model_uri=MIAPPE_LINKML.person_email, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.person_roles = Slot(uri=MIAPPE_LINKML.person_roles, name="person_roles", curie=MIAPPE_LINKML.curie('person_roles'),
                   model_uri=MIAPPE_LINKML.person_roles, domain=None, range=Union[str, list[str]])

slots.person_affiliations = Slot(uri=MIAPPE_LINKML.person_affiliations, name="person_affiliations", curie=MIAPPE_LINKML.curie('person_affiliations'),
                   model_uri=MIAPPE_LINKML.person_affiliations, domain=None, range=Union[str, list[str]])

slots.data_file_link = Slot(uri=MIAPPE_LINKML.data_file_link, name="data_file_link", curie=MIAPPE_LINKML.curie('data_file_link'),
                   model_uri=MIAPPE_LINKML.data_file_link, domain=None, range=Union[str, URI])

slots.data_file_description = Slot(uri=MIAPPE_LINKML.data_file_description, name="data_file_description", curie=MIAPPE_LINKML.curie('data_file_description'),
                   model_uri=MIAPPE_LINKML.data_file_description, domain=None, range=str)

slots.data_file_version = Slot(uri=MIAPPE_LINKML.data_file_version, name="data_file_version", curie=MIAPPE_LINKML.curie('data_file_version'),
                   model_uri=MIAPPE_LINKML.data_file_version, domain=None, range=Optional[str])

slots.biological_material_id = Slot(uri=MIAPPE_LINKML.biological_material_id, name="biological_material_id", curie=MIAPPE_LINKML.curie('biological_material_id'),
                   model_uri=MIAPPE_LINKML.biological_material_id, domain=None, range=URIRef)

slots.biological_material_external_ids = Slot(uri=MIAPPE_LINKML.biological_material_external_ids, name="biological_material_external_ids", curie=MIAPPE_LINKML.curie('biological_material_external_ids'),
                   model_uri=MIAPPE_LINKML.biological_material_external_ids, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.organism = Slot(uri=MIAPPE_LINKML.organism, name="organism", curie=MIAPPE_LINKML.curie('organism'),
                   model_uri=MIAPPE_LINKML.organism, domain=None, range=Union[str, URIorCURIE])

slots.genus = Slot(uri=MIAPPE_LINKML.genus, name="genus", curie=MIAPPE_LINKML.curie('genus'),
                   model_uri=MIAPPE_LINKML.genus, domain=None, range=Optional[str])

slots.species = Slot(uri=MIAPPE_LINKML.species, name="species", curie=MIAPPE_LINKML.curie('species'),
                   model_uri=MIAPPE_LINKML.species, domain=None, range=Optional[str])

slots.infraspecific_name = Slot(uri=MIAPPE_LINKML.infraspecific_name, name="infraspecific_name", curie=MIAPPE_LINKML.curie('infraspecific_name'),
                   model_uri=MIAPPE_LINKML.infraspecific_name, domain=None, range=Optional[str])

slots.biological_material_preprocessing = Slot(uri=MIAPPE_LINKML.biological_material_preprocessing, name="biological_material_preprocessing", curie=MIAPPE_LINKML.curie('biological_material_preprocessing'),
                   model_uri=MIAPPE_LINKML.biological_material_preprocessing, domain=None, range=Optional[Union[str, list[str]]])

slots.material_source = Slot(uri=MIAPPE_LINKML.material_source, name="material_source", curie=MIAPPE_LINKML.curie('material_source'),
                   model_uri=MIAPPE_LINKML.material_source, domain=None, range=Optional[Union[dict, MaterialSource]])

slots.material_source_id = Slot(uri=MIAPPE_LINKML.material_source_id, name="material_source_id", curie=MIAPPE_LINKML.curie('material_source_id'),
                   model_uri=MIAPPE_LINKML.material_source_id, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.material_source_doi = Slot(uri=MIAPPE_LINKML.material_source_doi, name="material_source_doi", curie=MIAPPE_LINKML.curie('material_source_doi'),
                   model_uri=MIAPPE_LINKML.material_source_doi, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.material_source_accession_number = Slot(uri=MIAPPE_LINKML.material_source_accession_number, name="material_source_accession_number", curie=MIAPPE_LINKML.curie('material_source_accession_number'),
                   model_uri=MIAPPE_LINKML.material_source_accession_number, domain=None, range=Optional[str])

slots.material_source_accession_name = Slot(uri=MIAPPE_LINKML.material_source_accession_name, name="material_source_accession_name", curie=MIAPPE_LINKML.curie('material_source_accession_name'),
                   model_uri=MIAPPE_LINKML.material_source_accession_name, domain=None, range=Optional[str])

slots.material_source_institute_code = Slot(uri=MIAPPE_LINKML.material_source_institute_code, name="material_source_institute_code", curie=MIAPPE_LINKML.curie('material_source_institute_code'),
                   model_uri=MIAPPE_LINKML.material_source_institute_code, domain=None, range=Optional[str])

slots.material_source_institute_name = Slot(uri=MIAPPE_LINKML.material_source_institute_name, name="material_source_institute_name", curie=MIAPPE_LINKML.curie('material_source_institute_name'),
                   model_uri=MIAPPE_LINKML.material_source_institute_name, domain=None, range=Optional[str])

slots.material_source_other_ids = Slot(uri=MIAPPE_LINKML.material_source_other_ids, name="material_source_other_ids", curie=MIAPPE_LINKML.curie('material_source_other_ids'),
                   model_uri=MIAPPE_LINKML.material_source_other_ids, domain=None, range=Optional[str])

slots.material_source_description = Slot(uri=MIAPPE_LINKML.material_source_description, name="material_source_description", curie=MIAPPE_LINKML.curie('material_source_description'),
                   model_uri=MIAPPE_LINKML.material_source_description, domain=None, range=Optional[str])

slots.environment_parameter_name = Slot(uri=MIAPPE_LINKML.environment_parameter_name, name="environment_parameter_name", curie=MIAPPE_LINKML.curie('environment_parameter_name'),
                   model_uri=MIAPPE_LINKML.environment_parameter_name, domain=None, range=str)

slots.environment_parameter_value = Slot(uri=MIAPPE_LINKML.environment_parameter_value, name="environment_parameter_value", curie=MIAPPE_LINKML.curie('environment_parameter_value'),
                   model_uri=MIAPPE_LINKML.environment_parameter_value, domain=None, range=str)

slots.experimental_factor_type = Slot(uri=MIAPPE_LINKML.experimental_factor_type, name="experimental_factor_type", curie=MIAPPE_LINKML.curie('experimental_factor_type'),
                   model_uri=MIAPPE_LINKML.experimental_factor_type, domain=None, range=Union[str, "ExperimentalFactorTypeEnum"])

slots.experimental_factor_description = Slot(uri=MIAPPE_LINKML.experimental_factor_description, name="experimental_factor_description", curie=MIAPPE_LINKML.curie('experimental_factor_description'),
                   model_uri=MIAPPE_LINKML.experimental_factor_description, domain=None, range=Optional[str])

slots.experimental_factor_values = Slot(uri=MIAPPE_LINKML.experimental_factor_values, name="experimental_factor_values", curie=MIAPPE_LINKML.curie('experimental_factor_values'),
                   model_uri=MIAPPE_LINKML.experimental_factor_values, domain=None, range=Optional[Union[str, list[str]]])

slots.event_type = Slot(uri=MIAPPE_LINKML.event_type, name="event_type", curie=MIAPPE_LINKML.curie('event_type'),
                   model_uri=MIAPPE_LINKML.event_type, domain=None, range=str)

slots.event_accession_number = Slot(uri=MIAPPE_LINKML.event_accession_number, name="event_accession_number", curie=MIAPPE_LINKML.curie('event_accession_number'),
                   model_uri=MIAPPE_LINKML.event_accession_number, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.event_description = Slot(uri=MIAPPE_LINKML.event_description, name="event_description", curie=MIAPPE_LINKML.curie('event_description'),
                   model_uri=MIAPPE_LINKML.event_description, domain=None, range=Optional[str])

slots.event_dates = Slot(uri=MIAPPE_LINKML.event_dates, name="event_dates", curie=MIAPPE_LINKML.curie('event_dates'),
                   model_uri=MIAPPE_LINKML.event_dates, domain=None, range=Union[Union[str, str], list[Union[str, str]]])

slots.observation_unit_id = Slot(uri=MIAPPE_LINKML.observation_unit_id, name="observation_unit_id", curie=MIAPPE_LINKML.curie('observation_unit_id'),
                   model_uri=MIAPPE_LINKML.observation_unit_id, domain=None, range=URIRef)

slots.observation_unit_type = Slot(uri=MIAPPE_LINKML.observation_unit_type, name="observation_unit_type", curie=MIAPPE_LINKML.curie('observation_unit_type'),
                   model_uri=MIAPPE_LINKML.observation_unit_type, domain=None, range=Union[str, "ObservationUnitTypeEnum"])

slots.observation_unit_external_ids = Slot(uri=MIAPPE_LINKML.observation_unit_external_ids, name="observation_unit_external_ids", curie=MIAPPE_LINKML.curie('observation_unit_external_ids'),
                   model_uri=MIAPPE_LINKML.observation_unit_external_ids, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.spatial_distribution = Slot(uri=MIAPPE_LINKML.spatial_distribution, name="spatial_distribution", curie=MIAPPE_LINKML.curie('spatial_distribution'),
                   model_uri=MIAPPE_LINKML.spatial_distribution, domain=None, range=Optional[Union[str, list[str]]])

slots.observation_unit_factor_values = Slot(uri=MIAPPE_LINKML.observation_unit_factor_values, name="observation_unit_factor_values", curie=MIAPPE_LINKML.curie('observation_unit_factor_values'),
                   model_uri=MIAPPE_LINKML.observation_unit_factor_values, domain=None, range=Optional[Union[str, list[str]]])

slots.biological_material = Slot(uri=MIAPPE_LINKML.biological_material, name="biological_material", curie=MIAPPE_LINKML.curie('biological_material'),
                   model_uri=MIAPPE_LINKML.biological_material, domain=None, range=Optional[Union[Union[str, BiologicalMaterialBiologicalMaterialId], list[Union[str, BiologicalMaterialBiologicalMaterialId]]]])

slots.sample_id = Slot(uri=MIAPPE_LINKML.sample_id, name="sample_id", curie=MIAPPE_LINKML.curie('sample_id'),
                   model_uri=MIAPPE_LINKML.sample_id, domain=None, range=URIRef)

slots.development_stage = Slot(uri=MIAPPE_LINKML.development_stage, name="development_stage", curie=MIAPPE_LINKML.curie('development_stage'),
                   model_uri=MIAPPE_LINKML.development_stage, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.anatomical_entity = Slot(uri=MIAPPE_LINKML.anatomical_entity, name="anatomical_entity", curie=MIAPPE_LINKML.curie('anatomical_entity'),
                   model_uri=MIAPPE_LINKML.anatomical_entity, domain=None, range=Union[str, URIorCURIE])

slots.sample_description = Slot(uri=MIAPPE_LINKML.sample_description, name="sample_description", curie=MIAPPE_LINKML.curie('sample_description'),
                   model_uri=MIAPPE_LINKML.sample_description, domain=None, range=Optional[str])

slots.collection_date = Slot(uri=MIAPPE_LINKML.collection_date, name="collection_date", curie=MIAPPE_LINKML.curie('collection_date'),
                   model_uri=MIAPPE_LINKML.collection_date, domain=None, range=Union[str, str])

slots.sample_external_ids = Slot(uri=MIAPPE_LINKML.sample_external_ids, name="sample_external_ids", curie=MIAPPE_LINKML.curie('sample_external_ids'),
                   model_uri=MIAPPE_LINKML.sample_external_ids, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.variable_id = Slot(uri=MIAPPE_LINKML.variable_id, name="variable_id", curie=MIAPPE_LINKML.curie('variable_id'),
                   model_uri=MIAPPE_LINKML.variable_id, domain=None, range=URIRef)

slots.variable_name = Slot(uri=MIAPPE_LINKML.variable_name, name="variable_name", curie=MIAPPE_LINKML.curie('variable_name'),
                   model_uri=MIAPPE_LINKML.variable_name, domain=None, range=Optional[str])

slots.variable_accession_number = Slot(uri=MIAPPE_LINKML.variable_accession_number, name="variable_accession_number", curie=MIAPPE_LINKML.curie('variable_accession_number'),
                   model_uri=MIAPPE_LINKML.variable_accession_number, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.trait = Slot(uri=MIAPPE_LINKML.trait, name="trait", curie=MIAPPE_LINKML.curie('trait'),
                   model_uri=MIAPPE_LINKML.trait, domain=None, range=Optional[Union[dict, Trait]])

slots.method = Slot(uri=MIAPPE_LINKML.method, name="method", curie=MIAPPE_LINKML.curie('method'),
                   model_uri=MIAPPE_LINKML.method, domain=None, range=Optional[Union[dict, Method]])

slots.scale = Slot(uri=MIAPPE_LINKML.scale, name="scale", curie=MIAPPE_LINKML.curie('scale'),
                   model_uri=MIAPPE_LINKML.scale, domain=None, range=Optional[Union[dict, Scale]])

slots.trait_name = Slot(uri=MIAPPE_LINKML.trait_name, name="trait_name", curie=MIAPPE_LINKML.curie('trait_name'),
                   model_uri=MIAPPE_LINKML.trait_name, domain=None, range=str)

slots.trait_entity = Slot(uri=MIAPPE_LINKML.trait_entity, name="trait_entity", curie=MIAPPE_LINKML.curie('trait_entity'),
                   model_uri=MIAPPE_LINKML.trait_entity, domain=None, range=Optional[str])

slots.trait_entity_accession_number = Slot(uri=MIAPPE_LINKML.trait_entity_accession_number, name="trait_entity_accession_number", curie=MIAPPE_LINKML.curie('trait_entity_accession_number'),
                   model_uri=MIAPPE_LINKML.trait_entity_accession_number, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.trait_characteristic = Slot(uri=MIAPPE_LINKML.trait_characteristic, name="trait_characteristic", curie=MIAPPE_LINKML.curie('trait_characteristic'),
                   model_uri=MIAPPE_LINKML.trait_characteristic, domain=None, range=Optional[str])

slots.trait_characteristic_accession_number = Slot(uri=MIAPPE_LINKML.trait_characteristic_accession_number, name="trait_characteristic_accession_number", curie=MIAPPE_LINKML.curie('trait_characteristic_accession_number'),
                   model_uri=MIAPPE_LINKML.trait_characteristic_accession_number, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.trait_accession_number = Slot(uri=MIAPPE_LINKML.trait_accession_number, name="trait_accession_number", curie=MIAPPE_LINKML.curie('trait_accession_number'),
                   model_uri=MIAPPE_LINKML.trait_accession_number, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.method_name = Slot(uri=MIAPPE_LINKML.method_name, name="method_name", curie=MIAPPE_LINKML.curie('method_name'),
                   model_uri=MIAPPE_LINKML.method_name, domain=None, range=str)

slots.method_accession_number = Slot(uri=MIAPPE_LINKML.method_accession_number, name="method_accession_number", curie=MIAPPE_LINKML.curie('method_accession_number'),
                   model_uri=MIAPPE_LINKML.method_accession_number, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.method_description = Slot(uri=MIAPPE_LINKML.method_description, name="method_description", curie=MIAPPE_LINKML.curie('method_description'),
                   model_uri=MIAPPE_LINKML.method_description, domain=None, range=Optional[str])

slots.method_reference = Slot(uri=MIAPPE_LINKML.method_reference, name="method_reference", curie=MIAPPE_LINKML.curie('method_reference'),
                   model_uri=MIAPPE_LINKML.method_reference, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.scale_name = Slot(uri=MIAPPE_LINKML.scale_name, name="scale_name", curie=MIAPPE_LINKML.curie('scale_name'),
                   model_uri=MIAPPE_LINKML.scale_name, domain=None, range=str)

slots.scale_accession_number = Slot(uri=MIAPPE_LINKML.scale_accession_number, name="scale_accession_number", curie=MIAPPE_LINKML.curie('scale_accession_number'),
                   model_uri=MIAPPE_LINKML.scale_accession_number, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.time_scale = Slot(uri=MIAPPE_LINKML.time_scale, name="time_scale", curie=MIAPPE_LINKML.curie('time_scale'),
                   model_uri=MIAPPE_LINKML.time_scale, domain=None, range=Optional[Union[str, list[str]]])

slots.studies = Slot(uri=MIAPPE_LINKML.studies, name="studies", curie=MIAPPE_LINKML.curie('studies'),
                   model_uri=MIAPPE_LINKML.studies, domain=None, range=Union[dict[Union[str, StudyStudyId], Union[dict, Study]], list[Union[dict, Study]]])

slots.persons = Slot(uri=MIAPPE_LINKML.persons, name="persons", curie=MIAPPE_LINKML.curie('persons'),
                   model_uri=MIAPPE_LINKML.persons, domain=None, range=Optional[Union[Union[dict, Person], list[Union[dict, Person]]]])

slots.data_files = Slot(uri=MIAPPE_LINKML.data_files, name="data_files", curie=MIAPPE_LINKML.curie('data_files'),
                   model_uri=MIAPPE_LINKML.data_files, domain=None, range=Optional[Union[Union[dict, DataFile], list[Union[dict, DataFile]]]])

slots.biological_materials = Slot(uri=MIAPPE_LINKML.biological_materials, name="biological_materials", curie=MIAPPE_LINKML.curie('biological_materials'),
                   model_uri=MIAPPE_LINKML.biological_materials, domain=None, range=Optional[Union[dict[Union[str, BiologicalMaterialBiologicalMaterialId], Union[dict, BiologicalMaterial]], list[Union[dict, BiologicalMaterial]]]])

slots.environment_parameters = Slot(uri=MIAPPE_LINKML.environment_parameters, name="environment_parameters", curie=MIAPPE_LINKML.curie('environment_parameters'),
                   model_uri=MIAPPE_LINKML.environment_parameters, domain=None, range=Optional[Union[Union[dict, EnvironmentParameter], list[Union[dict, EnvironmentParameter]]]])

slots.experimental_factors = Slot(uri=MIAPPE_LINKML.experimental_factors, name="experimental_factors", curie=MIAPPE_LINKML.curie('experimental_factors'),
                   model_uri=MIAPPE_LINKML.experimental_factors, domain=None, range=Optional[Union[Union[dict, ExperimentalFactor], list[Union[dict, ExperimentalFactor]]]])

slots.events = Slot(uri=MIAPPE_LINKML.events, name="events", curie=MIAPPE_LINKML.curie('events'),
                   model_uri=MIAPPE_LINKML.events, domain=None, range=Optional[Union[Union[dict, Event], list[Union[dict, Event]]]])

slots.observation_units = Slot(uri=MIAPPE_LINKML.observation_units, name="observation_units", curie=MIAPPE_LINKML.curie('observation_units'),
                   model_uri=MIAPPE_LINKML.observation_units, domain=None, range=Union[dict[Union[str, ObservationUnitObservationUnitId], Union[dict, ObservationUnit]], list[Union[dict, ObservationUnit]]])

slots.observed_variables = Slot(uri=MIAPPE_LINKML.observed_variables, name="observed_variables", curie=MIAPPE_LINKML.curie('observed_variables'),
                   model_uri=MIAPPE_LINKML.observed_variables, domain=None, range=Union[dict[Union[str, ObservedVariableVariableId], Union[dict, ObservedVariable]], list[Union[dict, ObservedVariable]]])

slots.samples = Slot(uri=MIAPPE_LINKML.samples, name="samples", curie=MIAPPE_LINKML.curie('samples'),
                   model_uri=MIAPPE_LINKML.samples, domain=None, range=Optional[Union[dict[Union[str, SampleSampleId], Union[dict, Sample]], list[Union[dict, Sample]]]])

slots.latitude = Slot(uri=MIAPPE_LINKML.latitude, name="latitude", curie=MIAPPE_LINKML.curie('latitude'),
                   model_uri=MIAPPE_LINKML.latitude, domain=None, range=Optional[float])

slots.longitude = Slot(uri=MIAPPE_LINKML.longitude, name="longitude", curie=MIAPPE_LINKML.curie('longitude'),
                   model_uri=MIAPPE_LINKML.longitude, domain=None, range=Optional[float])

slots.altitude = Slot(uri=MIAPPE_LINKML.altitude, name="altitude", curie=MIAPPE_LINKML.curie('altitude'),
                   model_uri=MIAPPE_LINKML.altitude, domain=None, range=Optional[str])

slots.coordinates_uncertainty = Slot(uri=MIAPPE_LINKML.coordinates_uncertainty, name="coordinates_uncertainty", curie=MIAPPE_LINKML.curie('coordinates_uncertainty'),
                   model_uri=MIAPPE_LINKML.coordinates_uncertainty, domain=None, range=Optional[str])

