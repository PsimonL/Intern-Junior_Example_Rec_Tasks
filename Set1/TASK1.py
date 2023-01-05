# import re
import numpy as np

def function(input_string):
    for each in input_string:
        if not each.isalpha():
            raise TypeError("Invalid input type! Every element should be letter.")
        if not each.islower():
            raise SyntaxError("Invalid input type! Every letter should be lowercased.")

    occurrancesDict = dict((x, input_string.count(x)) for x in set(input_string))
    conversionToList = [(key, value) for key, value in occurrancesDict.items()]
    sorted_list = sorted(conversionToList, key=lambda x: x[1], reverse=True)

    AllNOoccurences = [i[1] for i in sorted_list]

    NOsubdivisions = len(set(AllNOoccurences))
    NoDuplicates = np.unique(AllNOoccurences)
    ReversedOverallOccurencesByDivisions = NoDuplicates[::-1]

    SubdivisionsWithAllLetters = []
    for i in range(NOsubdivisions):
        helpArray = [item for item in sorted_list if ReversedOverallOccurencesByDivisions[i] in item]
        SubdivisionsWithAllLetters.append(helpArray)

    final_list = []
    for i in range(len(SubdivisionsWithAllLetters)):
        DividingIntoGroupsOfSorting = []
        for each in SubdivisionsWithAllLetters[i]:
            DividingIntoGroupsOfSorting.append(each[0])
        final_list.append(sorted(DividingIntoGroupsOfSorting))

    final_string = ""
    for each in final_list:
        final_string += ''.join(each)

    return ' '.join(final_string)


if __name__ == "__main__":
    # Comment for example below:
    # According to rules: 1. Most occurrences 2. Alphabetical order
    # The output should be: y z a o p b c d e
    # Because we got: 5*z, 5*y, 4*a, 3*o, 3*p, 2*b, 2*c, 1*d and 1*e
    # So: first we take most occurrences - 5 times, we got 2 letters, so we use 2. rule and it goes: y z
    # then we take "a" which is single 4 time occurrence so: y z a
    # then we got 3 times "o" and "p" so we use alphabetical order and got: y z a o p so on and so on...
    getResult = function("zzzzzyyyyyaaaapppooobbccde")
    print(f"Final result: {getResult}")
