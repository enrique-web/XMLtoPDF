import aspose.pdf as ap

def convert_xml_to_pdf(xml_path: str, pdf_path: str):
    # Create a new PDF document
    pdf_document = ap.Document()

    # Bind XML file to the PDF document
    pdf_document.bind_xml(xml_path)

    # Save the PDF document
    pdf_document.save(pdf_path)
    print(f"PDF generated at: {pdf_path}")

if __name__ == "__main__":
    input_xml = "sample.xml"     # Path to your XML file
    output_pdf = "output.pdf"    # Path to save generated PDF
    convert_xml_to_pdf(input_xml, output_pdf)
