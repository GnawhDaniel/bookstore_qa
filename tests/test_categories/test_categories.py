import pytest
from playwright.sync_api import Page

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
            
            # Check if book belongs to proper category
            assert next_td.text_content().lower() == category.lower(), f"Category {next_td.text_content().lower()} does not match {category.lower()}" 
            
            page.go_back()

    @pytest.mark.parametrize("category", ["biography", "fiction", "mystery", "fantasy", "romance"])
    def test_category(self, category, page: Page):
        self.template(category, page)