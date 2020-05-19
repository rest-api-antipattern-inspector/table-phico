import math
import data


def print_relation(table):
    a = table["a"]
    b = table["b"]
    c = table["c"]
    d = table["d"]

    # https://www.statisticshowto.com/phi-coefficient-mean-square-contingency-coefficient/

    numerator = a * d - b * c
    denominator = math.sqrt(
        (a + b) * (c + d) * (a + c) * (b + d)
    )

    if numerator is not 0:
        r = numerator / denominator
    else:
        r = "NA"

    print(table["keyOne"], "&", table["keyTwo"], ":", r)


data_tables = data.get_json_data()

for table in data_tables:
    print_relation(table)
