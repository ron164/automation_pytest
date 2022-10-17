# -*- coding: utf-8 -*-
# @Time : 17-10-2022 23:34
# @Author : rohan
# @File : conftest.py
import pytest
import sys


@pytest.fixture
def capture_stdout(monkeypatch):  # monkeypatch is built-in fixture
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer


@pytest.fixture(scope="session")
def db_conn():
    db = ...
    url = ...
    with db.connect(url) as conn:  # connection will be torn down after all tests finish
        yield conn
