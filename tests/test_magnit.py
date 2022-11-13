import pytest

from pages.cart_page import CartPage
from pages.feedback_page import FeedbackPage
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
import allure


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Информация о компании'")
def test_link_company_info(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()

    home_page.click_company_info_link()
    home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/about-magnit/")


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Контакты'")
def test_link_contacts(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()

    home_page.click_contacts_link()
    home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/contacts/")


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Обратная связь'")
def test_link_feedback(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()

    home_page.click_feedback_link()
    home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/feedback/")


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Как сделать заказ'")
def test_link_how_to_order(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()

    home_page.click_how_to_order_link()
    home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/how_to_order")


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Как сделать заказ'")
def test_link_payment(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()

    home_page.click_payment_link()
    home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/payment")


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Возврат товара'")
def test_link_return(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()

    home_page.click_return_link()
    home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/return")


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Правила применения скидок'")
def test_link_promo_rules(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()

    home_page.click_promo_rules_link()
    home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/promo-rules")


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Порядок отпуска лекарственных средств'")
def test_link_medication_release(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()

    home_page.click_medication_release_link()
    home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/medication_release")


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Политика обработки персональных данных'")
def test_link_politics_personal_data(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()

    home_page.click_politics_personal_data_link()
    home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/politics_personal_data")


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Пользовательское соглашение'")
def test_link_terms_of_use(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()

    home_page.click_terms_of_use_link()
    home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/terms_of_use/")


@allure.suite("Работа ссылок")
@allure.title("Проверка работы ссылки 'Правовая информация'")
def test_link_legal_information(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.confirm_address()

    home_page.click_legal_information_link()
    home_page.check_for_url_is_changed(home_page.get_current_url(), "https://apteka.magnit.ru/legal_information/")
