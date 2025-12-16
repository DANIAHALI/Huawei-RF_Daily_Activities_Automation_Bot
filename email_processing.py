# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
import time


def email_func(login_email, login_pw, subject, To, Message):
    print('Processing Email!')
    time.sleep(2)
    strFrom = login_email

    strTo = To.split(',')

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = strFrom
    msgRoot['To'] = ", ".join(strTo)
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)


    msgText = MIMEText(Message +'<br><br><br>'    + '<b>' + '  Daily Activities Graphs  ' + '</b><br><br><img src="cid:image"><br><br><img src="cid:image1"><br><br><img src="cid:image2"><br><br><img src="cid:image3"><br><br><img src="cid:image4"><br><br><img src="cid:image5"><br><br><img src="cid:image6"><br><br><img src="cid:image7"><br><br><img src="cid:image8"><br><br><img src="cid:image9"><br><br><img src="cid:image10"><br><br><img src="cid:image11"><br><br><img src="cid:image12"><br><br><img src="cid:image13"><br><br><img src="cid:image14"><br><br><img src="cid:image15"><br><br><br><br>', 'html')
    msgAlternative.attach(msgText)

    fp = open(str(os.getcwd())+'\\Graphs\\User Downlink Average Throughput(Gbps).png', 'rb')
    Image_4G = MIMEImage(fp.read())
    fp = open(str(os.getcwd())+'\\Graphs\\User Uplink Average Throughput(Gbps).png', 'rb')
    Image_4G_001 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Cell Downlink Average Throughput(Gbps).png', 'rb')
    Image_4G_002 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Cell Uplink Average Throughput(Gbps).png', 'rb')
    Image_4G_003 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Downlink Resource Block Utilizing Rate.png', 'rb')
    Image_4G_004 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Uplink Resource Block Utilizing Rate.png', 'rb')
    Image_4G_005 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Radio Network Unavailability Rate.png', 'rb')
    Image_4G_006 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Downlink Traffic Volume(GB).png', 'rb')
    Image_4G_007 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Uplink Traffic Volume(GB).png', 'rb')
    Image_4G_008 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Average User Number.png', 'rb')
    Image_4G_009 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Maximum User Number.png', 'rb')
    Image_4G_010 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\SgNB Addition Success Rate.png', 'rb')
    Image_4G_011 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Intra-SgNB PSCell Change Success Rate.png', 'rb')
    Image_4G_012 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Inter-SgNB PSCell Change Success Rate.png', 'rb')
    Image_4G_013 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\SgNB-Triggered Abnormal SgNB Release Rate.png', 'rb')
    Image_4G_014 = MIMEImage(fp.read())
    fp = open(str(os.getcwd()) + '\\Graphs\\Network availability Rate (System).png', 'rb')
    Image_4G_015 = MIMEImage(fp.read())


    # Define the image's ID as referenced above
    Image_4G.add_header('Content-ID', '<image>')
    msgRoot.attach(Image_4G)
    Image_4G_001.add_header('Content-ID', '<image1>')
    msgRoot.attach(Image_4G_001)
    Image_4G_002.add_header('Content-ID', '<image2>')
    msgRoot.attach(Image_4G_002)
    Image_4G_003.add_header('Content-ID', '<image3>')
    msgRoot.attach(Image_4G_003)
    Image_4G_004.add_header('Content-ID', '<image4>')
    msgRoot.attach(Image_4G_004)
    Image_4G_005.add_header('Content-ID', '<image5>')
    msgRoot.attach(Image_4G_005)
    Image_4G_006.add_header('Content-ID', '<image6>')
    msgRoot.attach(Image_4G_006)
    Image_4G_007.add_header('Content-ID', '<image7>')
    msgRoot.attach(Image_4G_007)
    Image_4G_008.add_header('Content-ID', '<image8>')
    msgRoot.attach(Image_4G_008)
    Image_4G_009.add_header('Content-ID', '<image9>')
    msgRoot.attach(Image_4G_009)
    Image_4G_010.add_header('Content-ID', '<image10>')
    msgRoot.attach(Image_4G_010)
    Image_4G_011.add_header('Content-ID', '<image11>')
    msgRoot.attach(Image_4G_011)
    Image_4G_012.add_header('Content-ID', '<image12>')
    msgRoot.attach(Image_4G_012)
    Image_4G_013.add_header('Content-ID', '<image13>')
    msgRoot.attach(Image_4G_013)
    Image_4G_014.add_header('Content-ID', '<image14>')
    msgRoot.attach(Image_4G_014)
    Image_4G_015.add_header('Content-ID', '<image15>')
    msgRoot.attach(Image_4G_015)


    #************************************************************************************************

    # Info: for Gmail users
    import smtplib
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(login_email, login_pw)
    server.sendmail(strFrom, strTo, msgRoot.as_string())
    server.quit()

    #================================Huawei==========================================================
    # import smtplib
    # smtp_server = 'smtp.huawei.com'
    # pop_server = "pop.huawei.com"
    # email_username = 'pmail_ServicePub'
    # email_password = '65Pxqh1#'
    # email_from = 'servicepub@huawei.com'

    # import pdb
    # pdb.set_trace()

    # server = smtplib.SMTP()
    # server.connect('smtp.huawei.com', 25)
    # server.login(email_username, email_password)
    # #server.login('danish.ali3@huawei.com', 'D@sh8855')
    # server.sendmail(email_from, strTo, msgRoot.as_string())
    # #server.sendmail('danish.ali3@huawei.com', 'danish.ali2@huawei.com', msgRoot.as_string())
    # server.quit()

    #=================================================================================================
    print('Email Sent!')