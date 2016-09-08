class myClass:
    def hello(self):
        print "hi"
    @classmethod
    def hello(cls, string):
        print string
ob = myClass()
ob.hello()

