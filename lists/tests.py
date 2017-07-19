from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


# 1. 假設我的 context root 是 / ，我要測試我的 view function 能不能處理 / 
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # resolve 
        self.assertEqual(found.func, home_page)


# 2. 我的 view function 處理請求，並返回某個 http response? ( 即通過功能測試 )

    def test_home_page_returns_corrent_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
       