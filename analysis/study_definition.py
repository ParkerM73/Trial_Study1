from cohortextractor import StudyDefinition,\
     patients,\
     codelist,\
     codelist_from_csv,\
     filter_codes_by_category,\
     combine_codelists

#Import codelists
chronic_cardiac_disease_codes = codelist_from_csv(
    "codelists/opensafely-chronic-cardiac-disease.csv", system="ctv3", column="CTV3ID"
)


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    population=patients.registered_with_one_practice_between( #Line 10 means "I'm interested in all patients who have never changed practice, between these two dates";
        "2019-02-01", "2020-02-01"

    ),
    age=patients.age_as_of( # lines 14-15 "Give me a column of data corresponding to the age of each patient on the given date"; 
        "2019-09-01",
        return_expectations={
            "rate": "universal", #and lines 16-18 "I expect every patient to have a value, and the distribution of ages to match that of the real UK populatio
            "int": {"distribution": "population_ages"},
        },
    ),

    # https://github.com/opensafely/risk-factors-research/issues/46
    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {1: 0.49, 2: 0.51}},
        }
    ),

        chronic_cardiac_disease=patients.with_these_clinical_events(
        chronic_cardiac_disease_codes,
        returning="date",
        find_first_match_in_period=True,
        include_month=True,
        return_expectations={"incidence": 0.2},
    ),



    

)
