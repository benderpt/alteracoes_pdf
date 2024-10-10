import fitz  # PyMuPDF
import difflib

def extract_text_from_pdf(pdf_path):
    # Abre o PDF e extrai o texto de cada página
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def compare_pdfs(pdf1_path, pdf2_path):
    # Extrai o texto dos dois PDFs
    text1 = extract_text_from_pdf(pdf1_path)
    text2 = extract_text_from_pdf(pdf2_path)

    # Usa difflib para comparar o texto
    diff = difflib.unified_diff(text1.splitlines(), text2.splitlines(), lineterm="")
    return list(diff)

def save_diff_to_file(diff, output_file):
    with open(output_file, 'w') as f:
        for line in diff:
            f.write(line + '\n')

# Define os caminhos dos PDFs e do ficheiro de saída
pdf1_path = "c/workspaces/alteracoes_pdf/data/planapp_organica_2021.pdf"
pdf2_path = "c/workspaces/alteracoes_pdf/data/planapp_organica_2024.pdf"
output_file = "differences.txt"

# Compara os PDFs e salva o resultado
differences = compare_pdfs(pdf1_path, pdf2_path)
save_diff_to_file(differences, output_file)

print(f"Diferenças guardadas em {output_file}")
