from cohortextractor import StudyDefinition,\
     patients,\
     codelist,\
     codelist_from_csv,\
     filter_codes_by_category,\
     combine_codelists


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

)
