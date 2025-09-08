import os
import PyPDF2
import re

def merge_pdfs(input_folder, output_filename):
    if not os.path.exists(input_folder):
        print(f"Folderul {input_folder} nu există. Se creează acum...")
        os.makedirs(input_folder)
    
    pdf_merger = PyPDF2.PdfMerger()
    
    # Listăm toate fișierele PDF din folder
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
    
    # Grupăm fișierele după numărul din titlu și tratăm cazul special "Tichet"
    file_dict = {}

    for file in pdf_files:
        match_fisa = re.match(r'Fisa-(\d+)\.pdf', file)
        match_doc = re.match(r'(\d+)[ _-](.*)\.pdf', file)
        match_tichet = re.match(r'Tichet[ _-](\d+)[ _-](.*)\.pdf', file)  # Caz special pentru "Tichet"
        
        if match_fisa:
            numar = match_fisa.group(1)
            file_dict.setdefault(numar, []).insert(0, file)  # Fisa trebuie să fie prima
        elif match_tichet:
            numar = match_tichet.group(1)
            rest = match_tichet.group(2)
            file_dict.setdefault(numar, []).append((file, rest))  # Tichetul trebuie să vină după fișă
        elif match_doc:
            numar = match_doc.group(1)
            rest = match_doc.group(2)
            file_dict.setdefault(numar, []).append((file, rest))  # Documentele trebuie să urmeze tichetele

    sorted_files = []
    for numar in sorted(file_dict.keys(), key=int):
        fisa_files = [f for f in file_dict[numar] if isinstance(f, str)]
        doc_files = sorted([f for f in file_dict[numar] if isinstance(f, tuple)], key=lambda x: x[1])
        sorted_files.extend(fisa_files + [f[0] for f in doc_files])

    if not sorted_files:
        print("Nu există fișiere PDF în folder.")
        return

    for pdf in sorted_files:
        pdf_path = os.path.join(input_folder, pdf)
        try:
            pdf_merger.append(pdf_path)
            print(f"Adăugat: {pdf}")
        except Exception as e:
            print(f"Eroare la adăugarea fișierului {pdf}: {e}")

    output_path = os.path.join(input_folder, output_filename)
    pdf_merger.write(output_path)
    pdf_merger.close()
    
    print(f"Fișierele au fost unite în: {output_path}")

if __name__ == "__main__":
    folder_name = "pdfs"
    folder = os.path.join(os.getcwd(), folder_name)
    output_pdf = input("Introduceți numele fișierului final (ex: unificat.pdf): ")
    merge_pdfs(folder, output_pdf)
