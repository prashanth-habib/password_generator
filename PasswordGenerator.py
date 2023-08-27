"""
This program contains the code to generate a password of given length of characters.
"""

import string
import random


class PasswdGenerator:
    passwd_length = 5

    def set_length(self, new_length):
        """
        This method stores the length of the password to be generated.
        :return: none
        """
        #pass_len = int(input("Enter the length of the password:"))
        self.passwd_length = new_length

    def generate_passwd(self):
        """
        This method generated the password with the given length.
        :return: password
        """
        passwd = ""
        #self.get_length()
        chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(
            string.punctuation)
        for i in range(0, self.passwd_length):
            passwd = passwd + str(chars[random.randrange(len(chars))])
        return passwd
