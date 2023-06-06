import textwrap
import cv2
from fpdf import FPDF
import time
from PIL import Image


def put_text(img, text, x_value, y_value,font_size, font_thickness):
    font = cv2.FONT_HERSHEY_SIMPLEX
    wrapped_text = textwrap.wrap(text, width=40)
    x, y = 200, 40


    for i, line in enumerate(wrapped_text):
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]

        gap = textsize[1] + 40
        y = 325
        #y = int((img.shape[0] + textsize[1]) / 2) + i * gap
        x = 50
        cv2.putText(img, line, (x_value, y_value), font,
                    font_size,
                    (0,0,0),
                    font_thickness,
                    lineType = cv2.LINE_AA)



f =open("files/Name.txt",'r')
name = f.read()

f.close()
f =open("files/Occupation.txt",'r')
occupation = f.read()
f.close()
f =open("files/Phonenum.txt",'r')
Phone = f.read()
f.close()
f =open("files/email.txt",'r')
email = f.read()
f.close()
f =open("files/Linkdin.txt",'r')
Linkdin = f.read()
f.close()
f =open("files/PresentAdd.txt",'r')
PresentAdd = f.read()
f.close()
f =open("files/shortdescription.txt",'r')
shortdescription = f.read()
f.close()
f =open("files/designation.txt",'r')
Designation = f.read()
f.close()
f =open("files/CompanyName.txt",'r')
CompanyName = f.read()
f.close()
f =open("files/CompanyDescription.txt",'r')
CompanyDes = f.read()
f.close()
f =open("files/Degree.txt",'r')
Degree = f.read()
f.close()
f =open("files/university.txt",'r')
Uni = f.read()
f.close()
f =open("files/Graduationdate.txt",'r')
GradDate = f.read()
f.close()
f =open("files/EducationDescription.txt",'r')
EduDes = f.read()
f.close()
f =open("files/languages.txt",'r')
Lang = f.read()
f.close()


base_image = Image.open("cv2.jpg")

wrap_image= Image.open("userinput.jpg")




wrap_image = wrap_image.resize((200, 200))  # Adjust the dimensions as per your requirements
base_image.paste(wrap_image, (30, 62))  # Adjust the position as per your requirements
base_image.save("result_image.jpg")

img = cv2.imread("result_image.jpg")

put_text(img, name, 50, 325,1,2)
put_text(img, occupation, 100, 380,0.25,1)
put_text(img, Phone, 100, 483,0.25,1)
put_text(img, email, 100, 505,0.25,1)
put_text(img, Linkdin, 100, 527,0.25,1)
put_text(img, PresentAdd, 100, 552,0.25,1)
put_text(img, shortdescription, 50, 650,0.25,1)
put_text(img, Designation, 315, 130,0.5,1)
put_text(img, CompanyName, 315, 160,0.25,1)
put_text(img, CompanyDes, 315, 190,0.25,1)
put_text(img, Degree, 315, 490,0.25,1)
put_text(img, Uni, 315, 515,0.25,1)
put_text(img, GradDate, 315, 535,0.25,1)
put_text(img, EduDes, 315, 555,0.25,1)
put_text(img, Lang, 315, 750,0.25,1)

cv2.imwrite("output.jpg", img)


pdf_filename = f"PDFS/{time.time()}.pdf"

pdf = FPDF(unit = "pt", format="A4")

pdf.add_page()




#pdf.set_font("Arial", size = 15)


pdf.image("output.jpg", x=0,y=0)

#saving the pdf
pdf.output(pdf_filename)