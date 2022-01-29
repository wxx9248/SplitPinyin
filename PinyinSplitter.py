#!/usr/bin/env python3

# 拼音规则：
## 除了n，l行，其余韵母u，v合并为u；
## un和vn合并为un（同形合并：j、q、x行后读vn，但是写作un，而其他行本身就是un）
## ue和ve合并为ue（同声合并：不存在ue的读音，所有写作ue的都读作ve）


class PinyinSplitter:
    def __init__(self, consonants: list, vowels: list, syllables: dict, delimiter = '\''):
        self.consonants = consonants
        self.vowels = vowels
        self.syllables = syllables
        self.delimiter = delimiter

        # 辅音和元音的反向查找字典
        self.consonantReverse = {key: value for (value, key) in enumerate(self.consonants)}
        self.vowelReverse = {key: value for (value, key) in enumerate(self.vowels)}

        # 所有辅音的首字母集合
        self.consonantInitials = set([consonant[0] for consonant in self.consonants if len(consonant) > 0])

        # 所有元音的首字母集合
        self.vowelInitials = set([vowel[0] for vowel in self.vowels])

        # 最大元音长度
        self.maxVowelLength = max([len(vowel) for vowel in vowels])

    def split(self, s: str):
        # 游标初始化
        # start和end分别指向音节的开头和结尾，cut指向音节中元音的开头
        # 音节范围为：[start, end)，且start <= cut < end
        if s is None:
            return None
        if len(s) < 1:
            return [""]

        start = cut = 0

        if s[start] in self.consonantInitials:
            # 普通音节
            # 匹配辅音（贪婪）
            cut = start
            while cut < len(s) and s[cut] not in self.vowelInitials:
                if s[start:cut + 1] in self.consonants:
                    cut += 1
                else:
                    # 未检测到元音首字母，且此组合不属于辅音，非拼音
                    return []
        else:
            # 纯元音音节
            pass

        end = cut
        possibilities = []
        # 匹配元音（懒惰）
        while end <= len(s) and end - cut <= self.maxVowelLength:
            # 如果是元音
            if s[cut:end] in self.vowelReverse:
                # 如果整个音节是有效的拼音
                if self.syllables[self.consonantReverse[s[start:cut]]][self.vowelReverse[s[cut:end]]] > 0:
                    # 匹配后面的切片
                    result = self.split(s[end:])
                    for item in result:
                        if len(item) > 0:
                            # 去掉最后的分词符号
                            possibilities.append(s[start:end] + self.delimiter + item)
                        else:
                            possibilities.append(s[start:end])
            # 继续匹配
            end += 1

        return possibilities
