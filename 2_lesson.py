from selene import have, browser


def test_search_1(open_browser):
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_search_2(open_browser):
    browser.element('[class="ExCKkf z1asCe rzyADb"]').click()
    browser.element('[name="q"]').type('ыфа!2512афыа1йафывп!"№!"4').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print("В поиске нет результатов...")
