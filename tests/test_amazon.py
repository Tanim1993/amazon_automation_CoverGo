import pytest
from pages.amazon_home_page import HomePage

def test_full_amazon_flow(browser):
    home = HomePage(browser)

    # TC1 - Select Software
    home.select_software_category()
    assert home.category_dropdown.input_value() == "search-alias=software-intl-ship"

    # TC2 - Search for games
    home.search_for_term("games")
    assert "games" in browser.url or browser.title()

    # TC3 - Login (if you can bypass CAPTCHA manually)
    home.login("khaledtanim22@gmail.com", "T@nim1993")

    # TC4 - Add product to cart via direct URL
    product_url = "https://www.amazon.com/Hasbro-Gaming-Hardwood-Stacking-Stuffers/dp/B00ABA0ZOA/"
    home.add_product_by_url(product_url)

    # TC5 - Validate cart
    home.go_to_cart()
    assert "cart" in browser.url

    # TC6 - Logout
    home.logout()
    assert "signin" in browser.url or "logout" in browser.url