import os
from fpdf import FPDF
from pypdf import PdfReader, PdfWriter
from fpdf.enums import XPos
from fpdf.enums import YPos



def text_to_pdf():
    try:
        pdf=FPDF()
        pdf.set_auto_page_break(auto=True, margin=20)
        pdf.add_page()
        pdf.set_font("Helvetica", 'B', 18)
        pdf.cell(w=0,h=12,text=title,border=0,align='C',new_x=XPos.LMARGIN, new_y=YPos.NEXT )
        pdf.ln(8)
        pdf.set_font("Helvetica", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.output(dto)
        print("\n[SUCCESS] Text is successfully converted into PDF: ",dto)
    except Exception as e:
        print("ERROR ,Check the details filled",e)


def edit_pdf(newpdf, existingpdf, finalpdf):
    try:
        new = PdfReader(newpdf)
        existing = PdfReader(existingpdf)
        writer = PdfWriter()
        for page in new.pages:
            writer.add_page(page)
        for page in existing.pages:
            writer.add_page(page)
        with open(finalpdf, "wb") as f:
            writer.write(f)
        os.remove(newpdf)
        print("\n[SUCCESS] PDF is Edited: ",finalpdf)
    except FileNotFoundError as F:
        print("ERROR ,Check the details filled",F)
    except Exception as e:
        print("ERROR ,Check the details filled",e)

def compress_pdf(pdf):
    try:
        reader = PdfReader(pdf)
        writer=PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        base, ext = os.path.splitext(pdf)
        pdfname = base+"_compressed"+ext
        with open(pdfname, "wb") as f:
            writer.write(f)
        print("[SUCCESS] Pdf is successfully compressed as: ",pdfname)
    except FileNotFoundError as F:
        print("ERROR ,Check the details filled",F)
    except Exception as e:
        print("ERROR ,Check the details filled",e)

        


a=int(input("1 for new pdf\n2 for edit existing pdf by adding new topic\n3 for compressing Pdf\nEnter: "))
if a==1:
    dto=str(input("PDF name: \n")+".pdf")
    title=str(input("Enter the Title: \n"))
    text=str(input("Enter the text: \n"))
    text_to_pdf()
elif a==2:
    dto="new.pdf"
    title=str(input("Enter the Title: \n"))
    text=str(input("Enter the text: \n"))
    pre=str(input("Editing PDF name: \n")+".pdf")
    final=str(input("Final PDF name: \n")+".pdf")
    text_to_pdf()
    edit_pdf(dto,pre,final)
elif a==3:
    com=str(input("Compressing PDF name: \n")+".pdf")
    compress_pdf(com)
else:
    print("Invalid choice")
