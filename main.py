from utils.helper import WordToPDFConvert
import os


class WordToPDFApp:
    def __init__(self,input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def convert(self):
        if os.path.exists(self.input_path):
            WordToPDFConvert.convert_word_to_pdf(self.input_path,self.output_path)
        else:
            print(f"Input word document file '{self.input_path}' doesnot exists") 

if __name__=="__main__":
    input_path = r"D:\Convert-Word-File-with-PDF\lovestory.docx"
    output_path = r"D:\Convert-Word-File-with-PDF\LoveStory.pdf"

    app = WordToPDFApp(input_path, output_path)
    app.convert()

