class solution:
    
    suggetions = []

    def __init__(self,array_of_correct_spellings):
        self.array_of_correct_spellings = array_of_correct_spellings

    def spellChecker(self,query) ->list:
        if query in self.array_of_correct_spellings:
            return []
        
        else:
            while not self.suggetions:
                query = query[0:-1]
                for i in self.array_of_correct_spellings:
                    if query in i:
                        self.suggetions.append(i)
        
        return self.suggetions


print(solution(['ninaja', 'ninajas', 'ninaeteen', 'ninany']).spellChecker('ninjk'))

'''
Best case complexity - O(N)
worst case complexity - O(N*M) where M is the length of query
'''