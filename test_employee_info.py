import employee_info as EMP
from employee_info import employee_data as EMPDATA


def test_get_employees_by_age_range():
    expected_result = [EMPDATA[0], EMPDATA[1], EMPDATA[4]]
    test_result = []
    test_result = EMP.get_employees_by_age_range(24, 33)
    assert(test_result == expected_result)


def test_Calculate_average_salary():
    expected_result = 60166.67
    test_result = EMP.calculate_average_salary()
    assert(test_result == expected_result)


def test_get_employees_by_dept_Marketing():
    expected_result = [EMPDATA[1], EMPDATA[2]]
    dept = 'Marketing'
    test_result = []
    test_result = EMP.get_employees_by_dept(dept)
    assert(test_result == expected_result)


def test_get_employees_by_dept_Sales():
    expected_result = [EMPDATA[0], EMPDATA[-1]]
    dept = 'Sales'
    test_result = []
    test_result = EMP.get_employees_by_dept(dept)
    assert(test_result == expected_result)


