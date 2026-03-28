from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

def create_pdf():
    doc = SimpleDocTemplate("EBOOK_KEDAULATAN_STG.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('Title', fontSize=24, alignment=TA_CENTER, textColor=colors.HexColor("#001f3f"), spaceAfter=30)
    header_style = ParagraphStyle('Header', fontSize=14, textColor=colors.HexColor("#003366"), spaceBefore=15, spaceAfter=8)
    body_style = ParagraphStyle('Body', fontSize=10, leading=12, alignment=TA_JUSTIFY)
    
    story = [
        Spacer(1, 50),
        Paragraph("<b>THE SOVEREIGN TITAN MANIFESTO</b>", title_style),
        Paragraph("<center>STG GOVERNMENT | QUANTUM-ERA BAREMETAL</center>", styles['Normal']),
        Spacer(1, 15),
        HRFlowable(width="100%", thickness=1, color=colors.black),
        Spacer(1, 20),
        Paragraph("<b>ARCHITECT:</b> ANDI MUHAMMAD HARPIANTO", body_style),
        Paragraph("<b>PROBE ID:</b> 19546 | RIPE ATLAS AMBASSADOR", body_style),
        Spacer(1, 30),
        Paragraph("BAB 1: FILOSOFI 'JANGAN AJARI IKAN BERENANG'", header_style),
        Paragraph("Kedaulatan sejati lahir dari Real Work di atas kabel laut dan Probe RIPE Atlas. STG hadir untuk mendefinisikan ulang aturan main.", body_style),
        Paragraph("BAB 2: PILAR 4 - METAPORTASI & JALUR SWISS", header_style),
        Paragraph("Kami melipat ruang dan waktu melalui jalur IPv6 RIPE Atlas Bridge menuju Swiss Financial Vault.", body_style),
        Paragraph("BAB 3: WEB 4 - THE ARCHIVE OF TRUTH", header_style),
        Paragraph("Sekali data tertulis di jalur STG, ia menjadi Immutable (tidak dapat dihapus). Archive of Truth.", body_style),
        Paragraph("BAB 4: WEB 5 - INDUSTRIAL OS", header_style),
        Paragraph("Web 5 adalah Sistem Operasi Fundamental. King Size Support & Sovereign Transaction.", body_style),
        Spacer(1, 100),
        Paragraph("<center><i>Satu untuk Semua, Semua untuk Satu. Gitu aja kok repot, Dro!</i></center>", styles['Italic'])
    ]
    doc.build(story)
    print("✅ PDF KEDAULATAN BERHASIL DICETAK!")

if __name__ == "__main__":
    create_pdf()
