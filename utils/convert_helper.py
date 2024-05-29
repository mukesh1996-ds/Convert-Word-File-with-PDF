from utils.helper import WordToPDFConvert


def convert_word_to_pdf(input_path, output_path):
    try:
        WordToPDFConvert.convert_word_to_pdf(input_path, output_path)
        return f"Conversion completed. PDF saved as {output_path}"
    except Exception as e:
        return f"An error occoured: {str(e)}"