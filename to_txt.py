import PyPDF2

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    return text

def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    pdf_path = 'tesis_doctoral.pdf'  # Change this to the path of your PDF file
    output_file = 'tesis_doctoral.txt'  # Change this to the desired output file path
    
    extracted_text = pdf_to_text(pdf_path)
    save_text_to_file(extracted_text, output_file)
    print("Text extracted and saved successfully.")
