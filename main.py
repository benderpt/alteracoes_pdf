import fitz  # PyMuPDF
import difflib

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from each page of a PDF file.

    Args:
        pdf_path (str): The file path to the PDF document.

    Returns:
        str: The extracted text from the PDF.
    """
    # Abre o PDF e extrai o texto de cada página
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def compare_pdfs(pdf1_path, pdf2_path):
    """
    Compares the text content of two PDF files and returns the differences.

    Args:
        pdf1_path (str): The file path to the first PDF.
        pdf2_path (str): The file path to the second PDF.

    Returns:
        list: A list of strings representing the differences between the two PDFs.
    """
    # Extrai o texto dos dois PDFs
    text1 = extract_text_from_pdf(pdf1_path)
    text2 = extract_text_from_pdf(pdf2_path)

    # Usa difflib para comparar o texto
    diff = difflib.unified_diff(text1.splitlines(), text2.splitlines(), lineterm="")
    return list(diff)

def save_diff_to_file(diff, output_file):
    """
    Saves the differences to a specified file.

    Args:
        diff (list of str): A list of strings representing the differences.
        output_file (str): The path to the file where the differences will be saved.

    Returns:
        None
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in diff:
            f.write(line + '\n')

# Define os caminhos dos PDFs e do ficheiro de saída
PDF1_PATH = "data/planapp_organica_2021.pdf"
PDF2_PATH = "data/planapp_organica_2024.pdf"
OUTPUT_FILE = "differences.txt"

# Compara os PDFs e salva o resultado
differences = compare_pdfs(PDF1_PATH, PDF2_PATH)
save_diff_to_file(differences, OUTPUT_FILE)

print(f"Diferenças guardadas em {OUTPUT_FILE}")
