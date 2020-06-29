# reuses function from one of our archived repos:
# https://github.com/rest-api-antipattern-inspector/relation-stats

def all_equal(binary_list):
    return len(set(binary_list)) <= 1
