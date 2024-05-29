import gradio as gr
from utils.convert_helper import convert_word_to_pdf

def gradio_convert_word_to_pdf(input_word):
    try:
        input_word_path=input_word.name
        output_pdf_path=r"D:\Convert-Word-File-with-PDF\BreakupStory1.pdf"
        result_message = convert_word_to_pdf(input_word_path,output_pdf_path)
        return result_message
    except Exception as e:
        return f"Error occoured: {str(e)}"


# Create Gradio base user interface 

app = gr.Interface(fn=gradio_convert_word_to_pdf,
                   inputs=gr.File(label="Input Word Document"),
                    outputs=gr.Textbox(label="Conversion status"),
                    live=True,
                    title="Word To PDF Converter",
                    description="Convert word document to PDF")


if __name__=="__main__":
    app.launch()