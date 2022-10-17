# -*- coding: utf-8 -*-
# @Time : 17-10-2022 20:01
# @Author : rohan
# @File : test_button_operation.py
import pytest
from operation.button_operation import LikeState, slap_many


def test_empty_operation():
    assert slap_many(LikeState.empty, '') is LikeState.empty


def test_one_operation():
    assert slap_many(LikeState.empty, 'l') is LikeState.liked
    assert slap_many(LikeState.empty, 'd') is LikeState.disliked


# def test_multi_operation():
#     assert slap_many(LikeState.empty, 'll') is LikeState.empty
#     assert slap_many(LikeState.empty, 'dd') is LikeState.empty
#     assert slap_many(LikeState.empty, 'ld') is LikeState.disliked
#     assert slap_many(LikeState.empty, 'dl') is LikeState.liked
#     assert slap_many(LikeState.empty, 'ddl') is LikeState.liked
#     assert slap_many(LikeState.empty, 'lldd') is LikeState.empty
#     assert slap_many(LikeState.empty, 'ldd') is LikeState.empty

@pytest.mark.parametrize("test_input,expected", [
    ('ll', LikeState.empty),
    ('dd', LikeState.empty),
    ('ld', LikeState.disliked),
    ('dl', LikeState.liked),
    ('ldd', LikeState.empty),
    ('lldd', LikeState.empty),
    ('ddl', LikeState.liked),
])
def test_multi_operation(test_input, expected):
    assert slap_many(LikeState.empty, test_input) is expected


@pytest.mark.skip(reason="regexes not implemented yet")
def test_regex_operation():
    assert slap_many(LikeState.empty, '[ld]*ddl') is LikeState.liked


# test which fails and dont want to fail the build stage
# This should not be used when your expecting an expection
@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


def test_invalid_operation():
    with pytest.raises(ValueError):
        slap_many(LikeState.empty, 'x')


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"


@pytest.mark.xfail
def test_db_slap(db_conn):
    db_conn.read_slaps()
    assert ...
