from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4") # Orientation = [P]ortrait, [L]andscape
# this is the initial configuration

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page() #adding a page to pdf.
    #each time i put pdf.add_page() in the program, i add another page.

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], new_x="LMARGIN", new_y="NEXT", align='L')
# related to text position in the page.
# w=0 means that i am going to extend this line until the end of the page (related to the border)
#new_x and new_y set the position of the text in the page. I used standard configurations,
# new_y = "NEXT" means that the text will start in the next line.
# new_x = "LMARGIN" means that the text will start in the defined margin to the left side.
# h=12 means the size of the font.
    pdf.line(10,22, 200,22) #adding a line under the titles

pdf.output("output.pdf")