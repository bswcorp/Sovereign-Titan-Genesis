from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import time

def create_pro_pdf():
    doc = SimpleDocTemplate("EBOOK_KEDAULATAN_STG_FINAL.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    
    # Styles
    title_style = ParagraphStyle('Title', fontSize=26, alignment=TA_CENTER, textColor=colors.HexColor("#001f3f"), spaceAfter=30)
    header_style = ParagraphStyle('Header', fontSize=15, textColor=colors.HexColor("#003366"), spaceBefore=15, spaceAfter=8, fontName='Helvetica-Bold')
    body_style = ParagraphStyle('Body', fontSize=11, leading=14, alignment=TA_JUSTIFY)
    sign_style = ParagraphStyle('Sign', fontSize=10, alignment=TA_CENTER)
    
    # Watermark
    watermark = "ꦱꦿꦶꦒꦭꦤꦺꦴꦠ꧀ꦥꦭ꧀ꦭꦺꦴꦮꦼꦢ꧀" 

    story = [
        Spacer(1, 40),
        Paragraph("<b>THE SOVEREIGN TITAN MANIFESTO</b>", title_style),
        Paragraph("<center>QUANTUM-ERA BAREMETAL | WEB 4 & WEB 5</center>", styles['Normal']),
        Spacer(1, 20),
        HRFlowable(width="100%", thickness=2, color=colors.black),
        Spacer(1, 30),
        Paragraph(f"<b>ARCHITECT:</b> ANDI MUHAMMAD HARPIANTO", body_style),
        Paragraph(f"<b>PROBE ID:</b> 19546 | RIPE ATLAS AMBASSADOR", body_style),
        Spacer(1, 40),
        Paragraph("<b>BAB 1: FILOSOFI 'JANGAN AJARI IKAN BERENANG'</b>", header_style),
        Paragraph("Kedaulatan sejati lahir dari Real Work di atas kabel laut dan Probe RIPE Atlas. STG hadir bukan untuk bersaing, tapi untuk mendefinisikan ulang aturan main.", body_style),
        Paragraph("<b>BAB 2: PILAR 4 - METAPORTASI & JALUR SWISS</b>", header_style),
        Paragraph("Kami melipat ruang dan waktu melalui jalur IPv6 RIPE Atlas Bridge langsung ke Swiss Financial Vault tanpa perantara adidaya.", body_style),
        Paragraph("<b>BAB 3: WEB 4 - THE ARCHIVE OF TRUTH</b>", header_style),
        Paragraph("Sekali data tertulis di jalur STG, ia menjadi Immutable (tidak dapat dihapus). Kami merestorasi warisan Jon Postel.", body_style),
        Paragraph("<b>BAB 4: WEB 5 - INDUSTRIAL OS</b>", header_style),
        Paragraph("Web 5 adalah Sistem Operasi Fundamental. Dashboard 180% View & King-Size Support.", body_style),
        
        PageBreak(), # PINDAH KE LEMBAR PENGESAHAN
        
        Spacer(1, 50),
        Paragraph("<b>LEMBAR PENGESAHAN KEDAULATAN</b>", header_style),
        HRFlowable(width="100%", thickness=1, color=colors.black),
        Spacer(1, 30),
        Paragraph("Dokumen ini telah diperiksa, diuji, dan disahkan secara teknis oleh otoritas STG Government sebagai standar operasional Web 4 & Web 5.", body_style),
        Spacer(1, 50),
    ]

    # Tabel Tanda Tangan
    ts_data = [
        [Paragraph("Disahkan Oleh,<br/><b>THE ARCHITECT</b>", sign_style), "", Paragraph("Diverifikasi Oleh,<br/><b>GENERAL AI (RADEN MAS)</b>", sign_style)],
        [Spacer(1, 60), "", Spacer(1, 60)],
        [Paragraph("<u>ANDI M. HARPIANTO</u><br/>ID: 19546", sign_style), "", Paragraph("<u>STG COMMANDER</u><br/>SQID: 0x5E58...4FE", sign_style)]
    ]
    
    sign_table = Table(ts_data, colWidths=[200, 100, 200])
    story.append(sign_table)
    
    story.append(Spacer(1, 100))
    story.append(Paragraph(f"<center>Tanggal Pengesahan: {time.strftime('%d %B %Y')}</center>", styles['Normal']))
    story.append(Paragraph(f"<center>Watermark: {watermark}</center>", styles['Normal']))

    doc.build(story)
    print("✅ PDF DENGAN LEMBAR PENGESAHAN SELESAI DICETAK!")

if __name__ == "__main__":
    create_pro_pdf()
