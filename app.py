import tabula
import pandas as pd

# Specify the PDF file path
pdf_path = "demo.pdf"

# Specify the output CSV file path
output_csv_path = "demo_csv.csv"

# Convert PDF to CSV
tabula.convert_into(pdf_path, output_csv_path, output_format="csv", pages="all")

# Read the CSV file using pandas
df = pd.read_csv(output_csv_path)

# Specify the output Excel file path
output_excel_path = "data_excel.xlsx"

# Save the DataFrame as an Excel file (XLSX)
df.to_excel(output_excel_path, index=False)