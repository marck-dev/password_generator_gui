# -*- coding: utf-8 -*-
import random
class generator:
    # dictionary for the characters
    __dicc__ = '@()*+qwertyuiopasdfghjklñzxcvbnm,.áéíóúÉÁÍÓÚ?_-1234567890QWERTYUIOPASDFGHJKLÑZXCVBNM'
    # constructor, we need the length of password
    def __init__(self, length):
        """
        create a generator object
        :param length: of the password
        """
        self._lenght = int(length)
        self._pass = ""
    # private method to generate random num between 48 and 122
    def __gen_random(self):
        # get one of the dictionary
        tmp = random.choice((self.__dicc__))
        return tmp

    def generate(self):
        """
        generate the password
        :return: self
        """
        for i in range(self._lenght):
            self._pass = self._pass + self.__gen_random()
        # builder pattern
        return self;

    def get_password(self):
        """

        :return: the password
        """
        return self._pass
