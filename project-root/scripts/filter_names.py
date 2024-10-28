import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load data from Excel
df = pd.read_excel('data/input_data.xlsx')

# Filter names beginning with "H"
filtered_df = df[df['Name'].str.startswith('H')]

# Generate PDF
def create_pdf(dataframe, output_path):
    pdf = canvas.Canvas(output_path, pagesize=letter)
    pdf.setTitle("Filtered Names - Starting with H")

    # Write data to PDF
    text = pdf.beginText(40, 750)
    text.setFont("Helvetica", 12)
    text.textLine("Names Beginning with 'H'")
    text.textLine("")

    for index, row in dataframe.iterrows():
        text.textLine(row['Name'])
    
    pdf.drawText(text)
    pdf.save()

# Create the PDF file
create_pdf(filtered_df, 'filtered_names.pdf')
