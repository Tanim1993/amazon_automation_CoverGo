from playwright.sync_api import Page

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        # Locators
        self.category_dropdown = page.locator('select#searchDropdownBox')
        self.search_input = page.locator("input#twotabsearchtextbox")
        self.search_button = page.locator("input#nav-search-submit-button")
        self.cart_link = page.get_by_role("link", name="Go to Cart")


    def select_software_category(self):
        self.category_dropdown.wait_for(state="visible")
        self.category_dropdown.select_option("search-alias=software-intl-ship")
        self.page.wait_for_timeout(2000)

    def search_for_term(self, term: str):
        self.search_input.fill(term)
        self.search_button.click()
        self.page.wait_for_timeout(3000)

    def login(self, email, password):
        self.page.goto("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0", wait_until="domcontentloaded")
        
        email_box = self.page.locator('input[name="email"]')
        email_box.wait_for(state="visible", timeout=10000)
        email_box.fill(email)

        self.page.get_by_role("button", name="Continue").click()


        password_box = self.page.locator('input[name="password"]')
        password_box.wait_for(state="visible", timeout=10000)
        password_box.fill(password)

        sign_in_btn = self.page.locator('input#signInSubmit')
        sign_in_btn.wait_for(state="visible", timeout=5000)
        sign_in_btn.click()

        self.page.wait_for_timeout(3000)

    def add_product_by_url(self, url: str):
        self.page.goto(url)
        self.page.wait_for_timeout(2000)
        self.page.get_by_title("Add to Shopping Cart").click()
        self.page.locator("#sw-gtc").get_by_role("link", name="Go to Cart").click()

    def go_to_cart(self):
        self.page.goto("https://www.amazon.com/cart")
        self.page.wait_for_timeout(2000)

    def logout(self):
        self.page.goto("https://www.amazon.com/")
        self.page.hover("#nav-link-accountList")
        self.page.get_by_role("link", name="Sign Out").click()
        self.page.wait_for_timeout(3000)



