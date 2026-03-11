import matplotlib.pyplot as plt
import random

def plot_results(results, title):
    names = list(results.keys())
    values = list(results.values())

    plt.figure()
    plt.bar(names, values)
    plt.title(title)
    plt.xlabel("Candidates")
    plt.ylabel("Number of Wins")
    plt.show()


def condorcet_paradox(preferences):
    candidates = preferences[0]
    pairwise = {}

    for a in candidates:
        for b in candidates:
            if a == b:
                continue

            a_count = 0
            b_count = 0

            for pref in preferences:
                if pref.index(a) < pref.index(b):
                    a_count += 1
                else:
                    b_count += 1

            if a_count > b_count:
                pairwise[(a,b)] = a
            else:
                pairwise[(a,b)] = b

    for a in candidates:
        for b in candidates:
            for c in candidates:
                if a!=b and b!=c and a!=c:
                    if pairwise.get((a,b))==a and pairwise.get((b,c))==b and pairwise.get((c,a))==c:
                        return True

    return False


def generate_preferences(voters, candidates):
    prefs = []
    for _ in range(voters):
        ranking = candidates[:]
        random.shuffle(ranking)
        prefs.append(ranking)
    return prefs


def plurality_vote(preferences):
    count = {}
    
    for pref in preferences:
        first = pref[0]
        count[first] = count.get(first, 0) + 1

    return max(count, key=count.get)


def borda_count(preferences):
    scores = {}
    n = len(preferences[0])

    for pref in preferences:
        for i, candidate in enumerate(pref):
            scores[candidate] = scores.get(candidate, 0) + (n - i - 1)

    return max(scores, key=scores.get)


def condorcet(preferences):
    candidates = preferences[0]

    for c in candidates:
        wins = True
        for other in candidates:
            if c == other:
                continue

            c_count = 0
            o_count = 0

            for pref in preferences:
                if pref.index(c) < pref.index(other):
                    c_count += 1
                else:
                    o_count += 1

            if o_count > c_count:
                wins = False
                break

        if wins:
            return c

    return "No Condorcet Winner"


plurality_results = {}
borda_results = {}
condorcet_results = {}
disagreements = 0
paradox_count = 0


for _ in range(100):
    prefs = generate_preferences(50, ['A','B','C','D'])

    p = plurality_vote(prefs)
    b = borda_count(prefs)
    c = condorcet(prefs)
    if not (p == b == c):
        disagreements += 1
    
    if condorcet_paradox(prefs):
        paradox_count += 1
    plurality_results[p] = plurality_results.get(p,0)+1
    borda_results[b] = borda_results.get(b,0)+1
    condorcet_results[c] = condorcet_results.get(c,0)+1


print("Plurality results:", plurality_results)
print("Borda results:", borda_results)
print("Condorcet results:", condorcet_results)
print("Number of disagreements:", disagreements)
print("Condorcet paradox occurrences:", paradox_count)
plot_results(plurality_results, "Plurality Voting Results")
plot_results(borda_results, "Borda Count Results")
plot_results(condorcet_results, "Condorcet Voting Results")