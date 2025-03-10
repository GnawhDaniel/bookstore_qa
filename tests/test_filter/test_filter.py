import pytest
from playwright.sync_api import Page

class TestCategories:
    def template(self, price, page: Page):
        # Ensure the page is fully loaded
        page.goto("https://bookcart.azurewebsites.net/")
        page.wait_for_load_state("networkidle")
        
        page.get_by_role("slider").fill(str(price))
        
        costs = page.get_by_role("paragraph").all()
        for cost in costs:
            cost = float(cost.text_content()[1:].replace(",",""))
            assert cost <= price, f"Price {cost} does not match true price: {price}"
    
    @pytest.mark.parametrize("price", list(range(111,8211,100)))
    def test_values(self, price, page: Page): 
        self.template(price, page)
    