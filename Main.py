import typing
import time
import re
import math


class BLOSUM:
    statusCount = {
        "A": 0,
        "R": 0,
        "N": 0,
        "D": 0,
        "C": 0,
        "Q": 0,
        "E": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "L": 0,
        "K": 0,
        "M": 0,
        "F": 0,
        "P": 0,
        "S": 0,
        "T": 0,
        "W": 0,
        "Y": 0,
        "V": 0,
    }

    def count(self, amino_acids):
        for each_amino_acids in amino_acids:
            for each_character in each_amino_acids:
                if each_character == 'A' or each_character == 'a':
                    self.statusCount['A'] += 1
                elif each_character == 'R' or each_character == 'r':
                    self.statusCount['R'] += 1
                elif each_character == 'N' or each_character == 'n':
                    self.statusCount['N'] += 1
                elif each_character == "D" or each_character == 'd':
                    self.statusCount['D'] += 1
                elif each_character == 'C' or each_character == 'c':
                    self.statusCount['C'] += 1
                elif each_character == 'Q' or each_character == 'q':
                    self.statusCount['Q'] += 1
                elif each_character == 'E' or each_character == 'e':
                    self.statusCount['E'] += 1
                elif each_character == 'G' or each_character == 'g':
                    self.statusCount['G'] += 1
                elif each_character == 'H' or each_character == 'h':
                    self.statusCount['H'] += 1
                elif each_character == 'I' or each_character == 'i':
                    self.statusCount['I'] += 1
                elif each_character == 'L' or each_character == 'l':
                    self.statusCount['L'] += 1
                elif each_character == 'K' or each_character == 'k':
                    self.statusCount['K'] += 1
                elif each_character == 'M' or each_character == 'm':
                    self.statusCount['M'] += 1
                elif each_character == 'F' or each_character == 'f':
                    self.statusCount['F'] += 1
                elif each_character == 'P' or each_character == 'p':
                    self.statusCount['P'] += 1
                elif each_character == 'S' or each_character == 's':
                    self.statusCount['S'] += 1
                elif each_character == 'T' or each_character == 't':
                    self.statusCount['T'] += 1
                elif each_character == 'W' or each_character == 'w':
                    self.statusCount['W'] += 1
                elif each_character == 'Y' or each_character == 'y':
                    self.statusCount['Y'] += 1
                elif each_character == 'V' or each_character == 'v':
                    self.statusCount['V'] += 1
        return self.statusCount

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def permuation(self, n, m):
        result = (self.factorial(m) / (self.factorial(m - n) * self.factorial(n)))
        return result

    def multiplyPermutationToSequenceLength(self, permuation_number, length):
        return permuation_number * length

    def form(self):
        index_update = 0
        alphabets = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
        length = len(alphabets)

        all_states = []
        for character_index, characters in enumerate(alphabets):
            all_states.append(characters + "->" + characters)
            index_update += 1
            for inner_index in range(index_update, length):
                all_states.append(characters + "->" + alphabets[inner_index])

        return all_states

    def createColumns(self, sequences, states):
        permission = True
        counter = 0
        get_alphabet_in_column_format = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "",
                                         11: "", 12: "", 13: "", 14: "", 15: "", 16: "", 17: "", 18: "", 19: "", }
        for each_sequence in sequences:
            for char_index, chars in enumerate(each_sequence):
                get_alphabet_in_column_format[char_index] += chars

        return get_alphabet_in_column_format

        # for times in range(0, 20):
        #     for index, value in enumerate(sequences): # array
        #         for inner_index, char in enumerate(value): # character
        #             if counter == index:
        #                 create_string += char
        #                 if  index == len(sequences) - 1:
        #                     get_alphabet_in_column_format.append(create_string)
        #
        #
        #                 break
        #     counter += 1
        # print(get_alphabet_in_column_format)

    def allColumnPosibilities(self, dictionary):
        # for key , value in dictionary.items()
        counter = 0
        pairs = []
        for keys in dictionary:
            temp = dictionary[keys]
            counter = 0
            for i in range(0, len(temp)):
                counter += 1
                for j in range(counter, len(temp)):
                    pairs.append(temp[i] + '->' + temp[j])
                    pairs.append(temp[j] + '->' + temp[i])
                    # print(i)

        return pairs

    def observedProportion(self, all_states, all_column_possibility, denominator):
        print(denominator)
        for keys in all_states:
            for each_possible_sequence in all_column_possibility:
                if keys == each_possible_sequence:
                    all_states[keys] += 1

        for keys in all_states:
            all_states[keys] = all_states[keys] / denominator

        print(all_states)
        return all_states

    def expectedPortion(self, all_states, all_single_possibilities, ds: dict):
        ds_copy = ds.copy()
        counter = 0
        permission = False
        temp = []
        result = 0
        for keys in all_single_possibilities:
            result = result + all_single_possibilities[keys]
        # print(result)

        for keys in all_single_possibilities:
            all_single_possibilities[keys] /= result

        print(all_single_possibilities)

        for values in all_states:
            for chars in values:
                if chars == "A":
                    counter += 1
                    temp.append(chars)
                elif chars == "R":
                    counter += 1
                    temp.append(chars)
                elif chars == "N":
                    counter += 1
                    temp.append(chars)
                elif chars == "D":
                    counter += 1
                    temp.append(chars)
                elif chars == "C":
                    counter += 1
                    temp.append(chars)
                elif chars == "Q":
                    counter += 1
                    temp.append(chars)
                elif chars == "E":
                    counter += 1
                    temp.append(chars)
                elif chars == "G":
                    counter += 1
                    temp.append(chars)
                elif chars == "H":
                    counter += 1
                    temp.append(chars)
                elif chars == "I":
                    counter += 1
                    temp.append(chars)
                elif chars == "L":
                    counter += 1
                    temp.append(chars)
                elif chars == "K":
                    counter += 1
                    temp.append(chars)
                elif chars == "M":
                    counter += 1
                    temp.append(chars)
                elif chars == "F":
                    counter += 1
                    temp.append(chars)
                elif chars == "P":
                    counter += 1
                    temp.append(chars)
                elif chars == "S":
                    counter += 1
                    temp.append(chars)
                elif chars == "T":
                    counter += 1
                    temp.append(chars)
                elif chars == "W":
                    counter += 1
                    temp.append(chars)
                elif chars == "Y":
                    counter += 1
                    temp.append(chars)
                elif chars == "V":
                    counter += 1
                    temp.append(chars)

                if counter % 2 == 0:
                    permission = True
                else:
                    permission = False

                if permission:
                    amino_acid1 = temp[0]
                    amino_acid2 = temp[1]
                    # TODO be careful
                    temp = []

                    num1 = all_single_possibilities[amino_acid1]
                    num2 = all_single_possibilities[amino_acid2]
                    final = num1 * num2
                    ds_copy[amino_acid1 + "->" + amino_acid2] = final

        print(ds_copy)

        return ds_copy

    def logCalculation(self, observed_proportion, expected_proportion):
        final_score = observed_proportion.copy()
        for keys in observed_proportion:
            val = observed_proportion[keys] / expected_proportion[keys]
            # print(val)

            if val != 0:
                val = math.log2(val)
            else:
                pass

            val = 2 * val
            final_score[keys] = val

        return final_score

    def roundScores(self, final_score):
        print(final_score)
        for keys in final_score:
            final_score[keys] = round(final_score[keys])

        return final_score


