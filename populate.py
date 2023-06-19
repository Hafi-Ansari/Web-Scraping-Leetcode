import json
import html
from boilerplate import get_boilerplate_code
from description import get_problem_description
from clean import clean_questions
import ast
import re
from typing import List, Dict, Union, Any


def parse_problem_description(problem_description):
    sections = problem_description.split("\n")
    constraints_idx = next((i for i, string in enumerate(
        sections) if 'Constraints:' in string), None)
    examples_idx = next((i for i, string in enumerate(
        sections) if 'Example' in string), None)
    description = "\n".join(sections[:examples_idx]).strip()
    examples = process_problem_description("\n".join(sections[examples_idx:constraints_idx]))
    constraints = "\n".join(sections[constraints_idx+1:]).strip()
    return description, examples, constraints

def process_problem_description(description):
    parts = description.split("Example")
    examples = ["Example" + ex for ex in parts[1:]]
    return examples


def parse_example(example):
    example_lines = example.strip().split("\n")
    example_lines = [line.strip() for line in example_lines if line.strip()]
    inputs = {}
    outputs = []
    for idx, line in enumerate(example_lines):
        if "Input:" in line:
            input_str = line.replace("Input: ", "").strip()
            # Regex pattern that doesn't match commas inside brackets
            input_strs = re.split(',(?![^[]*])', input_str)
            for input_pair in input_strs:
                try:
                    key, value_str = input_pair.split('=')
                    # try parsing as a Python literal (list, dict, etc)
                    try:
                        value = ast.literal_eval(value_str.strip())
                    except (ValueError, SyntaxError):
                        # if that fails, remove leading/trailing quotes and handle as a string
                        value = value_str.strip()[1:-1] if value_str.strip().startswith(
                            '"') and value_str.strip().endswith('"') else value_str.strip()
                    inputs[key.strip()] = value
                except ValueError:
                    inputs[input_pair.strip()] = None
            output_str = example_lines[idx+1].replace("Output: ", "").strip()
            try:
                output_data = ast.literal_eval(output_str)
                # This part has been modified
                outputs = output_data
            except (ValueError, SyntaxError):
                outputs = output_str
    return {"inputs": inputs, "expectedOutput": outputs} if inputs and outputs else None


# Read the links from leetcode.txt
with open('leetcode.txt', 'r') as file:
    links = file.read().splitlines()

# Define an empty list to store the question data
question_data = []

# Loop through each link and scrape the data
for idx, link in enumerate(links, start=1):
    problem_description = get_problem_description(link)
    boilerplate_code = get_boilerplate_code(link)
    description, example_sections, constraints = parse_problem_description(
        problem_description)
    test_cases = [parse_example(example) for example in example_sections]
    # Exclude None from the list
    test_cases = [tc for tc in test_cases if tc is not None]
    question = {
        "id": idx,
        "title": link.split("/")[-2].replace("-", " ").title(),
        "description": html.escape(description),
        "examples": example_sections,
        "constraints": constraints,
        "code": html.escape(boilerplate_code),
        "testCases": test_cases
    }
    question_data.append(question)

# Write the question data to a JSON file
with open('questions.json', 'w') as json_file:
    json.dump(question_data, json_file, indent=2)

clean_questions()
