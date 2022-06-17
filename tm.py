
#TURING MACHINE SIMULATOR BY SRIKAR AND JAYANT
import sys
class turing:
    def __init__(self,state,head,tape):
        self.state = state
        self.head = head
        self.tape = tape

    def retstate(self):
        return self.state

    def rettape(self):
        return self.tape

    def rethead(self):
        return self.head

    def updateMachine(self,character_list):
        # Initial State
        if (self.state == 'q1'):
            if (self.tape[self.head] != 0):
                char_read = self.tape[self.head]
                char_index = character_list.index(char_read)
                self.state = ''.join(['p', str(char_index)])
                self.tape[self.head] = 0
                self.head += 1
            else:
                #if its 0, update state to qy
                self.state = 'qy'
                #update tape character to 0
                self.tape[self.head] = 0
                self.head += 1

        elif (self.state.startswith('p')):
            if (self.tape[self.head] != 0):
                self.state = self.state
                self.tape[self.head] = self.tape[self.head]
                self.head += 1
            else:
                ### STATE ### (r)
                self.state = ''.join(['r', self.state[1:]])
                ### WRITE ### (zero, unchanged)
                self.tape[self.head] = 0
                ### MOVE ### (left)
                self.head -= 1

        elif (self.state.startswith('r')):
            char_read = character_list[int(self.state[1:])]
            if (self.tape[self.head] != char_read and self.tape[
                self.head] != 0):  # zero is needed for strings of odd length
                ### STATE ### (qn)
                self.state = 'qn'
                ### WRITE ###
                self.tape[self.head] = self.tape[self.head]
                ### MOVE ### (left) (doesn't matter)
                self.head -= 1
            else:
                ### STATE ###
                self.state = 'q2'
                ### WRITE ### (zero)
                self.tape[self.head] = 0
                ### MOVE ### (left)
                self.head -= 1

        elif (self.state == 'q2'):
            if (self.tape[self.head] != 0):
                ### STATE ### (unchanged)
                self.state = 'q2'
                ### WRITE ### (unchanged)
                self.tape[self.head] = self.tape[self.head]
                ### MOVE ### (left)
                self.head -= 1
            else:
                ### STATE ### (q1)
                self.state = 'q1'
                ### WRITE ### (zero)
                self.tape[self.head] = 0
                ### MOVE ### (right)
                self.head += 1
