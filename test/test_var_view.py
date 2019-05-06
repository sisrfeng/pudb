# -*- coding: utf-8 -*-
from pudb.py3compat import text_type


class A:
    pass


class A2(object):
    pass


def test_get_stringifier():
    from pudb.var_view import InspectInfo, get_stringifier

    for value in [
            A, A2, A(), A2(), u"lól".encode('utf8'), u"lól",
            1233123, [u"lól".encode('utf8'), u"lól"]
            ]:
        for display_type in ["type", "repr", "str"]:
            iinfo = InspectInfo()
            iinfo.display_type = display_type

            strifier = get_stringifier(iinfo)

            s = strifier(value)
            assert isinstance(s, text_type)
