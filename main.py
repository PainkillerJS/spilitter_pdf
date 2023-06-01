

from borb.pdf import Document, PDF

page_count = 12

def split_half_half(input_pdf_href: str):
  # Читать PDF
  with open(input_pdf_href, "rb") as pdf_file_handle:
    input_pdf = PDF.loads(pdf_file_handle)
    
  count_pages_input_pdf = int(input_pdf.get_document_info().get_number_of_pages())
  
  output_pdfs = []

  # Разделение
  for i in range(0, count_pages_input_pdf):
    if i % page_count == 0:
       output_pdfs.append(Document())   
       
    output_pdfs[-1].add_page(input_pdf.get_page(i))  
    
  print(len(output_pdfs))    
  
  for i in range(0, len(output_pdfs)):
    with open(f"output_{i + 1}.pdf", "wb") as pdf_out_handle:
        PDF.dumps(pdf_out_handle, output_pdfs[i])  

    
if __name__ == "__main__":
    import sys
    
    input_file = sys.argv[1]
    
    split_half_half(input_file)