from conversor import converte

def test_deveEntenderOsSimbolosI():
    assert converte('I') == 1

def test_deveEntenderOsSimbolosV():
    assert converte('V') == 5

def test_deveEntenderOsSimbolosL():
    assert converte('L') == 50

def test_deveEntenderOsSimbolosII():
    assert converte('II') == 2

def test_deveEntenderSimbolosComoIX():
    assert converte('IX')== 9