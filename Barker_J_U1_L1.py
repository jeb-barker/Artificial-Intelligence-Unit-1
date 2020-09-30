# Jeb Barker
# Sep. 25, 2020
import random


def getInitialState():
    x = "_12345678"
    l = list(x)
    random.shuffle(l)
    y = ''.join(l)
    return y


'''precondition: i<j
   swap characters at position i and j and return the new state'''


def swap(state, i, j):
    li = list(state)  # create a list of each character in state
    li[i], li[j] = li[j], li[i]  # swap the elements of li at i/j
    return "".join(s for s in li)  # join every element in li into a string


'''Generate a list which hold all children of the current state
   and return the list'''


def generate_children(state):
    sIndex = state.index("_")  # store index of space (not necessary, just saves a little bit of space)

<<<<<<< Updated upstream
    # return [swap(state, sIndex, j) for j, val in enumerate(list(state)) if not sIndex == j and (sIndex % 3 == j % 3 and abs(sIndex - j) <= 3) or ((sIndex - 1 == j and ((sIndex % 3) - 1 == j % 3)) or (sIndex + 1 == j and ((sIndex % 3) + 1 == j % 3)))]

    # This returns children in the order: UP, LEFT, RIGHT, DOWN.
    # THIS CODE IS MUCH FASTER THAN THE SAMPLE BELOW
    # The sample output returns the order: UP, LEFT, DOWN, RIGHT.
    # See code below for a match of sample output.

=======
    return [swap(state, sIndex, j) for j, val in enumerate(list(state)) if
            not sIndex == j and (sIndex % 3 == j % 3 and abs(sIndex - j) <= 3) or (
                        (sIndex - 1 == j and ((sIndex % 3) - 1 == j % 3)) or (
                            sIndex + 1 == j and ((sIndex % 3) + 1 == j % 3)))]
>>>>>>> Stashed changes
    # Return state after swapping space/j for every index in the given state. The following conditions are in order
    # in the line above. Make sure the space and the index you are checking isn't the same Check if the space and the
    # index you are checking are in the same column (Mod 3 produces this), only if the space and j are less than 4
    # spaces apart. Check of the character to the left/right of the space is in the same row using mod 3 +/- 1. E.X.
    # space at index 2, j at index 3: 2%3 + 1 != 3%3.
    children = []
    if (sIndex - 3) >= 0:
        children.append(swap(state, sIndex, sIndex-3))
    if (sIndex % 3) - 1 == (sIndex - 1) % 3:
        children.append(swap(state, sIndex, sIndex-1))
    if (sIndex + 3) < 9:
        children.append(swap(state, sIndex, sIndex+3))
    if (sIndex % 3) + 1 == (sIndex + 1) % 3:
        children.append(swap(state, sIndex, sIndex+1))
    return children

def display_path(n, explored):  # key: current, value: parent
    l = []
    while explored[n] != "s":  # "s" is initial's parent
        l.append(n)
        n = explored[n]
    # print()
    l = l[::-1]
    for i in l:
<<<<<<< Updated upstream
        # print(" ".join(i[0:3]), end="   ")  # with spaces
        print(i[0:3], end="   ")
    print()
    for j in l:
        # print(" ".join(j[3:6]), end="   ")  # with spaces
        print(j[3:6], end="   ")
    print()
    for k in l:
        # print(" ".join(k[6:9]), end="   ")  # with spaces
=======
        print(i[0:3], end="   ")
    print()
    for j in l:
        print(j[3:6], end="   ")
    print()
    for k in l:
>>>>>>> Stashed changes
        print(k[6:9], end="   ")
    print("\n\nThe shortest path length is :", len(l))
    # return ""


'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''


<<<<<<< Updated upstream
def BFS(initial_state):  # Note to whoever reads this: 8-puzzle DOES have unsolvable board states.
    # google odd number of inversions for more info
=======
def BFS(initial_state):  # Note to whoever reads this: 8-puzzle DOES have unsolvable board states. google odd number
    # of inversions for more info
>>>>>>> Stashed changes
    explored = {initial_state: "s"}
    nodeQueue = [[initial_state]]
    while nodeQueue:
        path = nodeQueue.pop(0)
        s = path[-1]
        if s == "_12345678":
            display_path(s, explored)
            return ""
        for state in generate_children(list(s)):
            if state not in explored:
                nodeQueue.append([state])
                explored[state] = s  # state is the child while s is the parent
<<<<<<< Updated upstream
                # display_path(nodeQueue, explored)  # not correct: only display once the goal condition is met.
=======
                # display_path(nodeQueue, explored)
    return "No Solution"
>>>>>>> Stashed changes


'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''


def DFS(initial):
    explored = {initial: "s"}
    nodeStack = [[initial]]
    while nodeStack:
        path = nodeStack.pop()
        s = path[-1]
        if s == "_12345678":
            display_path(s, explored)
<<<<<<< Updated upstream
        for state in generate_children(list(s)):  # add child to the stack/explored for every child generated.
            if state not in explored and state not in nodeStack:
                nodeStack.append([state])
                explored[state] = s  # state is current, s is parent.
=======
            return ""
        for state in reversed(generate_children(list(s))):
            if state not in explored and state not in nodeStack:
                nodeStack.append([state])
                explored[state] = s
    return "No Solution"
>>>>>>> Stashed changes


def main():
    # initial = getInitialState()
    initial = "_42135678"
    # print(initial)
    # print(generate_children(initial)) # Test generate children
<<<<<<< Updated upstream

    # print("BFS start with:\n", " ".join(initial[0:3]), "\n", " ".join(initial[3:6]), "\n", " ".join(initial[6:]), "\n")  # prints with spaces
    print("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
    print(BFS(initial))
    # print("DFS start with:\n", " ".join(initial[0:3]), "\n", " ".join(initial[3:6]), "\n", " ".join(initial[6:]), "\n")  # with spaces
=======
    print("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
    print(BFS(initial))
>>>>>>> Stashed changes
    print("DFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
    print(DFS(initial))


if __name__ == '__main__':
    main()
