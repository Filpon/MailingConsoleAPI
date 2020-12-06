class Email:
    """
    Class for mail adresses console typing
    """

    def __init__(self, email_adress: str, email_content: str):
        self.json_content = {"email": email_adress, "content": email_content}
        self.punctuation_marks_list_gmail = {". ", "? ", "! "}  # These are marks of sentences ending if gmail domen
        self.replace_rules_yandex = {'<img src="': "[", '"/>': "]"}  # What replace to what if yandex domen
        self.replace_rules_mail = {".gif": ".png"}  # What replace to what if mail if mail domen

    def gmail_correction(self):
        """
        Correction mailing for gmail domen connection
        """
        if (
            len(self.json_content["content"]) == 0
            or type(self.json_content["content"]) is int
            or self.json_content["content"] is None
        ):
            """Nothing to do with such case"""
        elif (
            len(self.json_content["content"]) != 0
            and self.json_content["content"] is not None
        ):
            for punctuation_mark in self.punctuation_marks_list_gmail:
                if punctuation_mark in self.json_content["content"]:
                    try:
                        sentences = self.json_content["content"].split(punctuation_mark)
                        new_sentences = [
                            sentence
                            for sentence in sentences
                            if "offer" not in sentence
                            and not any(
                                p_mark in self.punctuation_marks_list_gmail
                                for p_mark in sentence.split()
                            )
                        ]
                        if len(new_sentences) == 1:
                            self.json_content["content"] = (str(new_sentences[0]) + punctuation_mark).rstrip()
                        else:
                            self.json_content["content"] = f"{punctuation_mark}".join(new_sentences)
                    except Exception:
                        print("Some error with list comprehension")
        else:
            raise Exception("Email gmail_correction method error")

    def yandex_and_mail_correction(self):
        """
        Correction mailing for yandex and domen connection
        """
        if (
            len(self.json_content["content"]) == 0
            or type(self.json_content["content"]) is int
            or self.json_content["content"] is None
        ):
            """Nothing to do with such case"""
        elif (
            len(self.json_content["content"]) != 0
            and self.json_content["content"] is not None
        ):
            # Example <img src="https://spam.org/pic1.png"/> в [https://spam.org/pic1.png]""" for yandex domen
            # Example < img src = "https://spam.org/pic1.gif"/> в < img src="https://spam.org/pic1.png"/> for mail domen
            try:
                replacing_rules = (
                    self.replace_rules_yandex
                    if "@yandex" in self.json_content["email"]
                    else (
                        self.replace_rules_mail
                        if "@mail" in self.json_content["email"]
                        else {}
                    )
                )
                for replace_rule in replacing_rules:
                    self.json_content["content"] = self.json_content[
                        "content"
                    ].replace(
                        replace_rule, replacing_rules.get(replace_rule, "")
                    )
            except TypeError:
                print("Exception occured with domen type, replacing is not applied")
        else:
            raise Exception("Email yandex_and_mail_correction method error")

    def send(self):
        """
        Sending mail code
        """
        if "@gmail" in self.json_content["email"]:
            self.gmail_correction()
        elif (
            "@yandex" in self.json_content["email"]
            or "@mail" in self.json_content["email"]
        ):
            self.yandex_and_mail_correction()
        else:
            raise Exception("Unknown email-domen")

        print(
            f"http://email-service/{self.json_content['email'].split('@')[1].split('.')[0]}/send/\n{self.json_content}"
        )

        return f"http://email-service/{self.json_content['email'].split('@')[1].split('.')[0]}/send/\n{self.json_content}"
