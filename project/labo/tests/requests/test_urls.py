from django.urls import reverse, resolve


class TestUrls:
    
    def test_labo_index_urls(self):
        path = reverse('labo:index')
        assert resolve(path)
        
    def test_labo_detail_urls(self):
        path = reverse('labo:detail', kwargs={'item_id': 1})
        assert resolve(path)
        
    def test_labo_user_edit_urls(self):
        path = reverse('labo:user_edit')
        assert resolve(path)
        
    def test_labo_item_edit_urls(self):
        path = reverse('labo:item_edit')
        assert resolve(path)