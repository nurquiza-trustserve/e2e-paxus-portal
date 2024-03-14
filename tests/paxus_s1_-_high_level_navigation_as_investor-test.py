import os
from playwright.sync_api import sync_playwright

# Check if all environment variables are set
required_env_vars = ['E2E_URL', 'E2E_USER', 'E2E_PASSWORD']
for env_var in required_env_vars:
    if not os.getenv(env_var):
        raise ValueError(f"Environment variable '{env_var}' is not set.")

# Go to the app landing view specified in environment variable E2E_URL
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    e2e_url = os.getenv('E2E_URL')
    page.goto(e2e_url)

    # Login with E2E_USER in input.name="username"], E2E_PASSWORD in input.name=”password"
    e2e_user = os.getenv('E2E_USER')
    e2e_password = os.getenv('E2E_PASSWORD')
    page.fill('input[name="username"]', e2e_user)
    page.fill('input[name="password"]', e2e_password)
    page.click('button[type="submit"]')

    # Go to ${E2E_URL}/transactions
    page.goto(f"{e2e_url}/transactions")

    # Assert that the h1 tag has the text “Transactions”
    assert page.inner_text('h1') == "Transactions", "Transactions page title assertion failed"

    # Go to ${E2E_URL}/dashboard
    page.goto(f"{e2e_url}/dashboard")

    # Assert that the h1 tag has the text “Dashboard”
    assert page.inner_text('h1') == "Dashboard", "Dashboard page title assertion failed"

    # Go to ${E2E_URL}/holdings
    page.goto(f"{e2e_url}/holdings")

    # Assert that the h1 tag has the text “Holdings”
    assert page.inner_text('h1') == "Holdings", "Holdings page title assertion failed"

    # Go to ${E2E_URL}/documents
    page.goto(f"{e2e_url}/documents")

    # Assert that the h1 tag has the text “Documents”
    assert page.inner_text('h1') == "Documents", "Documents page title assertion failed"

    browser.close()

