from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'miappe_linkml',
     'default_range': 'string',
     'description': 'A LinkML representation of the MIAPPE (Minimum Information '
                    'About a Plant Phenotyping Experiment) v1.1 checklist and data '
                    'model. The structure follows the MIAPPE entity relationship '
                    'diagram (Investigation > Study > Observation Unit > Sample) '
                    'together with the supporting entities (Person, Publication, '
                    'Biological Material, Environment Parameter, Experimental '
                    'Factor, Event, Data File and Observed Variable). Each slot '
                    'records its MIAPPE "codename" in a comment, and enumerations '
                    'are derived from the MIAPPE checklist and its appendices.',
     'id': 'https://w3id.org/sierra-moxon/miappe-linkml',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'miappe-linkml',
     'prefixes': {'CO_322': {'prefix_prefix': 'CO_322',
                             'prefix_reference': 'http://www.cropontology.org/rdf/CO_322_'},
                  'CO_715': {'prefix_prefix': 'CO_715',
                             'prefix_reference': 'http://www.cropontology.org/rdf/CO_715_'},
                  'EO': {'prefix_prefix': 'EO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/EO_'},
                  'NCBITaxon': {'prefix_prefix': 'NCBITaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'PO': {'prefix_prefix': 'PO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/PO_'},
                  'TO': {'prefix_prefix': 'TO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/TO_'},
                  'XEO': {'prefix_prefix': 'XEO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/XEO_'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'miappe_linkml': {'prefix_prefix': 'miappe_linkml',
                                    'prefix_reference': 'https://w3id.org/sierra-moxon/miappe-linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://github.com/MIAPPE/MIAPPE', 'https://www.miappe.org/'],
     'source_file': 'src/miappe_linkml/schema/miappe_linkml.yaml',
     'title': 'MIAPPE LinkML'} )

class LicenseEnum(str, Enum):
    """
    License for the reuse of the data associated with an investigation. The Creative Commons licenses are recommended.
    """
    cc_by_4_0 = "cc_by_4_0"
    """
    Creative Commons Attribution 4.0 International.
    """
    cc_by_sa_4_0 = "cc_by_sa_4_0"
    """
    Creative Commons Attribution-ShareAlike 4.0 International.
    """
    cc_by_nc_4_0 = "cc_by_nc_4_0"
    """
    Creative Commons Attribution-NonCommercial 4.0 International.
    """
    cc_by_nd_4_0 = "cc_by_nd_4_0"
    """
    Creative Commons Attribution-NoDerivatives 4.0 International.
    """
    cc0_1_0 = "cc0_1_0"
    """
    Creative Commons Public Domain Dedication.
    """
    unreported = "unreported"
    """
    The license was not reported.
    """


class ObservationUnitTypeEnum(str, Enum):
    """
    Type of observation unit. Use of other observation unit types is possible but not recommended.
    """
    study = "study"
    """
    The whole study as an observation unit.
    """
    block = "block"
    """
    A block in the experimental design.
    """
    sub_block = "sub_block"
    """
    A sub-block in the experimental design.
    """
    plot = "plot"
    """
    A plot in the experimental design.
    """
    sub_plot = "sub_plot"
    """
    A sub-plot in the experimental design.
    """
    pot = "pot"
    """
    A pot containing one or more plants.
    """
    plant = "plant"
    """
    An individual plant.
    """


class ExperimentalFactorTypeEnum(str, Enum):
    """
    Non-exhaustive list of experimental factor types, from MIAPPE Appendix II. Most map to the Plant Environment Ontology (EO).
    """
    seasonal_environment = "seasonal_environment"
    """
    A plant treatment involving an exposure to given conditions of regional seasons.
    """
    air_treatment_regime = "air_treatment_regime"
    """
    Exposure to wind/air with varying degree of temperature.
    """
    soil_temperature_regime = "soil_temperature_regime"
    """
    Exposure to varying degree of soil temperature.
    """
    soil_treatment_regime = "soil_treatment_regime"
    """
    Growing plants and exposing them to soil growth media with varying contents.
    """
    antibiotic_regime = "antibiotic_regime"
    """
    A chemical treatment involving the use of antibiotics.
    """
    chemical_administration = "chemical_administration"
    """
    An abiotic plant treatment involving the application of chemicals.
    """
    biotic_treatment = "biotic_treatment"
    """
    Application of a biotic factor such as a microbe, insect, animal or plant.
    """
    fertilizer_regime = "fertilizer_regime"
    """
    A plant nutrient treatment involving the use of a fertilizer.
    """
    fungicide_regime = "fungicide_regime"
    """
    Application of a fungicide.
    """
    gaseous_regime = "gaseous_regime"
    """
    Application of a gas or a combination of gasses.
    """
    gravity = "gravity"
    """
    Use of gravity to study responses in presence, absence or modified levels of gravity.
    """
    plant_hormone_regime = "plant_hormone_regime"
    """
    Use of growth hormones.
    """
    herbicide_regime = "herbicide_regime"
    """
    Application of a herbicide.
    """
    mechanical_treatment = "mechanical_treatment"
    """
    Application of a mechanical force.
    """
    chemical_regime = "chemical_regime"
    """
    Application of inorganic chemicals, nutriment or organic chemicals as a supplement.
    """
    humidity_regimen = "humidity_regimen"
    """
    Exposure to varying degree of humidity.
    """
    radiation_regime = "radiation_regime"
    """
    Exposure to a radiation type, intensity or quantity (light, UV-B, X-ray).
    """
    rainfall_regime = "rainfall_regime"
    """
    Exposure to a given amount of rainfall.
    """
    salt_regime = "salt_regime"
    """
    Use of salts as a supplement to growth media.
    """
    watering_regime = "watering_regime"
    """
    Exposure to watering frequencies.
    """
    water_temperature_regime = "water_temperature_regime"
    """
    Exposure to water with varying degree of temperature.
    """
    standing_water_regime = "standing_water_regime"
    """
    Exposure to standing water during a plant's life span.
    """
    pesticide_regime = "pesticide_regime"
    """
    Application of a pesticide.
    """
    ph_regime = "ph_regime"
    """
    Exposure to varying levels of pH of the growth media.
    """
    other_perturbation = "other_perturbation"
    """
    Any other perturbation not covered by the listed factor types.
    """



class Investigation(ConfiguredBaseModel):
    """
    Investigations are research programmes with defined aims. They can exist at various scales (for example, they could encompass a grant-funded programme of work, the various components comprising a peer-reviewed publication, or a single experiment). One investigation is expected per MIAPPE submission.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml',
         'tree_root': True})

    investigation_id: str = Field(default=..., description="""Identifier comprising the unique name of the institution/database hosting the submission of the investigation data, and the accession number of the investigation in that institution.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: investigationId'],
         'domain_of': ['Investigation'],
         'examples': [{'value': 'EBI:12345678'}],
         'slot_uri': 'schema:identifier'} })
    investigation_title: str = Field(default=..., description="""Human-readable string summarising the investigation.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: investigationTitle'],
         'domain_of': ['Investigation'],
         'slot_uri': 'dcterms:title'} })
    investigation_description: Optional[str] = Field(default=None, description="""Human-readable text describing the investigation in more detail.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: investigationDescription'],
         'domain_of': ['Investigation'],
         'slot_uri': 'dcterms:description'} })
    submission_date: Optional[str] = Field(default=None, description="""Date of submission of the dataset presently being described to a host repository (ISO 8601, optional time zone).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: submissionDate'],
         'domain_of': ['Investigation']} })
    public_release_date: Optional[str] = Field(default=None, description="""Date of first public release of the dataset presently being described (ISO 8601, optional time zone).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: publicReleaseDate'],
         'domain_of': ['Investigation']} })
    license: Optional[LicenseEnum] = Field(default=None, description="""License for the reuse of the data associated with this investigation. The Creative Commons licenses cover most use cases and are recommended.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: license'], 'domain_of': ['Investigation']} })
    miappe_version: str = Field(default=..., description="""The version of MIAPPE used.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: miappeVersion'],
         'domain_of': ['Investigation'],
         'examples': [{'value': '1.1'}]} })
    associated_publications: Optional[list[Publication]] = Field(default=None, description="""Publications where the investigation is described. Use of DOIs is recommended.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: associatedPublication'],
         'domain_of': ['Investigation']} })
    persons: Optional[list[Person]] = Field(default=None, description="""The people involved in this investigation or study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Investigation', 'Study']} })
    studies: list[Study] = Field(default=..., description="""The studies belonging to this investigation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Investigation']} })


class Study(ConfiguredBaseModel):
    """
    A study (or experiment) comprises a series of assays (or measurements) of one or more types, undertaken to answer a particular biological question. At least one study is expected per investigation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    study_id: str = Field(default=..., description="""Unique identifier comprising the name or identifier for the institution/database hosting the submission of the study data, and the identifier of the study in that institution.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: studyId'],
         'domain_of': ['Study'],
         'slot_uri': 'schema:identifier'} })
    study_title: str = Field(default=..., description="""Name, human-readable text summarising the study.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: studyTitle'],
         'domain_of': ['Study'],
         'slot_uri': 'dcterms:title'} })
    study_description: Optional[str] = Field(default=None, description="""Human-readable text describing the study.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: studyDescription'],
         'domain_of': ['Study'],
         'slot_uri': 'dcterms:description'} })
    study_start_date: str = Field(default=..., description="""Date and, if relevant, time when the experiment started.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: studyStartDate'], 'domain_of': ['Study']} })
    study_end_date: Optional[str] = Field(default=None, description="""Date and, if relevant, time when the experiment ended.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: studyEndDate'], 'domain_of': ['Study']} })
    contact_institution: str = Field(default=..., description="""Name and address of the institution responsible for the study.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: contactInst'], 'domain_of': ['Study']} })
    location_country: str = Field(default=..., description="""The country where the experiment took place, either as a full name or preferably as a 2-letter code (ISO 3166).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: locationCountry'],
         'domain_of': ['Study'],
         'examples': [{'value': 'FR'}]} })
    site_name: str = Field(default=..., description="""The name of the natural site, experimental field, greenhouse, phenotyping facility, etc. where the experiment took place.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: siteName'], 'domain_of': ['Study']} })
    location_latitude: Optional[float] = Field(default=None, description="""Latitude of the experimental site in degrees, in decimal format (ISO 6709).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: locationLatitude'], 'domain_of': ['Study']} })
    location_longitude: Optional[float] = Field(default=None, description="""Longitude of the experimental site in degrees, in decimal format (ISO 6709).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: locationLongitude'], 'domain_of': ['Study']} })
    location_altitude: Optional[str] = Field(default=None, description="""Altitude of the experimental site, provided in metres (m).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: locationAltitude'], 'domain_of': ['Study']} })
    experimental_design_description: str = Field(default=..., description="""Short description of the experimental design, possibly including statistical design.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: expeDesignDesc'], 'domain_of': ['Study']} })
    experimental_design_type: Optional[str] = Field(default=None, description="""Type of experimental design of the study, in the form of an accession number from the Crop Ontology (subclass of CO_715:0000003).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: expeDesignType'],
         'domain_of': ['Study'],
         'examples': [{'value': 'CO_715:0000145'}]} })
    observation_unit_level_hierarchy: Optional[str] = Field(default=None, description="""Hierarchy of the different levels of repetitions between each other.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: obsUnitLevelHierarchy'],
         'domain_of': ['Study'],
         'examples': [{'value': 'block>rep>plot'}]} })
    observation_unit_description: str = Field(default=..., description="""General description of the observation units in the study.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: obsUnitDesc'], 'domain_of': ['Study']} })
    growth_facility_description: str = Field(default=..., description="""Short description of the facility in which the study was carried out.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: growthFacilityDesc'], 'domain_of': ['Study']} })
    growth_facility_type: Optional[str] = Field(default=None, description="""Type of growth facility in which the study was carried out, in the form of an accession number from the Crop Ontology (subclass of CO_715:0000005).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: growthFacilityType'],
         'domain_of': ['Study'],
         'examples': [{'value': 'CO_715:0000162'}]} })
    cultural_practices: Optional[str] = Field(default=None, description="""General description of the cultural practices of the study.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: culturalPractice'], 'domain_of': ['Study']} })
    experimental_design_map: Optional[list[str]] = Field(default=None, description="""Representation of the experimental design (URL or file name).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: expeDesignMap'], 'domain_of': ['Study']} })
    persons: Optional[list[Person]] = Field(default=None, description="""The people involved in this investigation or study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Investigation', 'Study']} })
    data_files: Optional[list[DataFile]] = Field(default=None, description="""The data files associated with this study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    biological_materials: Optional[list[BiologicalMaterial]] = Field(default=None, description="""The biological materials studied in this study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    environment_parameters: Optional[list[EnvironmentParameter]] = Field(default=None, description="""The constant environment parameters of this study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    experimental_factors: Optional[list[ExperimentalFactor]] = Field(default=None, description="""The experimental factors varied in this study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    events: Optional[list[Event]] = Field(default=None, description="""The events occurring during this study or observation unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    observation_units: list[ObservationUnit] = Field(default=..., description="""The observation units of this study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    observed_variables: list[ObservedVariable] = Field(default=..., description="""The observed variables measured in this study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })


class Person(ConfiguredBaseModel):
    """
    A human involved in the investigation or specifically any of its studies. At least one person is expected per investigation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    person_name: str = Field(default=..., description="""The name of the person (either full name or as used in scientific publications).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: personName'],
         'domain_of': ['Person'],
         'slot_uri': 'schema:name'} })
    person_email: Optional[str] = Field(default=None, description="""The electronic mail address of the person.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: personEmail'],
         'domain_of': ['Person'],
         'slot_uri': 'schema:email'} })
    person_id: Optional[str] = Field(default=None, description="""An identifier for the data submitter. If that submitter is an individual, ORCID identifiers are recommended.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: personId'],
         'domain_of': ['Person'],
         'examples': [{'value': 'orcid.org/0000-0001-6494-0008'}]} })
    person_roles: list[str] = Field(default=..., description="""Type of contribution of the person to the investigation.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: personRole'],
         'domain_of': ['Person'],
         'examples': [{'value': 'corresponding author'}]} })
    person_affiliations: list[str] = Field(default=..., description="""The institution the person belongs to.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: personAffiliation'], 'domain_of': ['Person']} })

    @field_validator('person_email')
    def pattern_person_email(cls, v):
        pattern=re.compile(r"^\S+@[\S+\.]+\S+")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid person_email format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid person_email format: {v}"
            raise ValueError(err_msg)
        return v


class Publication(ConfiguredBaseModel):
    """
    A literature publication where the investigation is described. Use of DOIs is recommended.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    associated_publication: Optional[str] = Field(default=None, description="""An identifier for a literature publication where the investigation is described. Use of DOIs is recommended.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: associatedPublication'],
         'domain_of': ['Publication'],
         'examples': [{'value': 'doi:10.1371/journal.pone.0071377'}]} })


class DataFile(ConfiguredBaseModel):
    """
    A file or digital object holding observation data recorded during one or more assays of the study, typically in tabular form.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    data_file_link: str = Field(default=..., description="""Link to the data file (or digital object) in a public database or in a persistent institutional repository; or identifier of the data file when submitted together with the MIAPPE submission.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: dataFileLink'], 'domain_of': ['DataFile']} })
    data_file_description: str = Field(default=..., description="""Description of the format of the data file. May be a standard file format name, or a description of the organization of the data in a tabular file.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: dataFileDesc'], 'domain_of': ['DataFile']} })
    data_file_version: Optional[str] = Field(default=None, description="""The version of the dataset (the actual data).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: dataFileVersion'], 'domain_of': ['DataFile']} })


class EnvironmentParameter(ConfiguredBaseModel):
    """
    An environmental parameter that was kept constant throughout the study and did not change between observation units or assays.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    environment_parameter_name: str = Field(default=..., description="""Name of the environment parameter constant within the experiment (see MIAPPE Appendix I).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: envParam'],
         'domain_of': ['EnvironmentParameter'],
         'examples': [{'value': 'rooting medium composition'}]} })
    environment_parameter_value: str = Field(default=..., description="""Value of the environment parameter constant within the experiment.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: envParamValue'],
         'domain_of': ['EnvironmentParameter']} })


class ExperimentalFactor(ConfiguredBaseModel):
    """
    A condition that varies between observation units, which may be biotic (pest, disease interaction) or abiotic (treatment and cultural practice) in nature. The object of a study is to ascertain the impact of one or more factors on the biological material.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    experimental_factor_type: ExperimentalFactorTypeEnum = Field(default=..., description="""Name/acronym of the experimental factor (see MIAPPE Appendix II).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: expeFactorType'],
         'domain_of': ['ExperimentalFactor']} })
    experimental_factor_description: Optional[str] = Field(default=None, description="""Free text description of the experimental factor, including all relevant treatments planned for the plants targeted by a given factor.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: expeFactorDesc'],
         'domain_of': ['ExperimentalFactor']} })
    experimental_factor_values: Optional[list[str]] = Field(default=None, description="""List of possible values for the factor.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: expeFactorValues'],
         'domain_of': ['ExperimentalFactor'],
         'examples': [{'value': 'Watered'}, {'value': 'Unwatered'}]} })


class Event(ConfiguredBaseModel):
    """
    An event is a discrete occurrence at a particular time in the experiment (which can be natural, such as rain, or unnatural, such as planting, watering, etc).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    event_type: str = Field(default=..., description="""Short name of the event.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: eventType'],
         'domain_of': ['Event'],
         'examples': [{'value': 'Planting'}]} })
    event_accession_number: Optional[str] = Field(default=None, description="""Accession number of the event type in a suitable controlled vocabulary (Crop Ontology, subclass of CO_715:0000006).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: eventAccNumber'], 'domain_of': ['Event']} })
    event_description: Optional[str] = Field(default=None, description="""Description of the event, including details such as amount applied and possibly duration of the event.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: eventDesc'], 'domain_of': ['Event']} })
    event_dates: list[str] = Field(default=..., description="""Date and time of the event.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: eventDate'], 'domain_of': ['Event']} })


class ObservationUnit(ConfiguredBaseModel):
    """
    Observation units are objects that are subject to instances of observation and measurement. An observation unit comprises one or more plants, and/or their environment. (Synonym: Experimental unit)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    observation_unit_id: str = Field(default=..., description="""Identifier used to identify the observation unit in data files containing the values observed or measured on that unit. Must be locally unique.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: obsUnitId'], 'domain_of': ['ObservationUnit']} })
    observation_unit_type: ObservationUnitTypeEnum = Field(default=..., description="""Type of observation unit, usually one of: study, block, sub-block, plot, sub-plot, pot, plant.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: obsUnitType'], 'domain_of': ['ObservationUnit']} })
    observation_unit_external_ids: Optional[list[str]] = Field(default=None, description="""Identifier for the observation unit in a persistent repository. URIs are recommended when possible.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: externalId'], 'domain_of': ['ObservationUnit']} })
    spatial_distribution: Optional[list[str]] = Field(default=None, description="""Type and value of a spatial coordinate (georeference or relative) or level of observation, provided as a key-value pair of the form type:value.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: spatialDistribution'],
         'domain_of': ['ObservationUnit']} })
    observation_unit_factor_values: Optional[list[str]] = Field(default=None, description="""List of values for each factor applied to the observation unit.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: obsUnitFactorValue'],
         'domain_of': ['ObservationUnit']} })
    biological_material: Optional[list[str]] = Field(default=None, description="""Reference(s) (by biological_material_id) to the biological material(s) comprising this observation unit. The referenced materials are defined at the study level. An observation unit may reference zero or more biological materials (e.g. intercropping or mixed plots).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE checklist cardinality: Biological Material is 0+ per '
                      'observation unit'],
         'domain_of': ['ObservationUnit']} })
    samples: Optional[list[Sample]] = Field(default=None, description="""The samples taken from this observation unit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ObservationUnit']} })


class Sample(ConfiguredBaseModel):
    """
    A sample is a portion of plant tissue harvested, non-harvested or extracted from an observation unit for the purpose of sub-plant observations and/or molecular studies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    sample_id: str = Field(default=..., description="""Unique identifier for the sample.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: sampleId'], 'domain_of': ['Sample']} })
    development_stage: Optional[str] = Field(default=None, description="""The stage in the life of a plant structure during which the sample was taken (Plant Ontology, subclass of PO:0009012, or BBCH scale).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: developmentStage'], 'domain_of': ['Sample']} })
    anatomical_entity: str = Field(default=..., description="""A description of the plant part or plant product from which the sample was taken (Plant Ontology, subclass of PO:0025131).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: anatomicalEntity'], 'domain_of': ['Sample']} })
    sample_description: Optional[str] = Field(default=None, description="""Any information not captured by the other sample fields, including quantification, sample treatments and processing.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: sampleDesc'], 'domain_of': ['Sample']} })
    collection_date: str = Field(default=..., description="""The date and time when the sample was collected / harvested.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: collectionDate'], 'domain_of': ['Sample']} })
    sample_external_ids: Optional[list[str]] = Field(default=None, description="""An identifier for the sample in a persistent repository. URIs are recommended when possible.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: externalId'], 'domain_of': ['Sample']} })


class ObservedVariable(ConfiguredBaseModel):
    """
    An observed variable describes how a measurement has been made. It typically takes the form of a measured characteristic of the observation unit (plant or environmental trait), associated to the method and unit of measurement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    variable_id: str = Field(default=..., description="""Code used to identify the variable in the data file. A variable ID must be unique within a given investigation.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: variableId'], 'domain_of': ['ObservedVariable']} })
    variable_name: Optional[str] = Field(default=None, description="""Name of the variable.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: variableName'],
         'domain_of': ['ObservedVariable']} })
    variable_accession_number: Optional[str] = Field(default=None, description="""Accession number of the variable in the Crop Ontology.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: variableAccNumber'],
         'domain_of': ['ObservedVariable']} })
    trait: Optional[Trait] = Field(default=None, description="""The trait component of the observed variable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedVariable']} })
    method: Optional[Method] = Field(default=None, description="""The method component of the observed variable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedVariable']} })
    scale: Optional[Scale] = Field(default=None, description="""The scale component of the observed variable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ObservedVariable']} })


class Trait(ConfiguredBaseModel):
    """
    The (plant or environmental) trait under observation, optionally described by the entity it is measured on and its characteristic.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    trait_name: str = Field(default=..., description="""Name of the (plant or environmental) trait under observation.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: traitName'], 'domain_of': ['Trait']} })
    trait_entity: Optional[str] = Field(default=None, description="""Entity (part of the plant, whole plant, group of plants e.g. canopy) on which the trait has been measured.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: traitEntity'], 'domain_of': ['Trait']} })
    trait_entity_accession_number: Optional[str] = Field(default=None, description="""Accession number of the trait entity in a suitable controlled vocabulary (Plant Ontology).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: traitEntityAccessionNumber'],
         'domain_of': ['Trait']} })
    trait_characteristic: Optional[str] = Field(default=None, description="""Characteristic measured (e.g. size, volume, surface, concentration).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: traitCharacteristic'], 'domain_of': ['Trait']} })
    trait_characteristic_accession_number: Optional[str] = Field(default=None, description="""Accession number of the trait characteristic in a suitable controlled vocabulary (PATO).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: traitCharacteristicAccessionNumber'],
         'domain_of': ['Trait']} })
    trait_accession_number: Optional[str] = Field(default=None, description="""Accession number of the trait in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: traitAccNumber'], 'domain_of': ['Trait']} })


class Method(ConfiguredBaseModel):
    """
    The method of observation used to record an observed variable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    method_name: str = Field(default=..., description="""Name of the method of observation.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: methodName'], 'domain_of': ['Method']} })
    method_accession_number: Optional[str] = Field(default=None, description="""Accession number of the method in a suitable controlled vocabulary (Crop Ontology, Trait Ontology).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: methodAccNumber'], 'domain_of': ['Method']} })
    method_description: Optional[str] = Field(default=None, description="""Textual description of the method.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: methodDesc'], 'domain_of': ['Method']} })
    method_reference: Optional[str] = Field(default=None, description="""URI/DOI of reference describing the method.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: methodRef'], 'domain_of': ['Method']} })


class Scale(ConfiguredBaseModel):
    """
    The scale (unit of measurement) associated with an observed variable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml'})

    scale_name: str = Field(default=..., description="""Name of the scale associated with the variable.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: scaleName'], 'domain_of': ['Scale']} })
    scale_accession_number: Optional[str] = Field(default=None, description="""Accession number of the scale in a suitable controlled vocabulary.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: scaleAccNumber'], 'domain_of': ['Scale']} })
    time_scale: Optional[list[str]] = Field(default=None, description="""Name of the scale or unit of time with which observations of this type were recorded in the data file (for time series studies).""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: timeScale'], 'domain_of': ['Scale']} })


class GeoReferenced(ConfiguredBaseModel):
    """
    A mixin providing decimal geographic coordinates (latitude, longitude, altitude) plus a circular coordinate uncertainty, as used for in situ biological material and material sources in MIAPPE.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml', 'mixin': True})

    latitude: Optional[float] = Field(default=None, description="""Latitude in degrees, in decimal format (ISO 6709).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })
    longitude: Optional[float] = Field(default=None, description="""Longitude in degrees, in decimal format (ISO 6709).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })
    altitude: Optional[str] = Field(default=None, description="""Altitude provided in metres (m).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })
    coordinates_uncertainty: Optional[str] = Field(default=None, description="""Circular uncertainty of the coordinates, preferably in metres (m).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })


class BiologicalMaterial(GeoReferenced):
    """
    The biological material being studied (e.g. plants grown from a certain bag or seed, or plants grown in a particular field). The original source of that material is called the material source.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml',
         'mixins': ['GeoReferenced']})

    biological_material_id: str = Field(default=..., description="""Code used to identify the biological material in the data file. Should be unique within the Investigation.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: biologicalMaterialId'],
         'domain_of': ['BiologicalMaterial'],
         'examples': [{'value': 'INRA:W95115_inra_2001'}]} })
    biological_material_external_ids: Optional[list[str]] = Field(default=None, description="""One to many identifiers for the biological material. Can include EBI Biosamples ID. URIs are recommended when possible.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: biologicalMaterialExtId'],
         'domain_of': ['BiologicalMaterial']} })
    organism: str = Field(default=..., description="""An identifier for the organism at the species level. Use of the NCBI taxon ID is recommended.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: organism'],
         'domain_of': ['BiologicalMaterial'],
         'examples': [{'value': 'NCBITaxon:4577'}]} })
    genus: Optional[str] = Field(default=None, description="""Genus name for the organism under study, according to standard scientific nomenclature.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: genus'], 'domain_of': ['BiologicalMaterial']} })
    species: Optional[str] = Field(default=None, description="""Species name (formally: specific epithet) for the organism under study, according to standard scientific nomenclature.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: species'], 'domain_of': ['BiologicalMaterial']} })
    infraspecific_name: Optional[str] = Field(default=None, description="""Name of any subtaxa level, including variety, crossing name, etc., as a key-value pair list or MCPD-compliant format.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: infraspecificName'],
         'domain_of': ['BiologicalMaterial']} })
    biological_material_preprocessing: Optional[list[str]] = Field(default=None, description="""Description of any process or treatment applied uniformly to the biological material, prior to the study itself.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: biologicalMaterialPreprocessing'],
         'domain_of': ['BiologicalMaterial']} })
    material_source: Optional[MaterialSource] = Field(default=None, description="""The source of the biological material (germplasm/accession).""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiologicalMaterial']} })
    latitude: Optional[float] = Field(default=None, description="""Latitude in degrees, in decimal format (ISO 6709).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })
    longitude: Optional[float] = Field(default=None, description="""Longitude in degrees, in decimal format (ISO 6709).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })
    altitude: Optional[str] = Field(default=None, description="""Altitude provided in metres (m).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })
    coordinates_uncertainty: Optional[str] = Field(default=None, description="""Circular uncertainty of the coordinates, preferably in metres (m).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })


class MaterialSource(GeoReferenced):
    """
    An identifier for the source of the biological material (commonly called germplasm, accession, genotype or variety), together with any repository accession information and provenance.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/sierra-moxon/miappe-linkml',
         'mixins': ['GeoReferenced']})

    material_source_id: Optional[str] = Field(default=None, description="""An identifier for the source of the biological material, as a key-value pair comprising the repository name/identifier plus the accession number.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: materialSourceId'],
         'domain_of': ['MaterialSource']} })
    material_source_doi: Optional[str] = Field(default=None, description="""Digital Object Identifier (DOI) of the material source.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: materialSourceDoi'],
         'domain_of': ['MaterialSource']} })
    material_source_accession_number: Optional[str] = Field(default=None, description="""Unique identifier for accessions within a genebank. If material source is not from a genebank, use a laboratory ID.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: materialSourceAccNumber'],
         'domain_of': ['MaterialSource']} })
    material_source_accession_name: Optional[str] = Field(default=None, description="""Genebank accession registered name or other designation given to the material, or variety name.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: materialSourceAccName'],
         'domain_of': ['MaterialSource']} })
    material_source_institute_code: Optional[str] = Field(default=None, description="""FAO WIEWS code of the institute where the accession is maintained.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: materialSourceInstCode'],
         'domain_of': ['MaterialSource']} })
    material_source_institute_name: Optional[str] = Field(default=None, description="""Name of the material source institute.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: materialSourceInstName'],
         'domain_of': ['MaterialSource']} })
    material_source_other_ids: Optional[str] = Field(default=None, description="""Any other identifiers known to exist in other collections for this material source, as key:value pairs separated by semicolons.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: materialSourceOtherIds'],
         'domain_of': ['MaterialSource']} })
    material_source_description: Optional[str] = Field(default=None, description="""Description of the material source.""", json_schema_extra = { "linkml_meta": {'comments': ['MIAPPE codename: materialSourceDesc'],
         'domain_of': ['MaterialSource']} })
    latitude: Optional[float] = Field(default=None, description="""Latitude in degrees, in decimal format (ISO 6709).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })
    longitude: Optional[float] = Field(default=None, description="""Longitude in degrees, in decimal format (ISO 6709).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })
    altitude: Optional[str] = Field(default=None, description="""Altitude provided in metres (m).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })
    coordinates_uncertainty: Optional[str] = Field(default=None, description="""Circular uncertainty of the coordinates, preferably in metres (m).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GeoReferenced']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Investigation.model_rebuild()
Study.model_rebuild()
Person.model_rebuild()
Publication.model_rebuild()
DataFile.model_rebuild()
EnvironmentParameter.model_rebuild()
ExperimentalFactor.model_rebuild()
Event.model_rebuild()
ObservationUnit.model_rebuild()
Sample.model_rebuild()
ObservedVariable.model_rebuild()
Trait.model_rebuild()
Method.model_rebuild()
Scale.model_rebuild()
GeoReferenced.model_rebuild()
BiologicalMaterial.model_rebuild()
MaterialSource.model_rebuild()
