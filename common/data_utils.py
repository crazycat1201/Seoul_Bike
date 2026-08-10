"""Small, dataset-agnostic helpers reused across datasets/*/*.ipynb.

Kept intentionally minimal: only functions that have already been needed by
two or more datasets belong here. One-off cleaning logic stays in the
notebook it belongs to.
"""
import pandas as pd

DEFAULT_ENCODINGS = ("utf-8", "utf-8-sig", "cp949", "euc-kr")


def read_csv_any_encoding(path, encodings=DEFAULT_ENCODINGS, **kwargs):
    """Read a CSV trying several Korean-locale encodings in order.

    Korean public-data CSVs are inconsistently saved as UTF-8, CP949, or
    EUC-KR depending on the tool that exported them. Raises the last
    error if none of the encodings work.
    """
    last_err = None
    for enc in encodings:
        try:
            return pd.read_csv(path, encoding=enc, **kwargs)
        except (UnicodeDecodeError, UnicodeError) as e:
            last_err = e
    raise last_err
