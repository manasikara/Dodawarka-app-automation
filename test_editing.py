#https://naucz-sie-testowac.czyitjestdlamnie.pl/
#edit the expense

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    context = browser.new_context()
    page.goto("https://naucz-sie-testowac.czyitjestdlamnie.pl/")
    page.click('text= Chcę potrenować pisanie testów automatycznych!')
    page.click('body > app-root > app-board > div > div >       div.col-auto.flex-column.d-sm-flex.expene-list-column.ng-tns-c31-0 > div.btn-plus.mx-auto.ng-tns-c31-0.ng-star-inserted > i')
    page.locator('body > app-root > app-board > div > div > div.col-auto.flex-column.d-sm-flex.expene-list-column.ng-tns-c31-0 > div.expense-details.ng-trigger.ng-trigger-slideTopAnimation.ng-tns-c31-0.ng-star-inserted > div:nth-child(1) > input').fill('some name')
    page.locator('body > app-root > app-board > div > div > div.col-auto.flex-column.d-sm-flex.expene-list-column.ng-tns-c31-0 > div.expense-details.ng-trigger.ng-trigger-slideTopAnimation.ng-tns-c31-0.ng-star-inserted > div:nth-child(2) > input').fill('1500')
    page.locator('body > app-root > app-board > div > div > div.col-auto.flex-column.d-sm-flex.expene-list-column.ng-tns-c31-0 > div.expense-details.ng-trigger.ng-trigger-slideTopAnimation.ng-tns-c31-0.ng-star-inserted > div:nth-child(3) > input').fill('1999-01-02')
    page.click('body > app-root > app-board > div > div > div.col-auto.flex-column.d-sm-flex.expene-list-column.ng-tns-c31-0 > div.expense-details.ng-trigger.ng-trigger-slideTopAnimation.ng-tns-c31-0.ng-star-inserted > button.btn.btn-outline-success.float-end.ng-tns-c31-0 > i')
    page.locator('.bi bi-clipboard ng-tns-c31-0 ng-star-inserted').click
    
    time.sleep(3)
    
    #editing the expense
    page.click('button[data-cy=edit-expense-btn]')
    
    page.locator('body > app-root > app-board > div > div > div.col-auto.flex-column.d-sm-flex.expene-list-column.ng-tns-c31-0 > div.expense-details.ng-trigger.ng-trigger-slideTopAnimation.ng-tns-c31-0.ng-star-inserted > div:nth-child(1) > input').fill('now different name')
    time.sleep(3)
    page.locator('body > app-root > app-board > div > div > div.col-auto.flex-column.d-sm-flex.expene-list-column.ng-tns-c31-0 > div.expense-details.ng-trigger.ng-trigger-slideTopAnimation.ng-tns-c31-0.ng-star-inserted > div:nth-child(2) > input').fill('2300')
    page.locator('body > app-root > app-board > div > div > div.col-auto.flex-column.d-sm-flex.expene-list-column.ng-tns-c31-0 > div.expense-details.ng-trigger.ng-trigger-slideTopAnimation.ng-tns-c31-0.ng-star-inserted > div:nth-child(3) > input').fill('2012-06-13')
    page.locator('.bi bi-clipboard ng-tns-c31-0 ng-star-inserted').click
    
    time.sleep(2)
    
    context.storage_state(path="data/state.json")
    browser.close()
    print('Done!')
    
    



