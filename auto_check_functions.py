import os
from pathlib import Path
import csv
from easygui import *

def detect_files(subdirectory):
    context_file = os.path.join(subdirectory, 'context.txt')
    input_file = None
    for file in os.listdir(subdirectory):
        if file != 'context.txt':
            input_file = os.path.join(subdirectory, file)
            break
    return context_file, input_file

def read_context(context_file):
    with open(context_file, 'r') as file:
        return file.read()
    
def get_file_extension(input_file):
    return Path(input_file).suffix[1:]

def check_file_type(input_file):
    allowed_extensions = [
        'csv', 'json', 'txt', 'md', 'rst', 'tex', 'pdf', 'py', 'sql', 'gz',
        'jpg', 'jpeg', 'svg', 'png', 'gif', 'notebook', 'r'
    ]
    file_extension = get_file_extension(input_file)
    return file_extension in allowed_extensions

def check_context_length(context):
    return len(context) >= 250

def check_csv_format(input_file):
    try:
        with open(input_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            if len(headers) > 30:
                return False, "CSV has more than 30 columns"
            for row in reader:
                if any(isinstance(field, str) for field in row):
                    return False, "CSV contains string values"
            return True, "CSV is properly formatted"
    except Exception as e:
        print("Csv file is not formatted for automatic checking")
        return False, str(e)

def validate_inputs(context, input_file):
    if not check_file_type(input_file):
        return f"File type {get_file_extension(input_file)} is not allowed. Do you want to continue? (yes/no)"
    if not check_context_length(context):
        return "Context string is less than 250 characters. Do you want to continue? (yes/no)"
    if input_file.endswith('.csv'):
        is_valid, message = check_csv_format(input_file)
        if not is_valid:
            return f"{message}. Do you want to continue? (yes/no)"
    return "All checks passed"

