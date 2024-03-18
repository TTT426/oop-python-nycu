import add_path
import mit_ocw_exercises.lec8_classes as lc
    
def test_coordinate():
   c = lc.Coordinate(3, 4)
   origin = lc.Coordinate(0,0)
   assert c.x == 3
   assert c.y == 4
   assert c.distance(origin) == 5
   assert origin.distance(c) == 5

def test_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)
    
def test_5_frac():
    quarter = lc.Fraction(1, 4)
    half = lc.Fraction(1,2)
    assert quarter.num == 1
    assert quarter.denom == 4
    sum = half.__add__(quarter)
    assert sum.num == 6
    assert sum.denom == 8
    
def test_8_coordinate():
    c = lc.Coordinate(6,8)
    origin = lc.Coordinate(0,0)
    assert c.x == 6
    assert c.y == 8
    assert c.distance(origin) == 10
    assert origin.distance(c) == 10
    
    assert not c.x == 7; assert not c.y == 9

def test_8_intset():
    myset = lc.intSet() # create a new intSet
    myset.insert(100)
    myset.insert(200)
    myset.insert(300)
    assert myset.member(100) # returns True
    assert not myset.member(400) # returns False
    myset.remove(100)
    assert not myset.member(100) # returns False
    myset.__str__() # returns a string representation of the set

def test_13_coordinate():
    c = lc.Coordinate(14, 48)
    origin = lc.Coordinate(0,0)
    assert c.x == 14
    assert c.y == 48
    assert c.distance(origin) == 50
    assert origin.distance(c) == 50
    
    c = lc.Coordinate(3, 11)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 11
    assert c.distance(origin) == 11.40175425099138
    assert origin.distance(c) == 11.40175425099138

def test_17_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5
def test_1_coordinate():
    a = lc.Coordinate(5, 12)
    assert a.distance(origin) == 13
    assert a.x == 5
    assert a.y == 12

def test_17_intset():
    s = lc.intSet()
    s.insert(3)
    s.insert(4)
    assert s.member(3)
    assert s.member(4)
    assert not s.member(5)
    s.remove(3)
    assert not s.member(3)
    assert s.member(4)
    
def test_6_coordinate():
    c = lc.Coordinate(5, 12)
    origin = lc.Coordinate(0,0)
    assert c.x == 5
    assert c.y == 12
    assert c.distance(origin) == 13
    assert origin.distance(c) == 13
    
def test_14_coordinate():
    s = lc.Coordinate(8, 15)
    origin = lc.Coordinate(0,0)
    assert s.x == 8
    assert s.y == 15
    assert s.distance(origin) == 17
    assert origin.distance(s) == 17
    
def test_9_coordinate():
    c = lc.Coordinate(6,8)
    origin = lc.Coordinate(0,0)
    assert c.x == 6
    assert c.y == 8
    assert c.distance(origin) == 10
    assert origin.distance(c) == 10

def test_1_intset():
    b = lc.intSet()
    b.insert(10)
    b.insert(11)
    assert b.member(10)
    assert b.member(11)
    assert not b.member(12)
    b.remove(11)
    assert not b.member(11)
    assert b.member(10)

def test_9_intset():
    s = lc.intSet()
    s.insert(8)
    s.insert(7)
    assert s.member(8)
    assert s.member(7)
    s.remove(8)
    assert not s.member(8)
    assert s.member(7)
