import cv2
import winsound
from email.message import EmailMessage
import ssl
import smtplib
from twilio.rest import Client
from twilio.rest import Client

cam =cv2.VideoCapture(0)
email_sender ="nithishprabha07@gmail.com"
email_password="iuhl kibe ufqs svaf"
email_receiver="sidarthsidarth67326@gmail.com"
subject="*Alert:Burglar Detected*"
body="""
        Our burglar detection system has detected unusual movement near the premises. 
        Please be aware and take necessary precautions.
        If you are on-site, avoid confronting the intruder directly.
        Contact local authorities immediately and provide them with any relevant information. 
        Stay safe and await further instructions

    """

account_sid='ACd57f26840b4696cf2175e11fd935d78b'
auth_token= 'ceb67ccb32ba45b7816dab961be212e1'
client = Client(account_sid, auth_token)
def message():
       
    to_number='+916380294734'
    from_number='+12133443526'

    message = client.messages.create(
        body='\b*Alert: Possible Intrusion Detected*'
        '\n Our burglar detection system has detected unusual movement near the premises.'
        '\nPlease be aware and take necessary precautions.'
        '\nIf you are on-site, avoid confronting the intruder directly.'
        '\nContact local authorities immediately and provide them with any relevant information.' 
        '\nStay safe and await further instructions.',
        to=to_number,
        from_=from_number
    )
    print(message.sid)   



account_sid='ACd57f26840b4696cf2175e11fd935d78b'
auth_token='ceb67ccb32ba45b7816dab961be212e1'
Client=Client(account_sid,auth_token) 
def call():
   
    to_number='+916380294734'
    from_number='+12133443526'
    
    call=Client.calls.create(
        twiml='<Response><Say> Alert.   alert.   alert.'
        'Our burglar detection system has detected unusual movement near the premises.'
          ' Please be aware and take necessary precautions.'
          ' If you are on-site, avoid confronting the intruder directly.' 
          ' Contact local authorities immediately and provide them with any relevant information.' 
          ' Stay safe and await further instructions</Say></Response>',
        to=to_number,
        from_=from_number
    )
    print(call.sid)





def email():
    em= EmailMessage()
    em['From']=email_sender
    em['To']=email_receiver
    em['Subject']=subject

    em.set_content(body)
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
        
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())        




while cam.isOpened():
    ret,frame1 =cam.read()
    ret,frame2 =cam.read()
    diff =cv2.absdiff(frame1,frame2)
    gray =cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    blur =cv2.GaussianBlur(gray,(5,5),0)
    _,thresh =cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated =cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
    for c in contours:
        if cv2.contourArea(c) < 5000 :
            continue
        x,y,w,h =cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0), 2)
        winsound.PlaySound('alert.wav',winsound.SND_ASYNC)
        email()
        call()
        message()
        
    if cv2.waitKey(10) == ord('N'):
        break
    cv2.imshow('Freaky Cam',frame1)
 