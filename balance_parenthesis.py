class Solution:

    def __init__(self,parenthesis_String):
        self.parenthesis_String = parenthesis_String

    @property
    def parenthesis_balanced(self) -> bool:
        '''
        poperty to check if a parenthesis string is valid or not

        :: Return ::
        True if balanced else False
        '''
        open = ['(','{','[']
        close = [')','}',']']
        opened = []
        if self.parenthesis_String[0] in open:
            opened.append(self.parenthesis_String[0])
        else:
            return False
        for i in self.parenthesis_String[1:]:
            if i in open:
                opened.append(i)
            else:
                close_ind = close.index(i)
                if opened:
                    if open.index(opened[-1])==close_ind:
                        opened.pop()
                    else:
                        return False
                else:
                    return False
            
        if not opened:
            return True
        else:
            False
parenthesis_String = '[(])'
print(Solution(parenthesis_String).parenthesis_balanced)