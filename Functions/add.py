# function add 2 numbers
def sum(a,b):
    return a + b

print(sum(1,2))


# test sum() 
def test_sum():
    # expected result
    expected_result = 3

    actual_result = sum(1,2)

    assert actual_result == expected_result
    
test_sum()


