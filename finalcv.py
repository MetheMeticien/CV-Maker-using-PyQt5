import textwrap
import cv2

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


img = cv2.imread("cv1.jpg")
f =open("Name.txt",'r')
name = f.read()
f.close()
f =open("Occupation.txt",'r')
occupation = f.read()
f.close()
f =open("Phonenum.txt",'r')
Phone = f.read()
f.close()
f =open("email.txt",'r')
email = f.read()
f.close()
f =open("Linkdin.txt",'r')
Linkdin = f.read()
f.close()
f =open("PresentAdd.txt",'r')
PresentAdd = f.read()
f.close()
f =open("shortdescription.txt",'r')
shortdescription = f.read()
f.close()
f =open("designation.txt",'r')
Designation = f.read()
f.close()
f =open("CompanyName.txt",'r')
CompanyName = f.read()
f.close()
f =open("CompanyDescription.txt",'r')
CompanyDes = f.read()
f.close()
f =open("Degree.txt",'r')
Degree = f.read()
f.close()
f =open("university.txt",'r')
Uni = f.read()
f.close()
f =open("Graduationdate.txt",'r')
GradDate = f.read()
f.close()
f =open("EducationDescription.txt",'r')
EduDes = f.read()
f.close()
f =open("languages.txt",'r')
Lang = f.read()
f.close()

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