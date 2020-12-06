import unittest

from messaging.email import Email


email_test_gmail = Email(
    email_adress="testgmail@gmail.com",
    email_content="Hello gmail! I have an offer for you.",
)
email_test_yandex = Email(
    email_adress="testyandex@yandex.ru",
    email_content='<img src="https://spam.org/pic1.png"/>',
)
email_test_mail = Email(
    email_adress="testmail@mail.ru",
    email_content='<img src="https://spam.org/pic1.gif"/',
)


class MailingTestStringMethods(unittest.TestCase):
    def test_gmail_domen(self):
        """
        Testing gmail domen
        """
        self.assertEqual(
            email_test_gmail.send(),
            """http://email-service/gmail/send/\n{'email': 'testgmail@gmail.com', 'content': 'Hello gmail!'}""",
        )

    def test_yandex_domen(self):
        """
        Testing yandex domen
        """
        self.assertEqual(
            email_test_yandex.send(),
            """http://email-service/yandex/send/\n{'email': 'testyandex@yandex.ru', 'content': '[https://spam.org/pic1.png]'}""",
        )

    def test_mail_domen(self):
        """
        Testing mail domen
        """
        self.assertEqual(
            email_test_mail.send(),
            """http://email-service/mail/send/\n{'email': 'testmail@mail.ru', 'content': '<img src="https://spam.org/pic1.png"/'}""",
        )


if __name__ == "__main__":
    unittest.main()
