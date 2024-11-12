from pages.home_page import HomePage


def test_free_vpn_text(driver):
    vpn_text = "Free VPN – best free online VPN, fast and secure"
    home_page = HomePage(driver)
    home_page.goto_page()
    text_from_element = home_page.find_text_element()
    assert text_from_element == vpn_text
