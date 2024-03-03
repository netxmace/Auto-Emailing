#Prepared by Goutham K B
#Python Script to send newsletter, this will send mail from gmail only. If any another smtp server is used change server name in Line#90

html_N = """\
<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">


<head>
    <title>Email Title</title>

    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="x-apple-disable-message-reformatting" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./style/styles.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
	
</head>

<body style="background-color:silver;">
<table style="width:100%;border-spacing:0px;" >
 
<tr> 
	<td style="width:10%;">&nbsp;</td> 
	<td style="color: white;background-color:black"><b>&nbsp;Hello {name}, </b> </td>  
	<td style="width:10%">&nbsp;</td> 
</tr>


<tr> 
	<td style="width:10%">&nbsp;</td> 
	<td style="width:80%;background-color:black" > <a href ="https://netxmace.github.io/"><img style="display:block;" width="100%" height="100%" src="cid:image1" alt="newsletter" id="a"></a> </td> 
	<td style="width:10%">&nbsp;</td> 
</tr>

<tr> 
   <td style="width:10%;">&nbsp;</td> 
   <td style="color: white;font-size:10px;text-align: center;background-color:black"> <i> Mail is send from NetX club MACE</i> </td> 
   <td style="width:10%">&nbsp;</td> 
</tr>

<tr> 
   <td style="width:10%;">&nbsp;</td> 
   <td style="color: white;font-size:10px;text-align: center;background-color:black"> <i>*Click the image to visit our webpage</i> </td> 
   <td style="width:10%">&nbsp;</td> 
</tr>
 
</table>

<body>

</html>
			
"""
import csv, smtplib, ssl, urllib.request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


# Define the pre-settings here.
strFrom = "thenetxnewsletter@gmail.com"
password = "aoihclfynjgbhpfq"
mailSubject = "Newsletter"
reciepientlistCsvFilename = "testcsv.csv"
newletterImageName = "newsletter.png"


msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = mailSubject
msgRoot['From'] = strFrom
msgRoot['To'] = strFrom
msgRoot.preamble = 'This is a multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

# msgText = MIMEText('Please visit online version of newsletter in https://svenski-79.github.io/NewsletterV3/.')
# msgAlternative.attach(msgText)

msgHtml = MIMEText(html_N, 'html')
msgAlternative.attach(msgHtml)

fp = open(newletterImageName, 'rb')
msgImage1 = MIMEImage(fp.read(), _subtype="png")
fp.close()

msgImage1.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage1)


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(strFrom, password)
    with open(reciepientlistCsvFilename) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            mailmsg =  msgRoot.as_string().format(name=name)
            server.sendmail(strFrom, email, mailmsg)