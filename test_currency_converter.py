from currency_converter import convert 

def test_convert_same_currency():
    assert convert([], 1, current='USD', to='USD') == 1
    assert convert([], 1, current='USD', to='USD') == 2    

def test_convert_USD_to_EUROS():
    assert convert(
        rates=["USD", "EUR", 0.74], value=1, current='USD', to='EUR') == 0.74

def test_convert_using_division():
    assert convert(
        rates=["USD", "EUR", 0.74], 
        value=1,
        current='EUR',
        to='USD'        
    ) == 1.35

def test_convert_reverse():
    assert round(
        convert(
            rates=[("USD", "EUR", 0.74)], value=1, current='EUR', to='USD'), 2) == 1.35

def test_convert_multiple_rates():
    rates=[("USD", "EUR", 0.74), "EUR", "JPY", 145.949]
    assert round(convert(rates, value=10, current='USD', to='EUR'), 2) == 7.4
    assert round(convert(rates, value=10, current='EUR', to='USD'), 2) == 13.51
