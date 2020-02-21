class Decode:
    def __init__(self, input_str):
        self.__input_str = input_str
        self.__encoded_alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.__decoded_alphabet = list("'n,lpkjhtgfdvbre]o;iym[.u/" + '"N<LPKJHTGFDVBRE}O:IYM{>U?')

    def decode_input(self):
        input_new = '_'.join(self.__input_str) + '_'
        output = input_new

        for letter in self.__decoded_alphabet:
            index = self.__decoded_alphabet.index(letter)
            if letter in input_new:
                if self.__decoded_alphabet[index] + '_' in output:
                    output = output.replace(self.__decoded_alphabet[index] + '_', self.__encoded_alphabet[index])

        return output.replace('_', '')
