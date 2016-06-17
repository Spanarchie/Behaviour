
def getPayload4matchrule():
    json_Payloads = {
        "US Diabetes":{
            "age": 55,
            "country_code": "US",
            "concept_id": "mesh:M0447381",
            "distance": 10,
            "geo": {
                "latitude": 40.7128,
                "longitude": 74.0059
            },
            "location": "New York, New York, United States",
            "gender": "Both",
            "containing_term": "Type 2 Diabetes"
        },

        "non-US Diabetes":{
            "age": 55,
            "country_code": "US",
            "concept_id": "mesh:M0447381",
            "distance": 10,
            "geo": {
                "latitude": 40.7128,
                "longitude": 74.0059
            },
            "location": "New York, New York, United States",
            "gender": "Both",
            "containing_term": "Type 2 Diabetes"
        },

        "US non-Diabetes":{
            "age": 55,
            "country_code": "US",
            "concept_id": "mesh:M0447384",
            "distance": 10,
            "geo": {
                "latitude": 40.7128,
                "longitude": 74.0059
            },
            "location": "New York, New York, United States",
            "gender": "Both",
            "containing_term": "Type 2 Diabetes"
        }
    };