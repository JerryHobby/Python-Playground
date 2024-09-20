import os
import json
import sharesdoc as sd

def collect_files(directories, ignore_prefix):
    """
    Collect all markdown files from the specified directories.
    Skip files starting with the ignore_file_prefix.
    """
    files = []
    for directory in directories:
        dir_contents = os.listdir(directory)
        for f in dir_contents:
            if f.endswith('.md') and not f.startswith(ignore_prefix):
                files.append(os.path.join(directory, f))
    return files

def parse_file(file):
    """
    Parse the prompts, keywords, and completions from one markdown file.
    Returns an instance of SharesDoc.
    """
    prompt_prefix = "PROMPT:"
    keyword_prefix = "KEYWORDS:"
    completion_prefix = "COMPLETION:"

    prompts = []
    completion = ""
    keywords = []

    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    header = True
    for line in lines:
        # parse header fields
        if line.startswith(prompt_prefix):
            prompts.append(line.strip(prompt_prefix).strip("\n").strip(' '))

        elif line.startswith(keyword_prefix):
            keywords = [keyword.strip() for keyword in line.strip(keyword_prefix).strip("\n").strip(' ').split(',')]

        elif line.startswith(completion_prefix):
            header = False

        # parse completion
        elif not header:
            completion += line

    if header:
        return None

    completion += "\n\n#### keywords: "
    for keyword in keywords:
        completion += f"{keyword.strip(' ')}, "

    completion = completion.strip(' ').strip(',')
    return sd.SharesDoc(file, prompts, completion, keywords)

def write_jsonl_data(output_file, data):
    """
    Write the data to a JSONL file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in data:
            json.dump(entry, f)
            f.write('\n')
