# Amazon Playwright Automation

## Project Overview

This project provides an automation suite using Playwright to test the Amazon website. The tests are written in Python using the **pytest** framework for structured test execution. The test cases are designed to cover key functionalities like selecting categories, searching for products, login, adding products to the cart, and logging out.

## Project Setup

### Prerequisites

Before you start, ensure you have the following installed:

* Python 3.x
* Playwright
* pytest

### Installing Dependencies

1. Clone the repository:

   ```bash
   git clone https://github.com/Tanim1993/amazon_playwright.git
   ```

2. Navigate to the project directory:

   ```bash
   cd amazon_playwright
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Installing Playwright Browsers

1. Playwright requires certain browsers to be installed. You can install them by running the following command:

   ```bash
   playwright install
   ```

## How to Run Tests

1. To run all tests, use the following command:

   ```bash
   pytest tests/test_amazon.py
   ```

2. For detailed logging, you can increase verbosity:

   ```bash
   pytest tests/test_amazon.py -v
   ```

### Test Cases Implemented

1. **Select Software Category**

   * Test case to verify if the 'Software' option is selected from the category dropdown.

2. **Search for Games**

   * Test case to search for products using the search input field.

3. **Login**

   * Tests for valid and invalid login attempts.

     * **Invalid login:** Test for incorrect credentials.
     * **Valid login:** Test for correct login credentials.

4. **Add Product to Cart**

   * Test case to add a specific product to the shopping cart using the direct URL.

5. **Validate Cart**

   * Verifies if the product added to the cart is reflected correctly.

6. **Logout**

   * Verifies if the user can log out of the application successfully.

### File Structure

```
├── pages/
│   └── amazon_home_page.py     # Contains the Page Object Model for Amazon homepage
├── tests/
│   └── test_amazon.py          # Test file containing all the test cases
├── requirements.txt            # Dependencies required for the project
└── confest.py                  # Test configuration file
```


