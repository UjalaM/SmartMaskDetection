from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse
from mask_detector.camera import WebCam
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase
from email import encoders  
import pyautogui 
import smtplib
import ssl

def home(request):    
    return render(request,'home.html')

def webcam(request):
    return render(request,'webcam.html')

def send_mail(request):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'E:/Ujala_folder/sem 6/ml/Sem6_FD/SmartMaskDetector/dataset/ss.png')
   
    sender_email = 'anchallsm2000@gmail.com'
    sender_name = 'Anchal Maurya'
    password = 'frjbzdqbkadzhupv'
    receiver_email = 'ujalamaurya.um@gmail.com'
    receiver_name = 'Ujala Maurya'
    body = """\
        <html>
          <body bgcolor=blue>
            <h3>Hello """ + receiver_name + """,<h3>
            <br>
            <h4>This email has been sent to you to inform that the 
            following person in screenshot is not wearing mask.<h4>
            <br>
          </body>
        </html>
        """
    filename = 'E:/Ujala_folder/sem 6/ml/Sem6_FD/SmartMaskDetector/dataset/ss.png'
    msg = MIMEMultipart()
    msg['To'] = formataddr((receiver_name, receiver_email))
    msg['From'] = formataddr((sender_name, sender_email))
    msg['Subject'] = 'Regarding No Mask'
    msg.attach(MIMEText(body,'html', 'utf-8'))
    try:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {filename}",
                )
        msg.attach(part)
        
    except Exception as e:
            print(f'Oh no! We didnt found the attachment!n{e}')
           
    try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            context = ssl.create_default_context()
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            
    except Exception as e:
            print(f'Oh no! Something bad happened!n{e}')
            
    finally:
            server.quit()
    
    return redirect('home')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
	return StreamingHttpResponse(gen(WebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')


