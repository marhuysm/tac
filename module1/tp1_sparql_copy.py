"""Query Wikidata for Belgian politicians"""

import argparse

from SPARQLWrapper import SPARQLWrapper, JSON

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filter', type=str, help='Filtering on name')
parser.add_argument('-n', '--number', type=int, help='Number of rows to display')

def get_rows():
    """Retrieve results from SPARQL"""
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    sparql = SPARQLWrapper(endpoint)

    statement = """
        SELECT ?street ?streetLabel ?placeLabel ?coords
        WHERE
        {
        ?street wdt:P31/wdt:P279* wd:Q79007 .
        ?street wdt:P131 ?place .
        ?place wdt:P131 wd:Q90870 .
        ?street wdt:P625 ?coords .
        SERVICE wikibase:label { bd:serviceParam wikibase:language "fr" . }
        } 

        ORDER BY ?placeLabel ?streetLabel
    """

    sparql.setQuery(statement)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    rows = results['results']['bindings']
    print(f"\n{len(rows)} Brussels streets found\n")
    return rows

def show(rows, name_filter=None, n=10):
    """Display n streets (default=10)"""
    if name_filter:
        rows = [row for row in rows if name_filter in row['streetLabel']['value'].lower()]
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        try:
            streetLabel = row['streetLabel']['value']
        except ValueError:
            streetLabel = "????"
        try:
            municipality = row['placeLabel']['value']
        except ValueError: # unknown municipality
            municipality = "????"
        try:
            coordinates = row['coords']['value']
        except ValueError: # unknown coords
            municipality = "????"
        print(f"{streetLabel} - {municipality} - {coordinates} - {row['street']['value']}")

if __name__ == "__main__":
    args = parser.parse_args()
    my_rows = get_rows()
    my_filter = args.filter if args.filter else None
    number = args.number if args.number else 10
    show(my_rows, my_filter, number)
