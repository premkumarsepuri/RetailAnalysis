from reportlab.lib.pagesizes import A4 # gives a4 size page
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table # pdf document builder, paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

class ReportGenerator:
    # Initialies the pdf and loads the text styles
    def __init__(self, level):
        self.filename = f"report_{level}.pdf"
        self.doc = SimpleDocTemplate(self.filename, pagesize=A4)
        self.story = []
        self.styles = getSampleStyleSheet()

    # title method
    def add_title(self):
        self.story.append(Paragraph(f"<b>{self.filename.replace('.pdf','')}</b>", self.styles['Title']))
        self.story.append(Spacer(1, 0.2 * inch))

   #paragraph method
    def add_paragraph(self, text):
        self.story.append(Paragraph(text, self.styles['BodyText']))
        self.story.append(Spacer(1, 0.2 * inch))

    #add image
    def add_image(self, path):
        self.story.append(Image(path, width=6 * inch, height=4 * inch))
        self.story.append(Spacer(1, 0.2 * inch))
    
    # add image
    def add_table(self, data_dict):
        data = [["Column", "Description"]] + list(data_dict.items())
        table = Table(data, hAlign='LEFT')
        self.story.append(table)
        self.story.append(Spacer(1, 0.2 * inch))
        
    #save pdf
    def save_pdf(self):
        self.doc.build(self.story)

