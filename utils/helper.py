from docx2pdf import convert

class WordToPDFConvert:
    def convert_word_to_pdf(input_path, output_path):
        try:
            convert(input_path=input_path,output_path=output_path)
            print(f"Conversion completed. PDF saved as {output_path}")
        except Exception as e:
            print(f"An Error occoured: {str(e)}")