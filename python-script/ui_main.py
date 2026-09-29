import sys
from run_sparql import ExecuteQuery


# user inputs
inp = input("Enter the model name: ")

try:
    qnty = int(input("How many SPARQL queries do you want to execute? "))
except ValueError:
    sys.exit("Invalid number of queries. Application terminated.")

if qnty <= 0:
    sys.exit("Number of queries must be greater than 0. Application terminated.")


# execution method
if qnty == 1:
    method = "i"
else:
    method = input(
        "\nDo you want to execute the queries individually or in batch?\n"
        "Enter 'i' for Individual\n"
        "Enter 'b' for Batch\n"
        "Enter 'x' for Exit\n"
        "Your choice: "
    ).lower()

    if method == "x":
        sys.exit("Application terminated.")

    if method not in ("i", "b"):
        sys.exit("Invalid choice. Application terminated.")



queries = [] # query(ies)

# collection queries and purposes
for i in range(qnty):
    print(f"\n--- Enter information for query {i + 1} of {qnty} ---")

    sparql_file_name = input(
        f"Enter the name of #{i + 1} SPARQL file: "
    )

    sparql_purpose = input(
        f"Enter the purpose for #{i + 1} query: "
    )
    query = {
        "file": sparql_file_name,
        "purpose": sparql_purpose
    }
    queries.append(query)

    if method == "i":

        for count, query in enumerate(queries, start=1):
            print(
                f"\n--- Executing query {count} of {qnty} "
                f"using file: {query['file']} ---"
            )

            query_runner = ExecuteQuery(
                model=inp,
                file=query["file"],
                purpose=query["purpose"]
            )

            query_runner.run_research_query()
# queries batch execution
if method == "b":
    print("\n========================================")
    print("Starting batch execution")
    print("========================================")

    for i, query in enumerate(queries, start=1):

        print(
            f"\n--- Executing query {i} of {qnty} "
            f"using file: {query['file']} ---"
        )

        query_runner = ExecuteQuery(
            model=inp,
            file=query["file"],
            purpose=query["purpose"]
        )

        query_runner.run_research_query()
else:
    sys.exit("Application ends!!!")