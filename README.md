# SplitPinyin

## 介绍

分割全拼拼音串，并列举所有可能性

练习小作品，demo级别代码，未优化

使用Python 3.10.2编写，理论兼容Python 3所有版本

## 用法

```python
import SplitPinyin

splitter = SplitPinyin.PinyinSplitter(consonants, vowels, syllables)
splitter.split("nihaoshijie")
```

| 必要参数         | 解释                 |
|--------------|--------------------|
| `consonants` | 数组，包含所有的辅音         |
| `vowels`     | 数组，包含所有的元音         |
| `syllables`  | 字典，包含所有的辅音和元音的可能组合 |

| 可选参数        | 解释                |
|-------------|-------------------|
| `delimiter` | 字符，分割出来的拼音所使用的分词符 |

## 其他

* 算法会枚举**所有**有效的拼音分割方式，所以有些不是很实用的结果也会出现
  * 例如 `nihaoshijie` 会被分割成以下四种情况
    ```plain
    nihaoshijie:
        ni'ha'o'shi'ji'e
        ni'ha'o'shi'jie
        ni'hao'shi'ji'e
        ni'hao'shi'jie
    ```
* 使用的数据分离成了JSON，可以用在其他语言里
