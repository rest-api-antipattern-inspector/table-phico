import json


def get_json_data():
    with open("full-data.json", "r") as read_file:
        return json.load(read_file)


# reuses function from one of our archived repos,
# this one: https://github.com/rest-api-antipattern-inspector/relation-stats
def get_endpoints_data():
    json_data = get_json_data()

    data = {
        "linguisticAntipatterns": {
            "AmorphousURI": [],
            "CRUDyURI": [],
            "ContextlessResource": [],
            "NonHierarchicalNodes": [],
            "PluralisedNodes": []
        },
        "designAntipatterns": {
            "isBreakingSelfDescriptiveness": [],
            "isForgettingHypermedia": [],
            "isIgnoringCaching": [],
            "isIgnoringMIMEType": [],
            "isIgnoringStatusCode": [],
            "isMisusingCookies": []
        },
        "linguisticPatterns": {
            "TidyURI": [],
            "VerblessURI": [],
            "ContextualisedResource": [],
            "HierarchicalNodes": [],
            "patternSingularisedPluralisedNodes": []
        },
        "designPatterns": {
            "EntityLinking": [],
            "ResponseCaching": [],
            "ContentNegotiation": []
        }
    }

    for endpoint in json_data:
        for lAKey in data["linguisticAntipatterns"].keys():
            lABinary = 1 if endpoint["linguisticAntipatterns"][lAKey] else 0
            data["linguisticAntipatterns"][lAKey].append(lABinary)

        for lPKey in data["linguisticPatterns"].keys():
            lPBinary = 1 if endpoint["linguisticPatterns"][lPKey] else 0
            data["linguisticPatterns"][lPKey].append(lPBinary)

        for dAKey in data["designAntipatterns"].keys():
            dABinary = 1 if endpoint["designAntipatterns"][dAKey] else 0
            data["designAntipatterns"][dAKey].append(dABinary)

        for dPKey in data["designPatterns"].keys():
            dPBinary = 1 if endpoint["designPatterns"][dPKey] else 0
            data["designPatterns"][dPKey].append(dPBinary)

    return data
