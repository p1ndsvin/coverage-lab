import pytest

from max_consecutive import max_consecutive_items


def test_empty():
    assert max_consecutive_items([]) == 0

def test_all_equal():
    assert max_consecutive_items([7, 7, 7]) == 3

def test_mixed_but_bug_not_exposed():
    assert max_consecutive_items([1, 1, 2, 2]) == 2

def test_mixed_bug_exposed():
    assert max_consecutive_items([1,2,2,3]) == 2
# test_mixed_but_bug_not_exposed non espone il bug perché, anche se current viene azzerato erroneamente, il massimo (2) era già stato trovato prima, quindi il risultato resta corretto.
# In test_mixed_bug_exposed, invece, la sequenza [2,2] viene contata in maniera errata (parte da 0 invece che 1), producendo un risultato sbagliato.
# La branch coverage è comunque 100% perché entrambi i rami (if ed else) vengono eseguiti, ma questo non garantisce che i bug vengano rilevati.
