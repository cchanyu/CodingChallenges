class BrowserHistory(object):
    def __init__(self, homepage) -> None:
        self.history = [homepage]
        self.current = 0

    def visit(self,url):
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current = len(self.history) - 1

    def back(self,steps):
        self.current = max(self.current - steps, 0)
        return self.history[self.current]
    
    def forward(self,steps):
        self.current = min(self.current + steps, len(self.history) - 1)
        return self.history[self.current]
    
'''
Explain 1: @forward
self.current = min(self.current + steps, len(self.history) - 1)
when you forward, there is a possibility of going over current index.
so in order to ensure that it stays within, we use min().
len(self.history) - 1 <- is the last index. so if it passes this, it'll return this index
if it doesn't, it'll return the regular value: self.current + steps

Explain 2: @back
self.current = max(self.current - steps, 0)
similar concept as forward, but this ensures that values stay beyond 0.
so if it's below 0, it'll return 0, otherwise returns the normal value.

Explain 3: @visit
self.history = self.history[:self.current + 1]
this slices the list, and replace it to keeps things updated
this is necessary due to going back and forward.

'''