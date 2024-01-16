from random import randint
from datetime import datetime
import smtplib
import pandas

my_email = "sushiuchihc@gmail.com"
password = "ulpshbscpemsrozk"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
birthday_person = birthdays_dict[today_tuple]


def send_mail():
    with open(f"letter_templates/letter_{randint(1,3)}.txt") as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Birthday Wishes\n\n{content}")


if today_tuple in birthdays_dict:
    send_mail()
