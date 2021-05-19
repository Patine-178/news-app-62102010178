import json

def read_loan_json():
    open_json_file = open('loan_data.json', 'r')
    read_json_file = open_json_file.read()

    loan_data = json.loads(read_json_file)

    return loan_data