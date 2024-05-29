from demo_tests_python import reverse_str_ko, reverse_str_ok

def test_should_reverse_string():
    assert reverse_str_ko('abc') == 'cba', 'Error in reversing string'
    
def test_should_reverse_string2():    
    assert reverse_str_ok('abc') == 'cba', 'Error in reversing string'

