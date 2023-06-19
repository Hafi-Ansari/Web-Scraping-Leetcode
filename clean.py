import json

def clean_questions():
    # Load the data
    with open('questions.json', 'r') as f:
        data = json.load(f)

    # Initialize a list to store cleaned data
    cleaned_data = []

    # Iterate over each question
    for question in data:
        # Replace Unicode non-breaking spaces with regular spaces in 'description' and 'examples'
        question['description'] = question['description'].replace('\u00a0', ' ')
        question['examples'] = [example.replace('\u00a0', ' ') for example in question['examples']]

        # Remove newline characters from 'description' and 'examples'
        question['description'] = question['description'].replace('\n', ' ')
        question['examples'] = [example.replace('\n', ' ') for example in question['examples']]

        # Split 'constraints' into an array
        question['constraints'] = question['constraints'].split('\n')

        # Add the cleaned question to the list
        cleaned_data.append(question)

    # Overwrite the existing data with the cleaned data
    with open('questions.json', 'w') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)
