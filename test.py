import os
from selene import be, have
from fixture_test import open_demo

def test_name(open_demo):
    open_demo.element('#firstName').should(be.blank).type('Jul')
    open_demo.element('#firstName').should(have.value('Jul'))
    open_demo.element('#lastName').should(be.blank).type('Krv')
    open_demo.element('#lastName').should(have.value('Krv'))

def test_email(open_demo):
    open_demo.element('#userEmail').should(be.blank).type('julkrv@test.co')
    open_demo.element('#userEmail').should(have.value('julkrv@test.co'))

def test_gender(open_demo):
    open_demo.element('label[for=gender-radio-2]').click()
    open_demo.element('label[for=gender-radio-2]').should(be.enabled)

def test_mobile(open_demo):
    open_demo.element('#userNumber').should(be.blank).type('1234567890')
    open_demo.element('#userNumber').should(have.value('1234567890'))

def test_birth_date(open_demo):
    open_demo.element('#dateOfBirthInput').click()
    open_demo.element('.react-datepicker__month-select').type('June')
    open_demo.element('.react-datepicker__year-select').type('1999')
    open_demo.element('.react-datepicker__day--015').click()
    open_demo.element('#dateOfBirthInput').should(have.value('15 Jun 1999'))

def test_subjects(open_demo):
    open_demo.element('#subjectsInput').should(be.blank).type('qwerty')
    open_demo.element('#subjectsInput').should(have.value('qwerty'))

def test_hobbies(open_demo):
    open_demo.element('label[for=hobbies-checkbox-1]').click()
    open_demo.element('label[for=hobbies-checkbox-2]').click()
    open_demo.element('label[for=hobbies-checkbox-1]').should(be.existing)
    open_demo.element('label[for=hobbies-checkbox-2]').should(be.existing)
    # open_demo.element('label[for=hobbies-checkbox-3]').should(be.)

def test_photo(open_demo):
    print()
    open_demo.element('#uploadPicture')\
        .set_value(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                'merry.jpg'
            )
        )
    )


def test_address(open_demo):
    open_demo.element('#currentAddress').should(be.blank).type('anything')
    open_demo.element('#currentAddress').should(have.value('anything'))

def test_state_and_city(open_demo):
    open_demo.element('#react-select-3-input').type('NCR').press_enter()
    open_demo.element('#react-select-4-input').type('Noida').press_enter()


def test_submit(open_demo):
    open_demo.element('#submit').press_enter()
