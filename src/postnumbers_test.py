# Kirjoita postinumerot-moduulin testit tähän tiedostoon
from postnumbers import get_postal_code


def test_find_single_code():
    assert get_postal_code('NIVELAX') == '25840'


def test_find_multiple_codes():
    assert get_postal_code(
        'PORVOO') == '06100, 06101, 06150, 06151, 06200, 06400, 06401, 06450, 06500'


def test_find_unknown_code():
    assert get_postal_code('Tukholma') == None


def test_name_with_gaps():
    assert get_postal_code('SMART POST') == get_postal_code('SMARTPOST')
