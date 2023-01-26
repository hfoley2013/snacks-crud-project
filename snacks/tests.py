from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class Test(TestCase):
    def test_home_page_status_code(self):
        url = reverse('snack_list')
        print(f'the url is: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_create_template(self):
        url = reverse('snack_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_create.html')
        self.assertTemplateUsed(response, 'base.html')
