from UniTest.Functions.add  import  sub


# function test sum() 
def test_sub():
    # expected result
    expected_result = 3

    actual_result = sub(6,2)

    assert actual_result == expected_result

test_sub()