class MaxSizeList(object):
    """
    This is my first assigment, this could be bad becuase it stores all
    the stuff that is eveer appeneded. In real apllication this could get
    huge. But I am gonna keep it give amethod to allow an update of max list size.
    ... actually maybe not as then I am essentailly reimplemeting a list as an
    object but any remable over ..... write comments like this in future
    """
    def __init__(self, max_size):
        self.mylist=[]
        self.max_size=max_size
    def push(self, new_entry):
        self.mylist.append(new_entry )
    def get_list(self):
        return self.mylist[-self.max_size:]
