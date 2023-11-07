import lab07

def test_validate_variable():
    assert lab07.validate_variable('max')          == True
    assert lab07.validate_variable('x2')           == True
    assert lab07.validate_variable('test_avg')     == True
    assert lab07.validate_variable('standardDev')  == True
    assert lab07.validate_variable('1minumum')     == False

def test_validate_domain():
    assert lab07.validate_domain('google.ca')        == True
    assert lab07.validate_domain('smile.amazon.com') == True
    assert lab07.validate_domain('unicef.org')       == True
    assert lab07.validate_domain('google.uk')        == False

def test_validate_phone():
    assert lab07.validate_phone('721-8668')      == True
    assert lab07.validate_phone('905-721-8668')  == True
    assert lab07.validate_phone('(905)721-8668') == True
    assert lab07.validate_phone('9057218668')    == False
