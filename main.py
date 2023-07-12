from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4") # Orientation = [P]ortrait, [L]andscape
# this is the initial configuration
pdf.set_auto_page_break(auto=False, margin=0) #page should not be broken automatically

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page() #adding a page to pdf.
    #each time i put pdf.add_page() in the program, i add another page.

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], new_x="LMARGIN", new_y="NEXT", align='L')
    pdf.line(10,20, 200,20) #adding a line under the titles
    # related to text position in the page.
    # w=0 means that i am going to extend this line until the end of the page (related to the border)
    #new_x and new_y set the position of the text in the page. I used standard configurations,
    # new_y = "NEXT" means that the text will start in the next line.
    # new_x = "LMARGIN" means that the text will start in the defined margin to the left side.
    # h=12 means the size of the font.

    # Set the footer
    pdf.ln(265) #265 milimiters (page has 298), we will add a footer
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # adding horizontal lines
    for i in range(30, 298, 10):
        pdf.line(10, i, 200, i)

    
    # using range for iterating an interval of numbers
    for i in range(row["Pages"] - 1): 
        pdf.add_page()
        
        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # adding horizontal lines
        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)

pdf.output("output.pdf")