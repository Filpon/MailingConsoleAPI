from messaging.email import Email


if __name__ == "__main__":
    email = Email(
        email_adress="test1@mail.ru",
        email_content='<img src="https://spam.org/pic1.gif"/',
    )
    email.send()
