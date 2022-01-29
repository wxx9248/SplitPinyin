import json
import sys

import PinyinSplitter


def testSplitter(splitter: PinyinSplitter, testCases: list):
    for testCase in testCases:
        print("{input}:".format(input = testCase))
        for output in splitter.split(testCase):
            print("\t{output}".format(output = output))
        print()


def main(argv: list):
    consonants = json.load(open("Consonants.json"))
    vowels = json.load(open("Vowels.json"))
    syllables = json.load(open("Syllables.json"))

    splitter = PinyinSplitter.PinyinSplitter(consonants, vowels, syllables)
    testCasesLegal = ["nihaoshijie", "chiputaobutuputaopi", 'buchiputaodaotuputaopi',
                      'zhehenangzang', "shuangliujichang", "xianganwushi",
                      "biangbiangmian"]
    testCasesIllegal = ['tsinghua', 'bokchoy', "xxxxxxxxxx", "wwwwwwww", "wxx9248"]
    testSplitter(splitter, testCasesLegal + testCasesIllegal)


if __name__ == "__main__":
    main(sys.argv)
