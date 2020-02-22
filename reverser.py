class Reverse:
    def __init__(self, input_str):
        self.__input_str = input_str
        self.__alphabet = list("qwertyuiop[]asdfghjkl;'zxcvbnm,./" + 'QWERTYUIOP{}ASDFGHJKL:ZXCVBNM<>?')
        self.__reversed_alphabet = list("][poiuytrewq';lkjhgfdsa/.,mnbvcxz" + '}{POIUYTREWQ":LKJHGFDSA?><MNBVCXZ')

    def reverse_input(self):
        input_new = '_'.join(self.__input_str) + '_'
        output = input_new

        for letter in self.__alphabet:
            index = self.__alphabet.index(letter)
            if letter in input_new:
                if self.__alphabet[index] + '_' in output:
                    output = output.replace(self.__alphabet[index] + '_', self.__reversed_alphabet[index])

        return output.replace('_', '')
