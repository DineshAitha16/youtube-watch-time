import pytest
import re


def test_regex():
    text = '{"webCommandMetadata":{"url":"/watch?v=huCBKiLTmXs\u0026list=PLVm-0YZ5lwzk1ZhtJgmHpdSIYSKsTkQ3D\u0026index=1\u0026pp=iAQB","webPageType":"WEB_PAGE_TYPE_WATCH","rootVe":3832}}'
    pattern = r'"/watch\?v=.*?list=.*?&index=.*?&pp=.*?"'
    match = re.search(pattern, text)
    url = match.group().strip('"')
    assert url == '/watch?v=huCBKiLTmXs&list=PLVm-0YZ5lwzk1ZhtJgmHpdSIYSKsTkQ3D&index=1&pp=iAQB'


