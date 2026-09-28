"""SLR(1) 分析表与表达式求值。"""

from .lr import LrError, build_table, evaluate

__all__ = ["LrError", "build_table", "evaluate"]
