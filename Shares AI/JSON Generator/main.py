import sharestraining as st
import fileutils as futil

# Define the input directories containing the markdown files
data_dir = './SHARES kb/'

md_directories = [
    data_dir + 'shares commands',
    data_dir + 'shares definitions',
    data_dir + 'shares procedures',
]

# Define the prefix of files to ignore
ignore_file_prefix = '0000'

# Define the keywords to include and exclude from the training data
# only searches the keywords in the keywords section of the markdown file
# if include_keywords is None, all documents are included
# if exclude_keywords is None, no documents are excluded

include_keywords = []
exclude_keywords = ['template']

# Define the output file for the JSONL data
output_file = data_dir + 'SHARES_training.jsonl'

######################################################################
# Main function
######################################################################

def main():
    # Initialize the SharesTraining instance
    training_data = st.SharesTraining()

    # Process each directory to get all valid file names
    files = futil.collect_files(md_directories, ignore_file_prefix)

    # Process each file
    for file in files:
        print("Processing file:", file)
        doc = futil.parse_file(file)
        if doc is None:
            print("Error: No prompt found in file", file)
            continue
        training_data.add_doc(doc)

    # Apply the include and exclude keyword filters
    filtered_jsonl = training_data.jsonl(include=include_keywords, exclude=exclude_keywords)

    # Write the JSONL data to the output file
    futil.write_jsonl_data(output_file, filtered_jsonl)

if __name__ == "__main__":
    main()