import pytest
from ctreport_selenium.ctlistener import Test
from ctreport_selenium.utility_classes import Priority

from pages.accountpage import AccountPage
from pages.paybillspage import PayBillsPage
from testdata.read_data import get_data


class TestPayBills:

    @pytest.fixture(scope="class")
    def navigate_to_paybills(self, driver, do_login):
        account = AccountPage(driver)
        account.click_pay_bills_link()

    @pytest.mark.usefixtures("navigate_to_paybills")
    @pytest.mark.parametrize("name,reg_no", get_data())
    def test_add_new_payee(self, driver, name, reg_no):
        self.test = Test("Adding New Payee",
                         id=3327,
                         description="Add a new payee in the pay bills page",
                         priority=Priority.HIGH)

        self.test.log("Navigated to Pay Bills page")
        paybills = PayBillsPage(driver)
        paybills.click_add_new_biller_button()
        self.test.log("Navigated to Add New Biller page")
        paybills.do_add_new_payee(name, reg_no)
        self.test.assert_are_equal(paybills.get_confirmation_text().strip(),
                                   "Payee Added Successful",
                                   "Verifying payment confirmation text",
                                   True)

    def teardown_method(self, method):
        self.test.finish()
