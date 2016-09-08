class A:
    def sum(self, a, b):
        return a + b
class B(A):
    def sum(self, a, b):
        return 2*(a + b)

class C(A):
    def sum(self, a, b):
        return super(C,self).sum(a,b)

print A().sum(4,5)
print B().sum(4,5)
print C().sum(4,5)
