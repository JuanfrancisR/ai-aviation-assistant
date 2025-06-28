from fpdf import FPDF
from datetime import datetime

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Maintenance Squawk & RTS Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_pdf(squawk_text, analysis_result, output_path="report.pdf"):
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Original Squawk:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, squawk_text)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "AI Analysis & Write-Off:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, analysis_result)

    pdf.output(output_path)
    return output_path
