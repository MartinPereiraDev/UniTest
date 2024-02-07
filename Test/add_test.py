from add  import sum, rest


# function test sum() 
def test_sum():
    # expected result
    expected_result = 3

    actual_result = sum(1,2)

    assert actual_result == expected_result

test_sum()

# function test sum() 
def test_rest():
    # expected result
    expected_result = 3

    actual_result = rest(6,2)

    assert actual_result == expected_result

test_rest()