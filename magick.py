from wand.image import Image
from wand.display import display
from pyPdf import PdfFileWriter, PdfFileReader
import urllib2
import io

with Image(file=urllib2.urlopen('https://fbcdn-sphotos-h-a.akamaihd.net/hphotos-ak-ash4/2995_564002320286807_2118083206_n.jpg')) as img:
    print(img.size)
    for r in 1, 2, 3:
        with img.clone() as i:
            i.resize(int(i.width * r * 0.25), int(i.height * r * 0.25))
            i.rotate(90 * r)
            i.save(filename='mona-lisa-{0}.pdf'.format(r))
    input1 = PdfFileReader(file("mona-lisa-1.pdf", "rb"))
    page1 = input1.getPage(0)
    input2 = PdfFileReader(open("mona-lisa-1.pdf", "rb"))
    page2 = input2.getPage(0)
    f = io.BytesIO(img.make_blob('pdf'))
    input3 = PdfFileReader(f)
    page4 = input3.getPage(0)
    output = PdfFileWriter()
    output.addPage(page1)
    output.addPage(page2)
    output.addPage(page4)
    outputStream = file("output.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
