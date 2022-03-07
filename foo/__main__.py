import argparse
import logging
import sys

from . import count_foo
from ._gettext import _

logger = logging.getLogger(__name__)


def parse_args():
    """Parse passed arguments and return result"""
    parser = argparse.ArgumentParser(description=_("Foo counter"))
    parser.add_argument(
        "file",
        nargs=argparse.REMAINDER,
        help=_("Files to count foos in. Stdin is used if none is specified."),
    )
    return parser.parse_args()


def main():
    args = parse_args()

    cnt = 0
    if args.file:
        for path in args.file:
            with open(path, "r") as file:
                cnt += count_foo(file)
    else:
        cnt += count_foo(sys.stdin)

    print(cnt)


if __name__ == "__main__":
    main()
