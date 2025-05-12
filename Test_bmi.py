import Lab2_2510.bmi as BMI


def test_bmi_normal_weight():
    expected_result = 0
    test_result = BMI.calculate_bmi(1.73, 57)
    assert(test_result == expected_result)


def test_bmi_over_weight():
    expected_result = 1
    test_result = BMI.calculate_bmi(1.73, 97)
    assert(test_result == expected_result)


def test_bmi_under_weight():
    expected_result = -1
    test_result = BMI.calculate_bmi(1.73, 37)
    assert(test_result == expected_result)

