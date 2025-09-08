import unicodedata


def strip_accents(unicode_string):
    """
    Strip accents (all combining unicode characters) from a unicode string.
    """
    ndf_string = unicodedata.normalize('NFD', unicode_string)
    is_not_accent = lambda char: unicodedata.category(char) != 'Mn'
    return ''.join(
        char for char in ndf_string if is_not_accent(char)
    )