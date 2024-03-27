import argparse
import json

def convert_md_to_json(filename):
    # Open the file and read the lines
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Initialize the JSON object and temporary variables
    json_object = {}
    current_section = None
    current_content = []

    # Iterate over the lines
    for line in lines:
        # If the line starts with '##', it's a new section
        if line.startswith('##'):
            # If there's a current section, add it to the JSON object
            if current_section is not None:
                json_object[current_section] = ' '.join(current_content).strip()
            # Start a new section and clear the content
            current_section = line.strip('# ').strip()
            current_content = []
        else:
            # Otherwise, add the line to the current content
            current_content.append(line.strip())

    # Add the last section to the JSON object
    if current_section is not None:
        json_object[current_section] = ' '.join(current_content).strip()

    # Return the JSON object
    return json_object

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Convert a Markdown file to a JSON object")

    # Add the arguments
    parser.add_argument('filename', type=str, help="The name of the Markdown file to convert")

    # Parse the arguments
    args = parser.parse_args()

    # Use the function
    json_object = convert_md_to_json(args.filename)
    print(json.dumps(json_object, indent=4))

if __name__ == "__main__":
    main()