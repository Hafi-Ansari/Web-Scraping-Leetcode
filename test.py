from description import get_problem_description

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


description, examples, constraints = parse_problem_description(get_problem_description('https://leetcode.com/problems/two-sum/'))

print("DESCRIPTION-------------:")
print(description)

print("EXAMPLES--------------:")
for example in examples:
    print(example)

print("CONSTRAINTS------------:")
print(constraints)
