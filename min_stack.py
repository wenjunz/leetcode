class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if self.minstack == []:
            self.minstack.append(x)
        else:
            self.minstack.append(min(self.minstack[-1],x))
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack == []:
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minstack == []:
            return None
        else:
            return self.minstack[-1]
        
