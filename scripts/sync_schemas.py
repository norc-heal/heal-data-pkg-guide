import requests
from pathlib import Path
import pprint
import subprocess
import argparse
import re

def copy_schemas(
    fork,
    branch,
    input_json_docspath,
    input_csv_docspath,
    output_json_docspath,
    output_csv_docspath,
):
    jsonmd_url = (
        f"https://raw.githubusercontent.com/{fork}/healdata-utils/{branch}/"
        f"{input_json_docspath}"
    )
    csvmd_url = (
        f"https://raw.githubusercontent.com/{fork}/healdata-utils/{branch}/"
        f"{input_csv_docspath}"
    )
    jsonmd = requests.get(jsonmd_url).text
    csvmd = requests.get(csvmd_url).text

    Path(output_json_docspath).write_text(str(jsonmd))
    Path(output_csv_docspath).write_text(str(csvmd))

    updated_mkdocs = re.sub(
        "- Data Dictionary:.*\n",
        f"- Data Dictionary: {output_csv_docspath.replace('docs/','')}\n",
        Path("mkdocs.yaml").read_text())
    
    Path("mkdocs.yaml").write_text(updated_mkdocs)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Copies and formats the HEAL" " vlmd fricitonless and jsonschema schemas "
        )
    )
    # Add arguments
    parser.add_argument(
        "-b",
        "--branch",
        type=str,
        default="pr-integration",
        help=("The branch name or commit hash from heal-metadata-schemas"),
    )
    parser.add_argument(
        "-f",
        "--fork",
        type=str,
        help="Name of the fork (default is HEAL)",
        default="norc-heal",
    )

    input_csv_docspath = "docs/vlmd/schemas/csv-fields.md"
    input_json_docspath = "docs/vlmd/schemas/json-data-dictionary.md"

    output_csv_docspath = "docs/schemas/csv-data-dictionary-fields.md"
    output_json_docspath = "docs/schemas/json-data-dictionary.md"

    parser.add_argument(
        "-ic",
        "--input-csv-docspath",
        type=str,
        help="Name of the relative path to the csv version of the documentation",
        default=input_csv_docspath,
    )
    parser.add_argument(
        "-ij",
        "--input-json-docspath",
        type=str,
        help="Name of the relative path to the json version of the documentation",
        default=input_json_docspath,
    )
    parser.add_argument(
        "-oc",
        "--output-csv-docspath",
        type=str,
        help="Name of the output relative path to the csv version of the documentation",
        default=output_csv_docspath,
    )
    parser.add_argument(
        "-oj",
        "--output-json-docspath",
        type=str,
        help="Name of the ouput relative path to the json version of the documentation",
        default=output_json_docspath,
    )

    args = parser.parse_args()
    copy_schemas(
        args.fork,
        args.branch,
        args.input_json_docspath,
        args.input_csv_docspath,
        args.output_json_docspath,
        args.output_csv_docspath,
    )
