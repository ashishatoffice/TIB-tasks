import os
import rdflib

class ExecuteQuery():
    def __init__(self, model: str,  **kwargs):
        self.model = model
        self.sparql_file = kwargs.get('file')
        self.purpose = kwargs.get('purpose')
    def run_research_query(self):
        # the RDF Graph
        g = rdflib.Graph()

        # parsing the Turtle file
        g.parse(
            os.path.join("..", "vivo-task/ontology/", self.model),
            format="turtle"
        )

        # loading the sparql file
        sparql_file = os.path.join("..", "vivo-task/sparql/", self.sparql_file)

        with open(sparql_file, "r") as query:
            sparql_query = query.read()

        # execute the query

        results = g.query(sparql_query)

        # variables returned by RDFLib
        output_variables = [str(var) for var in results.vars]

        print("-" * (5 + len(f"-- Query Results for the {self.purpose}------")))
        print(f"   --- Query Results for the {self.purpose}------")
        print("-" * (5 + len(f"-- Query Results for the {self.purpose}------")))
        for row in results:
            for variable in output_variables:
               value = getattr(row, variable, None)
               print(f"{variable}: {value}")

            print("-" * 60)



