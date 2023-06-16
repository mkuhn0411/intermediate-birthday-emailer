import datetime as dt
import random
import pandas
import smtplib

current_date = (dt.datetime.now().month, dt.datetime.now().day)
birthdays_data = pandas.read_csv("birthdays.csv")
birthdays_dict = {birthday_row["name"]: (birthday_row["month"], birthday_row["day"]) for (index, birthday_row) in birthdays_data.iterrows()}
PLACEHOLDER = "[NAME]"


def send_email(name, email_content):
    my_email = "test@gmail.com"
    password = "SOMEPASSWORD"

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Happy Birthday {name}!! \n\n{email_content}",
        )


def create_message(name):
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as names_file:
        message_contents = names_file.read()
        updated_message = message_contents.replace(PLACEHOLDER, name)
        send_email(name, updated_message)

def run():
    current_birthdays = [person for person in birthdays_dict if birthdays_dict[person] == current_date]
    for name in current_birthdays:
        create_message(name)


run()
