from nose.tools import assert_equal, assert_raises

from stats import mean, median

def test_median_1():

    obs = median([1,2,3])
    exp = 2
    assert_equal(obs,exp)

def test_median_2():

    obs = median([1,2,3,4])
    exp = 2.5
    assert_equal(obs,exp)

def test_median_sort():

    obs = median([5,3,8,2,1])
    exp = 3
    assert_equal(obs,exp)

def test_median_tuple():

    obs = median((5,3,8,2,1))
    exp = 3
    assert_equal(obs,exp)

def test_mean_1():

    obs = mean([1,2,3])
    exp = 2
    assert_equal(obs,exp)

def test_mean_2():

    obs = mean([3,4,5])
    exp = 4
    assert_equal(obs,exp)

def test_mean_3():

    obs = mean([-3,-4,-5])
    exp = -4
    assert_equal(obs,exp)

def test_mean_4():

    obs = mean([-3,5])
    exp = 1
    assert_equal(obs,exp)

def test_mean_5():

    obs = mean([5])
    exp = 5
    assert_equal(obs,exp)

def test_mean_6():

    obs = mean(6)
    exp = 6
    assert_equal(obs,exp)

def test_mean_float():

    obs = mean([3,4])
    exp = 3.5
    assert_equal(obs,exp)

def test_mean_empty():

    obs = mean([])
    exp = None
    assert_equal(obs,exp)

def test_mean_string():

    assert_raises(TypeError,mean,['one','two'])







