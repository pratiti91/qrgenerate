import qrcode
import image
img = qrcode.make("https://www.youtube.com/watch?v=EEqq0_Etuos&list=RDEEqq0_Etuos&start_radio=1")
print(img)
img.save('Pratiti1.jpg')