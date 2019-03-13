import smtplib
content = "Hi there the code worked"
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login("shrutidhimands@gmail.com","sdhiman98")
mail.sendmail("shrutidhimands@gmail.com","sdhiman_be15@thapar.edu",content)
mail.close()
print("the code worked")