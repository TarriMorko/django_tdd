from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page # home_page 函式，還沒寫 (TODO)


# 1. 假設我的 context root 是 / ，我要測試我的 view function 能不能處理 / 
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # resolve 
        self.assertEqual(found.func, home_page)


# 2. 我的 view function 處理請求，並返回某個 http response? ( 即通過功能測試 )

