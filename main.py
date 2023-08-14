import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
filepaths = glob.glob("invoice/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf.add_page()

    raw_filename = Path(filepath).stem
    filename = raw_filename.split("-")[0]
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice no: {filename}")
    pdf.output(f"PDFs/{raw_filename}.pdf")
