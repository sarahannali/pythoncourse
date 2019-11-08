class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
    def __missing__(self,key):
        return f"YOU WANT {key.upper()}? IT'S NOT HERE!"
    def __setitem__(self,key,value):
        print("YOU WANT ME TO CHANGE SOMETHING? FINE...")
        return super().__setitem__(key,value)

d = GrumpyDict({"home":"College Station", "animal":"Zeus"})
print(d)
print(d['house'])
d['home'] = "houston"
print(d)