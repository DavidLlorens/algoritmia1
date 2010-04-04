#coding: latin1

#< bigint0
class BigIntBase:
    def __init__(self, digits: "IList<int> or str or int"):
        if type(digits) == list:
            self.digit = digits[::-1]
        elif type(digits) == str:
            self.digit = [int(digit) for digit in reversed(digits)]
        elif type(digits) == int:
            self.digit = []
            while digits > 0:
                self.digit.append(digits%10)
                digits //= 10
            if self.digit == []: self.digit = [0]

    def __repr__(self):
        if len(self.digit) == 0: return '0'
        for i in range(len(self.digit)-1,-1,-1):
            if self.digit[i] != 0: break
        return ''.join(str(digit) for digit in reversed(self.digit[:i+1]))

    def __len__(self):
        i = 0
        for i in range(len(self.digit)-1,-1,-1):
            if self.digit[i] != 0: break
        return i+1

    def __getitem__(self, i: "int") -> "int":
        if not (0 <= i < len(self.digit)): return 0
        return self.digit[i]

    def __add__(self, other: "BigInt") -> "BigInt":
        n = max(len(self), len(other))
        result, carry = [], 0
        for i in range(n):
            s = self[i] + other[i] + carry
            carry = s // 10
            result.append(s % 10)
        if carry: result.append(carry)
        return self.__class__(list(reversed(result)))

    def __lshift__(self, n: "Bigint") -> "BigInt":
        return self.__class__(self.digit[::-1]+[0]*n)

    def __mul__(self, other: "BigInt") -> "BigInt":
        u, v = self, other
        n = max(len(u), len(v))
        if n == 1:
            r = u[0] * v[0]
            return BigIntBase([r]) if r < 10 else BigIntBase([r//10, r%10])
        else:
            s = n // 2
            w, x = BigIntBase(u.digit[s:][::-1]), BigIntBase(u.digit[:s][::-1])
            y, z = BigIntBase(v.digit[s:][::-1]), BigIntBase(v.digit[:s][::-1])
            return ((w*y) << (s<<1)) + ((w*z+x*y) << s) + x*z
#> bigint0

#< bigint
class BigInt(BigIntBase):
    def __init__(self, digits: "IList<int> or str or int"):
        super().__init__(digits)

    def __sub__(self, other: "BigInt") -> "BigInt":
        n = max(len(self), len(other))
        result, carry = [], 0
        for i in range(n):
            s = self[i] - other[i] + carry
            carry = s // 10
            if s < 0: result.append(10 + s)
            else: result.append(s % 10)
        if carry: result.append(-carry)
        return BigInt(list(reversed(result)))

    def __mul__(self, other: "BigInt") -> "BigInt":
        u, v = self, other
        n = max(len(u), len(v))
        if n == 1:
            r = u[0] * v[0]
            return BigInt([r]) if r < 10 else BigInt([r//10, r%10])
        else:
            s = n // 2
            w, x = BigInt(u.digit[s:][::-1]), BigInt(u.digit[:s][::-1])
            y, z = BigInt(v.digit[s:][::-1]), BigInt(v.digit[:s][::-1])
            alpha, beta, gamma = w * y, x * z, (w+x) * (y+z)
            return (alpha << (s<<1)) + ((gamma - beta - alpha) << s) + beta
#> bigint