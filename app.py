from docx2pdf import convert
import os, sys

def convert_word_to_pdf(input_path, output_paht):
    try:
        convert(input_path=input_path,output_path=output_paht)
        print(f"Conversion completed. PDF saved as {output_paht}")
    except Exception as e:
        print(f"An Error occoured: {str(e)}")

if __name__=="__main__":
    input_path = r"D:\Convert-Word-File-with-PDF\breakup.docx"
    output_path = r"D:\Convert-Word-File-with-PDF\BreakupStory.pdf"

    if os.path.exists(input_path):
        convert_word_to_pdf(input_path,output_path)
    else:
        print(f"Input word document file '{input_path}' doesnot exists")
    
