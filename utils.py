"""Utilities

"""
# pylint: disable=no-member

import collections.abc
import math
import os


def floor(value, size, offset=200): #size기준으로 나눈 화면 안에 value값이 어떤 분할점에 포함되는지 반환
    """Floor of `value` given `size` and `offset`.

    The floor function is best understood with a diagram of the number line::

         -200  -100    0    100   200
        <--|--x--|-----|--y--|--z--|-->

    The number line shown has offset 200 denoted by the left-hand tick mark at
    -200 and size 100 denoted by the tick marks at -100, 0, 100, and 200. The
    floor of a value is the left-hand tick mark of the range where it lies. So
    for the points show above: ``floor(x)`` is -200, ``floor(y)`` is 0, and
    ``floor(z)`` is 100.

    >>> floor(10, 100)
    0.0
    >>> floor(120, 100)
    100.0
    >>> floor(-10, 100)
    -100.0
    >>> floor(-150, 100)
    -200.0
    >>> floor(50, 167)
    -33.0

    """
    return float(((value + offset) // size) * size - offset)


def path(filename): #특정 디렉토리 내 파일을 받아오기 위한 메소드
    "Return full path to `filename` in freegames module."
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    fullpath = os.path.join(dirpath, filename)
    return fullpath


def line(a, b, x, y): #turtle을 사용해 선을 그리기 위해 구현한 메소드
    "Draw line from `(a, b)` to `(x, y)`."
    import turtle     #turtle모듈을 사용

    turtle.up()
    turtle.goto(a, b)
    turtle.down()
    turtle.goto(x, y)


def square(x, y, size, name): #turtle을 사용해 사각형을 그리기 위해 구현한 메소드
    """Draw square at `(x, y)` with side length `size` and fill color `name`.

    The square is oriented so the bottom left corner is at (x, y).

    """
    import turtle             #turtle모듈 사용

    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(name)
    turtle.begin_fill()

    for count in range(4):    #반복시 마다 90도 회전하여 선을 그림
        turtle.forward(size)
        turtle.left(90)

    turtle.end_fill()


class vector(collections.abc.Sequence): #좌표가 있는 객체를 만들기 위한 클래스
    """Two-dimensional vector.

    Vectors can be modified in-place.

    >>> v = vector(0, 1)
    >>> v.move(1)
    >>> v
    vector(1, 2)
    >>> v.rotate(90)
    >>> v
    vector(-2.0, 1.0)

    """

    # pylint: disable=invalid-name
    PRECISION = 6

    __slots__ = ('_x', '_y', '_hash')

    def __init__(self, x, y): #객체를 선언하기 위한 생성자 메소드
        """Initialize vector with coordinates: x, y.

        >>> v = vector(1, 2)
        >>> v.x
        1
        >>> v.y
        2

        """
        self._hash = None
        self._x = round(x, self.PRECISION) #입력받은 매개변수를 x변수에 입력
        self._y = round(y, self.PRECISION) #입력받은 매개변수를 y변수에 입력

    @property       #객체의 변수값을 받아오기 위해 GetterSetter을 구현
    def x(self):    #x값을 받아오기 위한 getter구현
        """X-axis component of vector.

        >>> v = vector(1, 2)
        >>> v.x
        1
        >>> v.x = 3
        >>> v.x
        3

        """
        return self._x

    @x.setter       #x값을 수정하기 위한 setter구현
    def x(self, value):
        if self._hash is not None:
            raise ValueError('cannot set x after hashing')
        self._x = round(value, self.PRECISION)

    @property       #y값을 받아오기 위한 getter구현
    def y(self):
        """Y-axis component of vector.

        >>> v = vector(1, 2)
        >>> v.y
        2
        >>> v.y = 5
        >>> v.y
        5

        """
        return self._y

    @y.setter       #y값을 받아오기 위한 setter구현
    def y(self, value):
        if self._hash is not None:
            raise ValueError('cannot set y after hashing')
        self._y = round(value, self.PRECISION)

    def __hash__(self): #클래스에 맞는 hash 구현
        """v.__hash__() -> hash(v)

        >>> v = vector(1, 2)
        >>> h = hash(v)
        >>> v.x = 2
        Traceback (most recent call last):
            ...
        ValueError: cannot set x after hashing

        """
        if self._hash is None:
            pair = (self.x, self.y)
            self._hash = hash(pair)
        return self._hash

    def __len__(self):  #객체의 길이를 출력하는 메소드
        """v.__len__() -> len(v)

        >>> v = vector(1, 2)
        >>> len(v)
        2

        """
        return 2        #객체의 길이는 x값과 y값 밖에 없음으로 2다

    def __getitem__(self, index):   #인덱스 값을 이용하여 객체의 정보를 받아오는 메소드
        """v.__getitem__(v, i) -> v[i]

        >>> v = vector(3, 4)
        >>> v[0]
        3
        >>> v[1]
        4
        >>> v[2]
        Traceback (most recent call last):
            ...
        IndexError

        """
        if index == 0:              #x가 첫번째 값이기 때문에 인덱스가 0이면 x를 반환
            return self.x
        if index == 1:              #y가 두번째 값이기 때문에 인덱스가 1이면 y를 반환
            return self.y
        raise IndexError            #vector객체는 x와 y밖에 없기 때문에 index값이 1을 초과하지 않음

    def copy(self):                 #객체를 복사하기 위한 메소드
        """Return copy of vector.

        >>> v = vector(1, 2)
        >>> w = v.copy()
        >>> v is w
        False

        """
        type_self = type(self)          #임시 객체를 생성
        return type_self(self.x, self.y)#임시 객체에 현 객체의 값을 저장하고 반환

    def __eq__(self, other):    #객체가 같은지 판별하는 메소드
        """v.__eq__(w) -> v == w

        >>> v = vector(1, 2)
        >>> w = vector(1, 2)
        >>> v == w
        True

        """
        if isinstance(other, vector):                       #매개변수가 vector객체인지 판별
            return self.x == other.x and self.y == other.y  #매개변수의 값이 현 객체와 맞는지 판별 후 참거짓을 출력
        return NotImplemented                               #매개변수가 vector이 아니라는 메세지 반환

    def __ne__(self, other):    #객체가 다른지 판별하는 메소드
        """v.__ne__(w) -> v != w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v != w
        True

        """
        if isinstance(other, vector):                       #매개변수가 vector객체인지 판별
            return self.x != other.x or self.y != other.y   #매개변수의 값이 현 객체와 다른지 판별 후 참거짓을 출력
        return NotImplemented                               #매개변수가 vector이 아니라는 메세지 반환

    def __iadd__(self, other):          #입력받은 객체를 현객체와 더하는 메소드 구현
        """v.__iadd__(w) -> v += w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v += w
        >>> v
        vector(4, 6)
        >>> v += 1
        >>> v
        vector(5, 7)

        """
        if self._hash is not None:       #해시값이 none면 오류를 발생시킴
            raise ValueError('cannot add vector after hashing')
        if isinstance(other, vector):   #매개변수의 타입이 vector인지 판별
            self.x += other.x           #매개변수의 x값과 현 객체의 x값의 합를 현 객체의 x값에 저장
            self.y += other.y           #매개변수의 y값과 현 객체의 y값의 합를 현 객체의 y값에 저장
        else:                           #매개변수의 타입이 vector이 아닐시
            self.x += other             #매개변수의 값과 현 객체의 x값의 합를 현 객체의 x값에 저장
            self.y += other             #매개변수의 값과 현 객체의 y값의 합를 현 객체의 y값에 저장
        return self

    def __add__(self, other):           #두 vector객체를 더하는 메소드  
        """v.__add__(w) -> v + w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v + w
        vector(4, 6)
        >>> v + 1
        vector(2, 3)
        >>> 2.0 + v
        vector(3.0, 4.0)

        """
        copy = self.copy()              #임시객체인 copy값에 현객체를 복사함
        return copy.__iadd__(other)     #iadd메소드를 호출하여 copy객체와 other객체를 더함

    __radd__ = __add__                  #피연산자가 반대로 된 경우에도 add를 이용

    def move(self, other):              #매개변수 만큼 x값과 y값을 더하는 메소드
        """Move vector by other (in-place).

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v.move(w)
        >>> v
        vector(4, 6)
        >>> v.move(3)
        >>> v
        vector(7, 9)

        """
        self.__iadd__(other)            #iadd메소드를 호출하여 연산

    def __isub__(self, other):          #입력받은 객체를 현객체와 빼는 메소드 구현
        """v.__isub__(w) -> v -= w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v -= w
        >>> v
        vector(-2, -2)
        >>> v -= 1
        >>> v
        vector(-3, -3)

        """
        if self._hash is not None:      #해시값이 none면 오류를 발생시킴
            raise ValueError('cannot subtract vector after hashing')
        if isinstance(other, vector):   #매개변수의 타입이 vector인지 판별
            self.x -= other.x           #매개변수의 x값과 현 객체의 x값의 차을 현 객체의 x값에 저장
            self.y -= other.y           #매개변수의 y값과 현 객체의 y값의 차을 현 객체의 y값에 저장
        else:                           #매개변수의 타입이 vector이 아닐시
            self.x -= other             #매개변수의 값과 현 객체의 x값의 차을 현 객체의 x값에 저장
            self.y -= other             #매개변수의 값과 현 객체의 y값의 차을 현 객체의 y값에 저장
        return self                     

    def __sub__(self, other):           #두 vector객체를 빼는 메소드  
        """v.__sub__(w) -> v - w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v - w
        vector(-2, -2)
        >>> v - 1
        vector(0, 1)

        """
        copy = self.copy()              #임시객체인 copy값에 현객체를 복사함
        return copy.__isub__(other)     #isub메소드를 호출하여 copy객체와 other객체를 뺌

    def __imul__(self, other):          #입력받은 객체를 현객체와 곱하는 메소드 구현
        """v.__imul__(w) -> v *= w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v *= w
        >>> v
        vector(3, 8)
        >>> v *= 2
        >>> v
        vector(6, 16)

        """
        if self._hash is not None:      #해시값이 none면 오류를 발생시킴
            raise ValueError('cannot multiply vector after hashing')
        if isinstance(other, vector):   #매개변수의 타입이 vector인지 판별
            self.x *= other.x           #매개변수의 x값과 현 객체의 x값의 곱을 현 객체의 x값에 저장
            self.y *= other.y           #매개변수의 y값과 현 객체의 y값의 곱을 현 객체의 y값에 저장
        else:                           #매개변수의 타입이 vector이 아닐시
            self.x *= other             #매개변수의 값과 현 객체의 x값의 곱을 현 객체의 x값에 저장
            self.y *= other             #매개변수의 값과 현 객체의 y값의 곱을 현 객체의 y값에 저장
        return self

    def __mul__(self, other):           #두 vector객체를 곱하는 메소드 
        """v.__mul__(w) -> v * w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v * w
        vector(3, 8)
        >>> v * 2
        vector(2, 4)
        >>> 3.0 * v
        vector(3.0, 6.0)

        """
        copy = self.copy()              #임시객체인 copy값에 현객체를 복사함
        return copy.__imul__(other)     #imul메소드를 호출하여 copy객체와 other객체를 곱함

    __rmul__ = __mul__                  #피연산자가 반대로 된 경우에도 mul를 이용

    def scale(self, other):             #원점과 객체의 위치를 기준으로 하는 도형의 크기를 조정하는 메소드
        """Scale vector by other (in-place).

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v.scale(w)
        >>> v
        vector(3, 8)
        >>> v.scale(0.5)
        >>> v
        vector(1.5, 4.0)

        """
        self.__imul__(other)            #imul을 호출하여 객체와 매개변수를 곱함

    def __itruediv__(self, other):      #입력받은 객체를 현객체와 나누는 메소드 구현
        """v.__itruediv__(w) -> v /= w

        >>> v = vector(2, 4)
        >>> w = vector(4, 8)
        >>> v /= w
        >>> v
        vector(0.5, 0.5)
        >>> v /= 2
        >>> v
        vector(0.25, 0.25)

        """
        if self._hash is not None:      #해시값이 none면 오류를 발생시킴
            raise ValueError('cannot divide vector after hashing')
        if isinstance(other, vector):   #매개변수의 타입이 vector인지 판별
            self.x /= other.x           #매개변수의 x값과 현 객체의 x값의 제산을 현 객체의 x값에 저장
            self.y /= other.y           #매개변수의 y값과 현 객체의 y값의 제산을 현 객체의 y값에 저장
        else:                           #매개변수의 타입이 vector이 아닐시
            self.x /= other             #매개변수의 값과 현 객체의 x값의 제산을 현 객체의 x값에 저장
            self.y /= other             #매개변수의 값과 현 객체의 y값의 제산을 현 객체의 y값에 저장
        return self

    def __truediv__(self, other):       #두 vector객체를 나누는 메소드 
        """v.__truediv__(w) -> v / w

        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> w / v
        vector(3.0, 2.0)
        >>> v / 2
        vector(0.5, 1.0)

        """
        copy = self.copy()              #임시객체인 copy값에 현객체를 복사함
        return copy.__itruediv__(other) #imul메소드를 호출하여 copy객체와 other객체를 곱함

    def __neg__(self):                  #객체의 역을 구하는 메소드
        """v.__neg__() -> -v

        >>> v = vector(1, 2)
        >>> -v
        vector(-1, -2)

        """
        # pylint: disable=invalid-unary-operand-type
        copy = self.copy()              #임시객체인 copy에 현 객체를 복사
        copy.x = -copy.x                #copy객체의 x값에 -를 붙인 값을 저장
        copy.y = -copy.y                #copy객체의 y값에 -를 붙인 값을 저장
        return copy                     #copy객체를 반환

    def __abs__(self):                  #객체의 스칼라 값을 구하는 메소드
        """v.__abs__() -> abs(v)        

        >>> v = vector(3, 4)
        >>> abs(v)
        5.0

        """
        return (self.x ** 2 + self.y ** 2) ** 0.5   #스칼라값을 반환함

    def rotate(self, angle):            #객체를 원점기준으로 매개변수 만큼 돌린 값을 구하는 메소드
        """Rotate vector counter-clockwise by angle (in-place).

        >>> v = vector(1, 2)
        >>> v.rotate(90)
        >>> v == vector(-2, 1)
        True

        """
        if self._hash is not None:      #해시값이 none면 오류를 발생시킴
            raise ValueError('cannot rotate vector after hashing')
        radians = angle * math.pi / 180.0   #radians변수를 선언하고 매개변수로 받은 값의 라디안 값을 저장
        cosine = math.cos(radians)      #cosine변수를 선언하고 radians변수에 있는 값의 코사인 값을 저장
        sine = math.sin(radians)        #sine변수를 선언하고 radians변수에 있는 값의 사인 값을 저장
        x = self.x                      #x변수에 현 객체의 x값을 저장
        y = self.y                      #y변수에 현 객체의 y값을 저장
        self.x = x * cosine - y * sine  #객체의 x값에 angle값만큼 회전시킨 후 x값을 저장
        self.y = y * cosine + x * sine  #객체의 y값에 angle값만큼 회전시킨 후 y값을 저장

    def __repr__(self):                 #현 객체를 표현하는 메소드
        """v.__repr__() -> repr(v)

        >>> v = vector(1, 2)
        >>> repr(v)
        'vector(1, 2)'

        """
        type_self = type(self)          #객체의 타입을 type_self변수에 저장
        name = type_self.__name__       #type_self의 내장변수를 name값에 저장
        return '{}({!r}, {!r})'.format(name, self.x, self.y)    #객체의 타입과 변수들의 저장값을 반환함
