# Name:          Date:
import time


def generate_adjacents(current, words_set):
    ''' words_set is a set which has all words.
    By comparing current and words in the words_set,
    generate adjacents set of current and return it'''
    adj_set = set()
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    for pos, letter in enumerate(current):
        for newLet in (alpha[:alpha.index(letter)] + alpha[alpha.index(letter) + 1:]):
            newWord = current[:pos] + newLet + current[pos+1:]
            if newWord in words_set:
                adj_set.add(newWord)
    return adj_set


def check_adj(words_set):
    # This check method is written for words_6_longer.txt
    adj = generate_adjacents('listen', words_set)
    target = {'listee', 'listel', 'litten', 'lister', 'listed'}
    return (adj == target)


def bi_bfs(start, goal, words_set):
    '''The idea of bi-directional search is to run two simultaneous searches--
    one forward from the initial state and the other backward from the goal--
    hoping that the two searches meet in the middle.
    '''
    if start == goal: return []
    exploredf = {start: [start]}
    frontier = [start]

    backtier = [goal]
    exploredb = {goal: [goal]}

    while frontier and backtier:
        s = frontier.pop(0)
        # pathf = exploredf[s]
        if s in backtier:
            return exploredf[s][:-1] + exploredb[s][::-1]
        for adj in generate_adjacents(s, words_set):
            if adj not in exploredf:
                pathf = exploredf[s][:]
                pathf.extend([adj])
                frontier.append(adj)
                exploredf[adj] = pathf[:]
            if adj in exploredf:
                if len(exploredf[adj]) > len(pathf):
                    pathf.extend([adj])
                    frontier.append(adj)
                    exploredf[adj] = pathf[:]
        s2 = backtier.pop(0)
        # pathb = exploredb[s2]
        if s2 in frontier:
            return exploredf[s2][:-1] + exploredb[s2][::-1]
        for adj in generate_adjacents(s2, words_set):
            pathb = exploredb[s2][:]
            if adj not in exploredb:
                pathb.extend([adj])
                backtier.append(adj)
                exploredb[adj] = pathb[:]
            if adj in exploredb:
                if len(exploredb[adj]) > len(pathb):
                    pathb.extend([adj])
                    backtier.append(adj)
                    exploredb[adj] = pathb[:]
    return "No Solution :("


def main():
    filename = input("Type the word file: ")
    words_set = set()
    file = open(filename, "r")
    for word in file.readlines():
        words_set.add(word.rstrip('\n'))
    # print(generate_adjacents("listen", words_set))
    # print ("Check generate_adjacents():", check_adj(words_set))
    initial = input("Type the starting word: ")
    goal = input("Type the goal word: ")
    cur_time = time.time()
    path = (bi_bfs(initial, goal, words_set))
    if path != None:
        print(path)
        print("The number of steps: ", len(path))
        print("Duration: ", time.time() - cur_time)
    else:
        print("There's no path")


if __name__ == '__main__':
    main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''