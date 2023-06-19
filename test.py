import json
import html
from boilerplate import get_boilerplate_code
from description import get_problem_description

def parse_problem_description(problem_description):
    sections = problem_description.split("\n")
    constraints_idx = next((i for i, string in enumerate(sections) if 'Constraints:' in string), None)
    description = "\n".join(sections[:constraints_idx]).strip()
    constraints = "\n".join(sections[constraints_idx+1:]).strip()
    examples = process_problem_description("\n".join(sections[:constraints_idx]))
    return description, examples, constraints

def process_problem_description(description):
    parts = description.split("\n")
    examples = []
    example = []
    for part in parts:
        if part.startswith("Example"):
            if example:
                examples.append("\n".join(example))
            example = [part]
        else:
            example.append(part)
    if example:
        examples.append("\n".join(example))
    return examples

def parse_example(example):
    example_lines = example.strip().split("\n")
    example_lines = [line.strip() for line in example_lines if line.strip()]
    inputs = []
    outputs = []
    for idx, line in enumerate(example_lines):
        if "Input:" in line:
            inputs.append(line.replace("Input: ", "").strip())
            outputs.append(
                example_lines[idx+1].replace("Output: ", "").strip())
    return {"inputs": inputs, "outputs": outputs} if inputs and outputs else None

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
    test_cases = [tc for tc in test_cases if tc is not None]  # Exclude None from the list
    question = {
        "id": idx,
        "title": link.split("/")[-2].replace("-", " ").title(),
        "description": html.escape(description),
        "examples": example_sections,
        "constraints": constraints,
        "code": html.escape(boilerplate_code),
        "test_cases": test_cases
    }
    question_data.append(question)

# Write the question data to a JSON file
with open('questions.json', 'w') as json_file:
    json.dump(question_data, json_file, indent=2)
