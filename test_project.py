from project import greeting
from project import get_answer
from project import result
import pytest


def test_greeting(monkeypatch,capsys):
    input=iter(["H*D","happy"])
    monkeypatch.setattr("builtins.input",lambda _:next(input))
    with pytest.raises(SystemExit):
        greeting()
    
    input=iter(["Baby Poo","Good:)"])
    monkeypatch.setattr("builtins.input",lambda _:next(input))
    captured = capsys.readouterr()
    assert "♡ Let's start with a survey to see your stress level." in captured.out
    

def test_get_answer(monkeypatch):
    input=iter(["C","C","C","C"])
    monkeypatch.setattr("builtins.input",lambda _:next(input))
    answers=get_answer([])
    assert answers==["C","C","C","C"]
    
    
def test_result():
    answers=["C","C","C","C"]
    assert result(answers)=="mid"
    
    answers=["A","E","E","A"]
    assert result(answers)=="low"
    
    answers=["E","A","A","E"]
    assert result(answers)=="high"