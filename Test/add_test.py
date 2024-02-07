from UniTest.Functions.add  import sum


# function test sum() 
def test_sum():
    # expected result
    expected_result = 3

    actual_result = sum(1,2)

    assert actual_result == expected_result

test_sum()

