from sklearn.metrics import matthews_corrcoef
import data
import utils

# reuses functionality from one of our archived repos:
# https://github.com/rest-api-antipattern-inspector/relation-stats

# source about phi coefficient
# https://www.statisticshowto.com/phi-coefficient-mean-square-contingency-coefficient/

# documentation for this method
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html

endpoints_data = data.get_endpoints_data()

relevant = []

def stats(type_a, type_b):  # type_a & type_b: (anti)pattern types
    for a_key in endpoints_data[type_a].keys():
        y_true_list = endpoints_data[type_a][a_key]

        for b_key in endpoints_data[type_b].keys():
            y_pred_list = endpoints_data[type_b][b_key]

            # TODO also if all 1
            if (utils.all_equal(y_true_list) or utils.all_equal(y_pred_list)):
                print(a_key, "vs", b_key, "NA")
            else:
                result = matthews_corrcoef(y_true_list, y_pred_list)
                print(a_key, "vs", b_key, result)

                if (result >= 0.2 or result <= -0.2):
                    #
                    data = {
                        "category": type_a + " vs " + type_b,
                        "qualities": a_key + " vs " + b_key,
                        "result": result
                    }

                    relevant.append(data)

stats("linguisticPatterns", "designAntipatterns")

stats("linguisticPatterns", "designPatterns")

stats("designPatterns", "linguisticAntipatterns")

stats("linguisticAntipatterns", "designAntipatterns")

data.write_json("relevant_results.json", relevant)
