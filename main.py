import pandas as pd
import json


def excel_to_json(excel_file_path, json_file_path):
    # Read the Excel file
    df = pd.read_excel(excel_file_path)

    # Convert the DataFrame to a list of dictionaries
    records = df.to_dict(orient='records')

    # Convert the list of dictionaries to a JSON string
    json_str = json.dumps(records, indent=4)

    # Write the JSON string to a file
    with open(json_file_path, 'w') as file:
        file.write(json_str)


if __name__ == "__main__":
    excel_input_file_path = "/path/to/your/file.xlsx"
    json_output_file_path = "/path/to/your/output/file.json"
    excel_to_json(excel_file_path=excel_input_file_path, json_file_path=json_output_file_path)
