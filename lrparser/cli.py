"""命令行入口：求值并打印 SLR 表信息。"""

import argparse
import sys

from .lr import LrError, build_table, evaluate


def build_parser():
    parser = argparse.ArgumentParser(prog="lr-parser", description="SLR(1) 表达式分析")
    parser.add_argument("--parse", help="表达式，例如 1+2*3")
    parser.add_argument("--table", action="store_true", help="构造并打印 SLR 表")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        if args.table:
            table = build_table()
            print("states=%d conflicts=%d" % (len(table["states"]), len(table["conflicts"])))
        if args.parse:
            print("value=%s" % evaluate(args.parse))
    except LrError as error:
        print("错误：%s" % error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
