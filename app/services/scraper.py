from app.utils.http_client import HttpClient
from app.utils.institution_utils import InstitutionUtils

import typing
import logging
from lxml import html

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CONTACT_BLOCK_NAME_A_TAG = '//a[contains(@class, "contact_block_name_link")]/@href'
EMAIL_A_TAG = "//a[contains(@class, 'people_meta_detail_info_link') and starts-with(@href, 'mailto:')]/@href"
NO_RESULTS_DIV = '//div[contains(@class, "results_message_inner typography") and contains(text(), "There are no results matching these criteria.")]'

class ProfileScraper:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def get_profile_endpoints_from_people_page(self, people_url: str) -> typing.List[str]:
        """
        Extracts faculty profile URLs from paginated department people pages.

        Args:
            people_url (str): The base URL of the department's people page.

        Returns:
            list: A list of profile URLs.
        """
        page_number = 0
        profile_urls = []
        MAX_PAGES = 100

        while page_number < MAX_PAGES:
            page_url = f"{people_url}&page={page_number}"
            logger.info(f"Processing page {page_number}: {page_url}")
            try:
                response = self.http_client.request('GET', page_url)
                tree = html.fromstring(response.content)
                no_results = tree.xpath(NO_RESULTS_DIV)
                if no_results:
                    logger.info(f"No results found for page {page_number}: {page_url}")
                    break
                links = tree.xpath(CONTACT_BLOCK_NAME_A_TAG)
                profile_urls.extend(links)
                page_number += 1
            except Exception as e:
                logger.error(f"Error processing page {page_number}: {e}")
                break
        return profile_urls