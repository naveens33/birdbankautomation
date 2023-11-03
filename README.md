# BirdBank Automation - Hybrid Framework

### Dependencies

-> refer it in requirement.txt

### Folder/Package Structure

* pages - POM (Page Object Model)- Design Pattern
  * BasePage class, hold all the selenium interaction like click(locator), enter_text(locator,text)
  * Page classes like, HomePage, LoginPage, AccountPage
    * Page objects -> By locators like By.ID, "signin_button"
    * Page actions -> def click_login_button():
    * has to inherit the BasePage
* testdata
  * Excel file that holds the test data
  * read_data.py - responsible to read data from the Excel (xlrd)
* reports
  * html reports (ctreport-selenium)
  * logs
* tests
  * pytest test methods
* Root Directory/Project Directory
  * pytest.ini
  * conftest.py
  * README.md
  * requirements.txt