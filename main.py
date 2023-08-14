import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# when multiple files have to be read use globe to loop through !!
filepaths = glob.glob("invoice/*.xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf.add_page()

    raw_filename = Path(filepath).stem
# filename,date these two variables will contain the list value as filename - [0], date - [1]
    filename, date = raw_filename.split("-")
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice no: {filename}",ln=1)

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date: {date}")

    pdf.output(f"PDFs/{raw_filename}.pdf")
