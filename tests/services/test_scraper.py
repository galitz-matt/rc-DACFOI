import unittest

from unittest.mock import MagicMock
from app.utils.http_client import HttpClient
from app.utils.institution_utils import InstitutionUtils
from app.services.scraper.seas_scraper import SEASScraper

class TestSEASScraper(unittest.TestCase):

    def setUp(self):
        self.mock_http_client = MagicMock(spec=HttpClient)
        self.scraper = SEASScraper(http_client=self.mock_http_client)
        InstitutionUtils.is_valid_url = MagicMock()

    def test_get_profile_endpoints_from_people_valid_response(self):
        InstitutionUtils.is_valid_url.return_value = True
        mock_html = """
        <div>
            <a class="contact_block_name_link" href="/profile/john-doe">John Doe</a>
            <a class="contact_block_name_link" href="/profile/jane-smith">Jane Smith</a>
        </div>
        """
        mock_response = MagicMock()
        mock_response.content = mock_html.encode('utf-8')
        self.mock_http_client.request.return_value = mock_response

        result = self.scraper.get_profile_endpoints_from_people("http://example.com/people", max_pages=1)
        self.assertEqual(result, ["/profile/john-doe", "/profile/jane-smith"])
