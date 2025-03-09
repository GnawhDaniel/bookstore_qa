import pytest
from playwright.sync_api import Page, expect

class TestCategories:
    def template(self, category, page: Page):
        # Ensure the page is fully loaded
        page.goto(f"/filter?category={category}")
        
        # The first two mat-card-content are in price filter element
        res = page.locator("mat-card-content").all()    
        for link in res[2:]:
            # Visit link
            path = link.get_by_role("link").get_attribute("href")
            link.get_by_role("link").click()
            page.wait_for_url(f"**{path}")

            # Get Category
            next_td = page.get_by_role("cell", name="Category").locator("xpath=following-sibling::td[1]")
            # print(next_td.text_content())
            assert next_td.text_content().lower() == category.lower(), f"Category {next_td.text_content().lower()} does not match {category.lower()}" 
            
            page.go_back()

    def test_biography(self, page: Page):
        self.template("biography", page)
        
    def test_fiction(self, page: Page):
        self.template("fiction", page)
        
    def test_mystery(self, page: Page):
        self.template("mystery", page)
        
    def test_fantasy(self, page: Page):
        self.template("fantasy", page)
        
    def test_romance(self, page: Page):
        self.template("romance", page)