if __name__ == '__main__':
    sample = ['MCKAGFAGDDAPRAVFPSIV',
              'GRPRHQGIMVGMGQKDSYVG',
              'DEAQSKRGILTLRYPIEHGI',
              'VTNWDDMEKIWHHTFYNELR',
              'VAPEEHPVLLTEAPMNPKSN',
              'TSSQSSAIEKSYELPDGQVI']

    blosum = BLOSUM()
    # calculate each single amino acid
    status = blosum.count(sample)
    # forming all possible pairs with 20 amino acid for example A->A
    states = blosum.form()

    zeros = []
    for i in range(0, len(states)):
        zeros.append(0)
    permutation_result = blosum.permuation(2, 6)
    length = 20
    denominator = blosum.multiplyPermutationToSequenceLength(permutation_result, length)
    # Covert list to dictioanry
    state_dictionary = dict(zip(states, zeros))
    # returning each column in matrix
    each_column = blosum.createColumns(sample, state_dictionary)
    # returning each possible solution that can be made in each column of matrix
    all_possible_solution = blosum.allColumnPosibilities(each_column)
    # calculating probability or observed proportion
    observed_proportion = blosum.observedProportion(state_dictionary, all_possible_solution, denominator)

    ''' Note  '''
    # states = list of possible pairs
    # status = possibility of each amino acid
    # state_dictionary = dictionary that has all pair possibilities of amino acids
    expected_proportion = blosum.expectedPortion(states, status, state_dictionary)
    final_score = blosum.logCalculation(observed_proportion, expected_proportion)

    rounded_final_score = blosum.roundScores(final_score)
    print(rounded_final_score)





    # print(state_dictionary)
    # [print(x) for x in range(10)]
