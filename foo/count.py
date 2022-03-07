# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright 2022, CZ.NIC z.s.p.o. (http://www.nic.cz/)
"""The 'foo' counting module."""
import io


def count_foo(file: io.TextIOBase) -> int:
    """Count number of lines starting with 'foo:'."""
    return sum(1 if line.startswith("foo:") else 0 for line in file)
