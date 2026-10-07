from validators import is_valid_password, is_adult


def test_password_min_boundary():
    assert is_valid_password("abcdefgh") is True


def test_password_below_min():
    assert is_valid_password("abcdefg") is False


def test_age_boundary():
    assert is_adult(18) is True
    assert is_adult(17) is False

def test_password_max_boundary():
    assert is_valid_password("abcdefghijkl") is True

def test_password_above_max():
    assert is_valid_password("abcdefghijklm") is False