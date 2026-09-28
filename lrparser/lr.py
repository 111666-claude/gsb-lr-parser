"""SLR(1) 分析表构造与表达式求值，只用标准库。

缺陷：build_table 还没实现；evaluate 用「从左到右直接算」的朴素求值，没有优先级。
"""


class LrError(ValueError):
    """输入不合法。缺陷：不带位置。"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


GRAMMAR = [
    ("E", ("E", "+", "T")),
    ("E", ("T",)),
    ("T", ("T", "*", "F")),
    ("T", ("F",)),
    ("F", ("(", "E", ")")),
    ("F", ("num",)),
]


def tokenize(text):
    """把表达式切成 token。"""
    tokens = []
    index = 0
    while index < len(text):
        char = text[index]
        if char.isspace():
            index += 1
            continue
        if char.isdigit():
            start = index
            while index < len(text) and text[index].isdigit():
                index += 1
            tokens.append(("num", int(text[start:index])))
            continue
        if char in "+*()":
            tokens.append((char, char))
            index += 1
            continue
        raise LrError("不认识的字符：%r" % char)
    return tokens


def build_table():
    """缺陷：SLR(1) 分析表还没实现。"""
    raise LrError("LR 分析表还没实现")


def _apply(total, operator, value):
    if operator == "+":
        return total + value
    return total * value


def evaluate(text):
    """求值。缺陷：从左到右直接算，先看到的先结合，等于没有优先级。"""
    tokens = tokenize(text)
    total = 0
    operator = "+"
    pending = None
    for kind, value in tokens:
        if kind in ("num", "(", ")"):
            if kind == "num":
                if pending is None:
                    pending = value
                else:
                    total = _apply(total, operator, pending)
                    pending = value
        else:
            if pending is not None:
                total = _apply(total, operator, pending)
                pending = None
            operator = kind
    if pending is not None:
        total = _apply(total, operator, pending)
    return total
