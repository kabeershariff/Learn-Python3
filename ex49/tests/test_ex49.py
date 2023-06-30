import pytest
from ex49.parser import *

def test_peek():
    result = peek([('noun', 'bear')])
    assert result == 'noun'

    result = peek([('noun', 'bear'), ('verb', 'eat'), ('noun', 'honey')])
    assert result == 'noun'

def test_parse_subject():
    result = parse_subject([('noun', 'bear'), ('verb', 'run')])
    assert result == ('noun', 'bear')

def test_parse_verb():
    result = parse_verb([('verb', 'eat'), ('noun', 'bear')])
    assert result == ('verb', 'eat')

def test_parse_sentence():
    result = parse_sentence([('verb', 'run'), ('direction', 'north')])

    assert result.subject == 'player'
    assert result.verb == 'run'
    assert result.object == 'north'

    result = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])

    assert result.subject == 'bear'
    assert result.verb == 'eat'
    assert result.object == 'honey'
