import price_info


def test_cost_of_fruits():
    expected_result = 19.50
    key = 'watermelon'
    test_result = price_info.cost_of_fruits(key, 3)
    assert(test_result == expected_result)



def test_total_cost_shopping():
    expected_result = 46.75
    test_result = price_info.total_cost_shopping()
    assert(test_result == expected_result)
