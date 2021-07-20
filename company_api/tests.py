from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CompanyProfileTests(APITestCase):

    databases = {'companies_db'}

    def test_view_company_profile_list(self):
        url = reverse('company_api:company-profile-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_company_profile(self):
        url = reverse('company_api:company-profile', kwargs={'pk': 'non-existent-company'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_view_company_quote(self):
        url = reverse('company_api:company-quote', kwargs={'pk': 'non-existent-company'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_view_company_trading_list(self):
        url = reverse('company_api:company-trading-list', kwargs={'pk': 'non-existent-company'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_company_adtv_list(self):
        url = reverse('company_api:company-adtv-list', kwargs={'pk': 'non-existent-company'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_company_adtv_quote(self):
        url = reverse('company_api:company-adtv-quote', kwargs={'pk': 'non-existent-company'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_company_trading_quote(self):
        url = reverse('company_api:company-trading-quote', kwargs={'pk': 'non-existent-company'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_company_list(self):
        url = reverse('company_api:company-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_fmp_list(self):
        url = reverse('company_api:fmp-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_iex_list(self):
        url = reverse('company_api:iex-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_company_quote_full(self):
        url = reverse('company_api:company-quote-full', kwargs={'ticker': 'non-existent-company'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_add_on(self):
        url = reverse('company_api:add-on')
        # data = {
        #     "company_ticker": "testing_company_ticker",
        #     "company_name": "testing_company_name"
        # }
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
