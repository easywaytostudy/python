import smtplib
content = "Hi there the code worked"
password = input("enter the password")
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login("shrutidhimands@gmail.com",password)
mail.sendmail("shrutidhimands@gmail.com","sdhiman_be15@thapar.edu",content)
mail.close()
print("the code worked")
