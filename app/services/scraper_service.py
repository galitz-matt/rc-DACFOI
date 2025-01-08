import typing
from app.services.scraper import BaseScraper
from app.utils.institution_utils import InstitutionUtils

class ScraperService:
    def __init__(self, scrapers: typing.List[BaseScraper]):
        self.scrapers = scrapers

    def get_department_info(self, department: str):
        """
        Returns scraped information about a department's faculty members as a Pandas DataFrame
        :param department: school department e.g. Biomedical Engineering (Dept of SEAS)
        :return: dataframe containing the faculty name, email address, about section, and SEAS website
        """
        people_url = InstitutionUtils.get_people_url_from_department(department)
        profile_endpoints = seas_scraper.get_profile_endpoints_from_people(people_url)
        school = InstitutionUtils.get_school_from_department(department)
        school_base_url = InstitutionUtils.get_school_base_url(school)


    def _select_scraper(self, department: str):



if __name__ == '__main__':
    from app.utils.http_client import HttpClient
    from app.services.scraper import SEASScraper
    seas_scraper = SEASScraper(http_client=HttpClient())
    scrapers = [seas_scraper]
    service = ScraperService(scrapers)
    print(service.get_department_info("Biomedical Engineering"))
