from .protocol import _decode


def _maybe_int(s):
    """
    >>> _maybe_int("abc")
    'abc'
    >>> _maybe_int("11")
    11
    >>> _maybe_int("0xa")
    10
    >>> _maybe_int("0xz")
    '0xz'
    """
    try:
        return int(s, 0)
    except:
        return s


def _parse(s):
    """
    Parse the telldus core json-like packet representation as a python dict
    This makes it easier to copy and adapt original test cases

    >>> d = _parse("class:command;protocol:arctech;model:codeswitch;house:A;"\
    "unit:1;method:turnoff;")
    >>> d ==  {'method': 'turnoff', 'house': 'A', 'protocol': 'arctech',\
    'class': 'command', 'unit': 1, 'model': 'codeswitch'}
    True
    """
    # make it deterministic (for testing)
    from collections import OrderedDict

    items = s.split(";")
    items = filter(len, items)  # remove empty
    items = [s.split(":") for s in items]
    items = dict(items)
    items = OrderedDict(sorted(items.items()))  # make it deterministic
    items = {k: _maybe_int(v) for k, v in items.items()}
    return items


def _assert_equal(template, packet):
    """
    Check for equality between decoded packet and template
    (both encoded as strings)
    """
    template = _parse(template)
    packet = _parse(packet)
    packet = _decode(**packet)
    assert template == packet


def test_protocols():
    """
    Test cases directly adapted from original sources
    """

    # https://github.com/telldus/telldus/blob/master/telldus-core/tests/service/ProtocolEverflourishTest.cpp

    _assert_equal("class:command;protocol:everflourish;model:selflearning;"
                  "house:4242;unit:3;method:turnon;",
                  "protocol:everflourish;data:0x424A6F;")

    _assert_equal("class:command;protocol:everflourish;model:selflearning;"
                  "house:5353;unit:4;method:turnoff;",
                  "protocol:everflourish;data:0x53A7E0;")

    # https://github.com/telldus/telldus/blob/master/telldus-core/tests/service/ProtocolNexaTest.cpp

    _assert_equal("class:command;protocol:arctech;model:codeswitch;house:A;"
                  "unit:1;method:turnon;",
                  "protocol:arctech;model:codeswitch;data:0xE00;")

    _assert_equal("class:command;protocol:arctech;model:codeswitch;house:A;"
                  "unit:1;method:turnoff;",
                  "protocol:arctech;model:codeswitch;data:0x600;")

    _assert_equal("class:command;protocol:arctech;model:selflearning;"
                  "house:1329110;unit:1;group:0;method:turnon;",
                  "protocol:arctech;model:selflearning;data:0x511F590;")

    _assert_equal("class:command;protocol:arctech;model:selflearning;"
                  "house:1329110;unit:1;group:0;method:turnoff;",
                  "protocol:arctech;model:selflearning;data:0x511F580;")

    # https://github.com/telldus/telldus/blob/master/telldus-core/tests/service/ProtocolSartanoTest.cpp

    _assert_equal("class:command;protocol:sartano;model:codeswitch;"
                  "code:0101010101;method:turnon;",
                  "protocol:arctech;model:codeswitch;data:0x955;")
