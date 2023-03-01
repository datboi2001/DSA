"""
This class is used to search for data in a list of dictionaries. Given a list of dictionaries and a query,
the class will return a list of dictionaries that match the query. The list can be really big,
so we want to make sure that the search is efficient.
"""
# Main idea: Use a trie to store the data.
# The trie will be a dictionary of dictionaries.
# The keys of the outer dictionary are the first letters of the words.
# The keys of the inner dictionaries are the second letters of the words.
# The values of the inner dictionaries are the third letters of the words.
# The values of the outer dictionary are the data that we want to return.
# For example, if we have the following data:
# 
# data = [
#     {"name": "John", "age": 20},
#     {"name": "Jane", "age": 21},
#     {"name": "Jack", "age": 22},
#     {"name": "Jill", "age": 23},
#     {"name": "Joe", "age": 24},
# ]





class DataSearch:
    def __init__(self, sources: list[dict[str, int | str]]):
        self.sources = sources
        self.trie = {}


    def suggest(self, query: str) -> list[dict[str | int | str]]:
        # Main idea: Use a trie to store the data. 
        query = query.lower()[1:]