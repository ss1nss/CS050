import pandas as pd

import os

import shutil

 # fixed output amount to not exceed upload limit in database, which is 15,000 rows

def process_excel_file(input_file, header_mapping, max_rows=15000):

    try:

        # Read the input Excel file

        df = pd.read_excel(input_file, header=2)

       

        # Rename headers based on the provided mapping

        df.rename(columns=header_mapping, inplace=True)

       

        # Split the dataframe into chunks of max_rows ±2

        num_chunks = len(df) // max_rows + (1 if len(df) % max_rows != 0 else 0)

       

        # Get the base name of the input file without extension

        base_name = os.path.splitext(os.path.basename(input_file))

       

        # Replace parentheses in the base name

        base_name = base_name.replace('(', '').replace(')', '')

       

        # Process each chunk

        start_row = 0

        for i in range(num_chunks):

            end_row = start_row + max_rows

           

            chunk = df.iloc[start_row:end_row]

           

            # Calculate row count for the chunk

            row_count = len(chunk)

           

            # Save each chunk to a new Excel file with row count in parentheses

            chunk.to_excel(f"{base_name}({row_count})_part_{i + 1}.xlsx", index=False)

           

            start_row = end_row

       

        print(f"Processed file: {input_file}")

   

    except Exception as e:

        print(f"Error processing file {input_file}: {e}")

 

def main():

    header_mapping = {

        'Offer Acceptance Date': 'Test_Converted_Name',

        'Invoice Status': 'Test_Converted_Name2',

        # Add more header mappings as needed

    }

 

    # Process all Excel files in the specified directory

    input_directory = r'C:\Users' # replace directory where input file is located

    completed_directory = r'C:\Users' # replace directory where output should be located

 

    # Create the completed directory if it doesn't exist

    os.makedirs(completed_directory, exist_ok=True)

 

    for filename in os.listdir(input_directory):

        if filename.endswith('.xlsx'):

            input_file_path = os.path.join(input_directory, filename)

            process_excel_file(input_file_path, header_mapping)

           

            # Move the processed file to the completed directory

            shutil.move(input_file_path, os.path.join(completed_directory, filename))

 

if __name__ == "__main__":

    main()