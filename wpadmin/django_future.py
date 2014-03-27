import re

from django.utils.datastructures import SortedDict
from django.utils.translation import check_for_language

language_code_prefix_re = re.compile(r'^/([\w-]+)(/|$)')


def get_supported_language_variant(lang_code, supported=None, strict=False):
    """
    Returns the language-code that's listed in supported languages, possibly
    selecting a more generic variant. Raises LookupError if nothing found.

    If `strict` is False (the default), the function will look for an alternative
    country-specific variant when the currently checked is not found.
    """
    if supported is None:
        from django.conf import settings
        supported = SortedDict(settings.LANGUAGES)
    if lang_code:
        # if fr-CA is not supported, try fr-ca; if that fails, fallback to fr.
        generic_lang_code = lang_code.split('-')[0]
        variants = (lang_code, lang_code.lower(), generic_lang_code,
                    generic_lang_code.lower())
        for code in variants:
            if code in supported and check_for_language(code):
                return code
        if not strict:
            # if fr-fr is not supported, try fr-ca.
            for supported_code in supported:
                if supported_code.startswith((generic_lang_code + '-',
                                              generic_lang_code.lower() + '-')):
                    return supported_code
    raise LookupError(lang_code)


def get_language_from_path(path, supported=None, strict=False):
    """
    Returns the language-code if there is a valid language-code
    found in the `path`.

    If `strict` is False (the default), the function will look for an alternative
    country-specific variant when the currently checked is not found.
    """
    if supported is None:
        from django.conf import settings
        supported = SortedDict(settings.LANGUAGES)
    regex_match = language_code_prefix_re.match(path)
    if not regex_match:
        return None
    lang_code = regex_match.group(1)
    try:
        return get_supported_language_variant(lang_code, supported, strict=strict)
    except LookupError:
        return None

