"""
Internal utils
"""
import django


def add_media(dest, media):
    """
    Optimized version of django.forms.Media.__add__() that doesn't create new objects.

    Only required for Django < 2.0
    """
    if django.VERSION >= (2, 0):
        combined = dest + media
        dest._css_lists = combined._css_lists
        dest._js_lists = combined._js_lists
    else:
        dest.add_css(media._css)
        dest.add_js(media._js)
