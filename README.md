# lr-parser

SLR(1) 分析表构造与表达式求值，只用 Python 标准库。

```
python3 -m lrparser.cli --parse '1+2*3'
python3 -m lrparser.cli --table
python3 -m unittest discover -s tests -v
```

## 口径（README 为准）

- **分析表要真的构造**：对内置表达式文法算出 FIRST / FOLLOW、LR(0) 项目集规范族（闭包要递归展开到不再新增）、
  goto 表与 ACTION 表；`--table` 现在直接报「LR 分析表还没实现」，按口径要给 `states=` 与 `conflicts=0`
  （这个文法本身无冲突，有冲突必须列出来）。
- **求值要按优先级**：`--parse '1+2*3'` 按口径是 7（先乘后加），现在从左到右直接算给 9；
  `--parse '(1+2)*3'` 是 9；`--parse '2*3+4*5'` 是 26。
- FOLLOW 要迭代到不动点：末尾非终结符加 `$`；`A -> a B b` 时 FIRST(b) 里非空的都进 FOLLOW(B)，
  b 可空时继续把 FOLLOW(A) 并进去。
- 错误处理：非法 token、括号不配对、多余运算符要报错并给出 token 位置；空表达式按 0 处理。
- 不变量：`evaluate(t)` 与「按 SLR 表逐步规约」的结果一致；同一表达式重复求值结果相同；`--trace` 能打印规约序列。
- 规模：10^4 个 token 的表达式 1 秒内解析完，内存 O(状态数 + token 数)。

## 现在的行为

- `build_table` 直接抛 `LrError("LR 分析表还没实现")`。
- `evaluate` 是从左到右的朴素累加：`1+2*3` 给 9（正确 7），括号也只是被跳过。
- `tokenize` 是对的（数字、`+`、`*`、括号）。

## 计划新增的能力

```
--parse 表达式
--table          打印 SLR 表
--trace          打印规约序列
```

## 输出

```
states=12 conflicts=0
value=7
```

## 目录

```
lrparser/lr.py    词法、FIRST/FOLLOW、项目集与求值
lrparser/cli.py   命令行入口
tests/            unittest 用例
```
