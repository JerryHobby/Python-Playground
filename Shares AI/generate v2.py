import os
import json

##############################################################

data_dir = './Shares AI/SHARES kb/'

# Define the output file for the JSONL data
output_file = data_dir + 'SHARES_training.jsonl'

# Define the input directories containing the markdown files

directories = [
    data_dir + 'shares commands',
    data_dir + 'shares definitions',
    data_dir + 'shares procedures',
    ]

# Define the prefix of files to ignore

ignore_file_prefix = '0000'

##############################################################

def collect_files(directories, ignore_file_prefix):
    """
    Collect all markdown files from the specified directories
    Append the folder name to the file name
    Skip files starting with the ignore_file_prefix
    """

    files = []
    for directory in directories:
        dir_contents = os.listdir(directory)
        for f in dir_contents:
            if f.endswith('.md') and not f.startswith(ignore_file_prefix):
                files.append(os.path.join(directory, f))
    return files


def parse_file(file):
    """
    Parse the prompts, keywords, and completions from one markdown file
    returns array of prompts and the completion text (used with each prompt)
    """
    prompt_prefix = "PROMPT:"
    keyword_prefix = "KEYWORDS:"
    completion_prefix = "COMPLETION:"

    prompts = []
    completion = ""
    keywords = []

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header = True;
    for line in lines:
        # parse header fields
        if line.startswith(prompt_prefix):
            prompts.append(line.strip(prompt_prefix).strip("\n").strip(' '))

        elif line.startswith(keyword_prefix):
            keywords = line.strip(keyword_prefix).strip("\n").strip(' ').split(',')
            
        elif line.startswith(completion_prefix):
            header = False

        # parse completion
        elif not header:
            completion += line

    if header:
        return None, None

    completion += "\n\n#### keywords: "
    for keyword in keywords:
        completion += f"{keyword.strip(' ')}, "

    completion = completion.strip(' ').strip(',')
    return prompts, completion


def create_jsonl_data(prompts, completion):
    """
    Create a JSONL data object
    """
    data = []

    for prompt in prompts:
        print("\t\tPrompt:", prompt)
        json_obj = {
            'prompt': prompt,
            'completion': completion
        }
        data.append(json_obj)

    return data


def write_jsonl_data(data):
    """
    Write the data to a JSONL file
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in data:
            json.dump(entry, f)
            f.write('\n')


def main():
    # Initialize an empty list to hold data
    json_data = []

    # Process each directory to get all valid file names
    files = collect_files(directories, ignore_file_prefix)
    #print(*files, sep="\n")

    # Process each file
    for file in files:
        print("Processing file:", file)

        prompts, completion = parse_file(file)
        if prompts is None:
            print("Error: No prompt found in file", file)
            continue

        file_json = create_jsonl_data(prompts, completion)
        json_data.extend(file_json)

    write_jsonl_data(json_data)



if __name__ == "__main__":
    main()