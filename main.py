from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,200,1)
    pdf.cell(w=10, h=12, txt=row["Topic"], align="L", ln=1)

    for j in range(20,298,10):
        pdf.line(10,j,200,j)
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")
    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(278)  # blank lines
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)

        for j in range(0, 300, 10):
            pdf.line(10, j, 200, j)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
