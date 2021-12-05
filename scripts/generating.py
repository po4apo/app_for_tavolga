from random import randint, shuffle

class PasswordGenerator:
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_symbols = "!#$%&*+-.;?^_~"
    digits = "0123456789"

    def __init__(self) -> None:
        pass

    
    def __get_random_chars(self, from_str, count):
        
        result = list()
        for _ in range(count):
            ind = randint(0, len(from_str) - 1)
            result.append(from_str[ind])
        return result


    def generate_passphrase(self):
        di_count = randint(2, 4)
        cl_count = randint(2, 4)
        ss_count = randint(2, 4)
        sl_count = 16 - di_count - cl_count - ss_count
        passphrase = list()
        passphrase = passphrase + self.__get_random_chars(self.digits, di_count)
        passphrase = passphrase + self.__get_random_chars(self.special_symbols, ss_count)
        passphrase = passphrase + self.__get_random_chars(self.capital_letters, cl_count)
        passphrase = passphrase + self.__get_random_chars(self.small_letters, sl_count)
        shuffle(passphrase)
        return "".join(passphrase)
