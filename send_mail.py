import streamlit as st
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def mime_init(from_addr, recipients_addr, subject, body):
    """
    :param str from_addr:           The email address you want to send mail from
    :param list recipients_addr:    The list of email addresses of recipients
    :param str subject:             Mail subject
    :param str body:                Mail body
    :return:                        MIMEMultipart object
    """
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = ','.join(recipients_addr)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg


def send_analysis(recipients_addr, files_path=None, server='smtp.gmail.com'):
    """
    :param str user:                Sender's email userID
    :param str password:            sender's email password
    :param str from_addr:           The email address you want to send mail from
    :param str recipients_addr:    List of (or space separated string) email addresses of recipients
    :param str subject:             Mail subject
    :param str body:                Mail body
    :param list files_path:         List of paths of files you want to attach
    :param str server:              SMTP server (port is choosen 587)
    :return:                        None
    """
    user = st.secrets["sau_kariyer"]
    password = st.secrets["sau_kariyer_sifre"]
    #   assert isinstance(recipents_addr, list)
    FROM = "Sakarya Üniversitesi Kariyer ve Yetenek Yönetimi Koordinatörlüğü"
    TO = recipients_addr if isinstance(recipients_addr, list) else recipients_addr.split(' ')
    PASS = password
    SERVER = server
    SUBJECT = "Kelime Testi Envanteri Sonuçları"
    BODY = "Tamamlamış olduğunuz envantere ait sonuçlar ekte yer almaktadır."
    msg = mime_init(FROM, TO, SUBJECT, BODY)

    for file_path in files_path or []:
        with open(file_path, "rb") as fp:
            part = MIMEBase('application', "octet-stream")
            part.set_payload((fp).read())
            # Encoding payload is necessary if encoded (compressed) file has to be attached.
            encoders.encode_base64(part)
            part.add_header('content-disposition', 'attachment', filename='%s' % file_path)
            msg.attach(part)

    if SERVER == 'localhost':  # send mail from local server
        # Start local SMTP server
        server = smtplib.SMTP(SERVER)
        text = msg.as_string()
        server.send_message(msg)
    else:
        # Start SMTP server at port 587
        server = smtplib.SMTP(SERVER, 587)
        server.starttls()
        # Enter login credentials for the email you want to sent mail from
        server.login(user, PASS)
        text = msg.as_string()
        # Send mail
        server.sendmail(FROM, TO, text)

    server.quit()


def send_analysi_to_analysis(recipients_addr, files_path=None, server='smtp.gmail.com'):
    """
    :param str user:                Sender's email userID
    :param str password:            sender's email password
    :param str from_addr:           The email address you want to send mail from
    :param str recipients_addr:    List of (or space separated string) email addresses of recipients
    :param str subject:             Mail subject
    :param str body:                Mail body
    :param list files_path:         List of paths of files you want to attach
    :param str server:              SMTP server (port is choosen 587)
    :return:                        None
    """
    user = st.secrets["sau_kariyer"]
    password = st.secrets["sau_kariyer_sifre"]
    #   assert isinstance(recipents_addr, list)
    FROM = "Sakarya Üniversitesi Kariyer ve Yetenek Yönetimi Koordinatörlüğü"
    TO = recipients_addr if isinstance(recipients_addr, list) else recipients_addr.split(' ')
    PASS = password
    SERVER = server
    SUBJECT = "Kelime Testi Envanteri Sonuçları"
    BODY = "Öğrenciye ait envanter sonuçları ekte yer almaktadır."
    msg = mime_init(FROM, TO, SUBJECT, BODY)

    for file_path in files_path or []:
        with open(file_path, "rb") as fp:
            part = MIMEBase('application', "octet-stream")
            part.set_payload((fp).read())
            # Encoding payload is necessary if encoded (compressed) file has to be attached.
            encoders.encode_base64(part)
            part.add_header('content-disposition', 'attachment', filename='%s' % file_path)
            msg.attach(part)

    if SERVER == 'localhost':  # send mail from local server
        # Start local SMTP server
        server = smtplib.SMTP(SERVER)
        text = msg.as_string()
        server.send_message(msg)
    else:
        # Start SMTP server at port 587
        server = smtplib.SMTP(SERVER, 587)
        server.starttls()
        # Enter login credentials for the email you want to sent mail from
        server.login(user, PASS)
        text = msg.as_string()
        # Send mail
        server.sendmail(FROM, TO, text)

    server.quit()