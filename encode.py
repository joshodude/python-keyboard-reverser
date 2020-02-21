class Encode:
    def __init__(self, input_str):
        self.__input_str = input_str
        self.__encoded_alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.__decoded_alphabet = list("'n,lpkjhtgfdvbre]o;iym[.u/" + '"N<LPKJHTGFDVBRE}O:IYM{>U?')

    def encode_input(self):
        input_new = '_'.join(self.__input_str) + '_'
        output = input_new

        for letter in self.__encoded_alphabet:
            index = self.__encoded_alphabet.index(letter)
            if letter in input_new:
                if self.__encoded_alphabet[index] + '_' in output:
                    output = output.replace(self.__encoded_alphabet[index] + '_', self.__decoded_alphabet[index])

        return output.replace('_', '')
