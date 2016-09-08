def decorator_test(func):
    def wraper(name):
        return "<p>{name}</p>".format(name=func(name))
    return wraper

@decorator_test
def get_text(name):
    return name
print get_text("test")

