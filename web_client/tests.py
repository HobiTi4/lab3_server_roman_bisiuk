from django.test import TestCase, RequestFactory
from django.urls import reverse
from unittest.mock import patch, MagicMock
from types import SimpleNamespace


class CharacterUnitTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    @patch('web_client.views.Character.objects.all')
    def test_list_view_mocks_db(self, mock_all):
        fake_char = SimpleNamespace()
        fake_char.name = "MockedHero"
        fake_char.level = 99
        fake_char.character_id = 1

        mock_all.return_value = [fake_char]

        response = self.client.get(reverse('character_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MockedHero")
        mock_all.assert_called_once()

    @patch('web_client.views.get_object_or_404')
    def test_detail_view_mocks_db(self, mock_get_object):
        fake_char = SimpleNamespace()
        fake_char.character_id = 1
        fake_char.name = "Arthas"
        fake_char.level = 80
        fake_char.guild = None

        mock_get_object.return_value = fake_char

        response = self.client.get(reverse('character_detail', args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Arthas")
        self.assertTemplateUsed(response, 'web_client/character_detail.html')

    @patch('web_client.views.CharacterForm')
    def test_create_view_post_mocks_save(self, MockForm):

        mock_form_instance = MockForm.return_value
        mock_form_instance.is_valid.return_value = True

        response = self.client.post(reverse('character_create'), {'name': 'NewGuy'})

        mock_form_instance.save.assert_called_once()
        self.assertEqual(response.status_code, 302)

    @patch('web_client.views.get_object_or_404')
    def test_delete_view_mocks_db(self, mock_get_object):

        fake_char = MagicMock()
        mock_get_object.return_value = fake_char

        response = self.client.post(reverse('character_delete', args=[1]))
        fake_char.delete.assert_called_once()
        self.assertEqual(response.status_code, 302)

@patch('web_client.views.helper')
class ExternalAPITests(TestCase):

    def test_external_list_view_calls_helper(self, mock_helper):
        fake_data = [{'client_id': 1, 'name': 'Mocked Client'}]
        mock_helper.get_list.return_value = fake_data

        response = self.client.get(reverse('external_clients_list'))

        self.assertEqual(response.status_code, 200)
        mock_helper.get_list.assert_called_once_with('clients')
        self.assertContains(response, 'Mocked Client')

    def test_external_delete_view_calls_helper(self, mock_helper):
        mock_helper.delete_item.return_value = True
        response = self.client.post(reverse('external_clients_list'), {'item_id': '1'})

        mock_helper.delete_item.assert_called_once_with('clients', '1')
        self.assertRedirects(response, reverse('external_clients_list'))