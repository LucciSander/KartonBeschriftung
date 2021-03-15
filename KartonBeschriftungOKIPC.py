from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import	A4
from reportlab.lib.units import mm
from reportlab.lib.styles import LineStyle
from reportlab.pdfbase.pdfmetrics import stringWidth



def makeLable(filename, MaschNr, AuftrNr, SeriNr):

	myCanvas = canvas.Canvas(filename, pagesize=A4)
	width, height = A4

	#Klebe-Linien
	myCanvas.setLineWidth(2.25)
	myCanvas.line(0*mm,25*mm,210*mm,25*mm)
	myCanvas.line(0*mm,height-(25*mm),210*mm,height-(25*mm))
	myCanvas.line(0*mm,height/2 + 25*mm,210*mm,height/2 + 25*mm)
	myCanvas.line(0*mm,height/2-(25*mm),210*mm,height/2-(25*mm))


	#Mittellinie
	myCanvas.setLineWidth(0.75)
	myCanvas.setDash(3,3)
	myCanvas.line(0*mm,height/2,210*mm,height/2)


	#Maschinennummer
	myCanvas.setFont("Helvetica-Bold",72)
	text_width = stringWidth(MaschNr,"Helvetica-Bold", 72 )
	myCanvas.drawString((width - text_width) / 2 ,95*mm, text=MaschNr)
	myCanvas.drawString((width - text_width) / 2 ,height/2 + 95*mm, text=MaschNr)

	#Auftragsnummer
	myCanvas.setFont("Helvetica",48)
	text_width = stringWidth(MaschNr,"Helvetica", 48 )
	myCanvas.drawString((width - text_width) / 2 ,65*mm, text=AuftrNr)
	myCanvas.drawString((width - text_width) / 2 ,height/2 + 65*mm, text=auftrag)

	#Seriennummer
	myCanvas.setFont("Helvetica",36)
	text_width = stringWidth(SeriNr,"Helvetica", 36 )
	myCanvas.drawString((width - text_width) / 2 ,40*mm, text=SeriNr)
	myCanvas.drawString((width - text_width) / 2 ,height/2 + 40*mm, text=SeriNr)

	myCanvas.showPage()

	myCanvas.save()

# Welche Art von IPC OK oder Beckhoff
art = input("OKIPC = 1 \nBeckhoff-IPC = 2\n\n")





if art == "1":
	maschine = input("Maschinennummer und IPC-Bezeichnung:   ")
	auftrag = input("Auftragsnummer:    ")
	IPC = input("IPC-Seriennummer:    ")
	makeLable("beschriftung{}.pdf".format(maschine),maschine, auftrag, IPC )
elif art == "2":
	exit()
	maschine = input("Maschinennummer und IPC-Bezeichnung:   ")
	auftrag = input("Auftragsnummer:    ")
else:
	exit()
	
	
