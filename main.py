import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# when multiple files have to be read use globe to loop through !!
filepaths = glob.glob("invoice/*.xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()

    raw_filename = Path(filepath).stem
# filename,date these two variables will contain the list value as filename - [0], date - [1]
    filename, date = raw_filename.split("-")
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice no: {filename}",ln=1)

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=2)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    """
    Other way is using columns method
    column = list(df.columns)
    pdf.cell(w=30, h=8, txt=f"{column[0]}", border=1)
    """

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=8, txt="Product_id", border=1)
    pdf.cell(w=70, h=8, txt="Product_name", border=1)
    pdf.cell(w=30, h=8, txt="Amount", border=1)
    pdf.cell(w=30, h=8, txt="Price", border=1)
    pdf.cell(w=30, h=8, txt="Total_price", border=1, ln=1)
    for index, row in df.iterrows():

        pdf.set_font(family="Times", size=8)
        pdf.cell(w=30, h=8, txt=f"{row['product_id']}", border=1)
        pdf.cell(w=70, h=8, txt=f"{row['product_name']}", border=1)
        pdf.cell(w=30, h=8, txt=f"{row['amount_purchased']}", border=1)
        pdf.cell(w=30, h=8, txt=f"{row['price_per_unit']}", border=1)
        pdf.cell(w=30, h=8, txt=f"{row['total_price']}",border=1, ln=1)

    total_sum = df["total_price"].sum()

    pdf.set_font(family="Times", size=8)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=30, h=8, txt=f"The total due amount is : {total_sum} rupees ", ln=1)

    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt="Invoice Generator")
    pdf.image("pythonhow.png", w=10)

    pdf.output(f"PDFs/{raw_filename}.pdf")
