# class PlayerGenerator:
#     def __init__(self, players):
#         self.players = players
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
        
#             current_player = self.players[self.index]
#             self.index += 1

            
#             next_player = self.players[self.index]
            


#             return current_player, next_player

    



class PlayerGenerator:
    def __init__(self, players):
        self.players = players
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.players):
            current_player = self.players[self.index]
            self.index += 1

            if self.index < len(self.players):
                next_player = self.players[self.index]

            else:
                next_player = None
                self.index = 0
                
            return current_player, next_player
        raise StopIteration