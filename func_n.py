def open_browser(browser_name):
    print_func_name(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
    print_func_name(go_to_companyname_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    print_func_name(find_registration_button_on_login_page, page_url, button_text)

def print_func_name(func_n, *args):
    func_n = func_n.__name__.capitalize().replace("_", " ")
    print(func_n, *args)

open_browser("Chrome")
go_to_companyname_homepage("https://www.nalog.gov.ru/")
find_registration_button_on_login_page("https://www.nalog.gov.ru/", "Деятельность")