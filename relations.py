import math
import data

# the Python code implements the method for calculating phi coefficient
# described in the following link:
# https://www.statisticshowto.com/phi-coefficient-mean-square-contingency-coefficient/


def add_results(table):
    a = table["a"]
    b = table["b"]
    c = table["c"]
    d = table["d"]

    numerator = a * d - b * c
    denominator = math.sqrt(
        (a + b) * (c + d) * (a + c) * (b + d)
    )

    if numerator is not 0:
        r = numerator / denominator
    else:
        r = "NA"

    table["result"] = r


data_tables = data.get_json_data()

for table in data_tables:
    add_results(table)

data.write_result_table(data_tables)
