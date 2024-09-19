import os
import json

# Define the output file for the JSONL data
output_file = './SHARES_training.jsonl'

# Define the directories containing the markdown files
directories = [
    './SHARES kb/shares commands/',
    './SHARES kb/shares definitions/',
    './SHARES kb/shares procedures/',
    ]

ignore_file_prefix = '0000'


##############################################################
# Initialize an empty list to hold data
data = []

for directory in directories:
    print("Processing folder:", directory)

    prompt_files = sorted([f for f in os.listdir(directory) if f.endswith('.md')])

    for prompt_file in prompt_files:

        if prompt_file.startswith(ignore_file_prefix):
            print("\tSkipping:", prompt_file)
            continue

        print("\tProcessing:", prompt_file)

        prompt_path = os.path.join(directory, prompt_file)

        with open(prompt_path, 'r', encoding='utf-8') as f:
            prompts = []
            completion = ""
            keywords = []

            header = True;
            lines = f.readlines()
            for line in lines:
                # parse header fields
                if line.startswith('PROMPT:'):
                    prompts.append(line.strip("PROMPT:").strip("\n").strip(' '))
                elif line.startswith('KEYWORDS:'):
                    keywords = line.strip("KEYWORDS:").strip("\n").strip(' ').split(',')
                elif line.startswith('COMPLETION:'):
                    header = False

                # parse completion
                elif not header:
                    completion += line

            completion += "\n\n#### keywords: "
            for keyword in keywords:
                completion += f"{keyword.strip(' ')}, "

            completion = completion.strip(' ').strip(',')

            # error checking
            if len(prompts) == 0:
                print(f"Error: No prompt found in file {prompt_file}")
                continue
            if len(completion) == 0:
                print(f"Error: No completion found in file {prompt_file}")
                continue
            if len(keywords) == 0:
                print(f"Error: No keywords found in file {prompt_file}")
                continue

            for prompt in prompts:
                # Create a JSON object
                json_obj = {
                    'prompt': prompt,
                    'completion': completion
                }

                data.append(json_obj)
                # print(json_obj)

# Write the data to a JSONL file
with open(output_file, 'w', encoding='utf-8') as f:
    for entry in data:
        json.dump(entry, f)
        f.write('\n')

print(f"JSONL file '{output_file}' has been created successfully.")
