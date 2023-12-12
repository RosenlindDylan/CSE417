from pprint import pprint
def SmallestSubsetSum(S, n, K):
    Opt = [[(float('inf'), []) for _ in range(K + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        Opt[i][0] = (0, [])

    for i in range(1, n + 1):
        for j in range(1, K + 1):
            if S[i - 1] > j:
                Opt[i][j] = Opt[i - 1][j]
            else:
                incl_size = Opt[i - 1][j - S[i - 1]][0] + 1
                incl_set = Opt[i - 1][j - S[i - 1]][1] + [i - 1]
                excl_size = Opt[i - 1][j][0]
                excl_set = Opt[i - 1][j][1]

                if incl_size < excl_size:
                    Opt[i][j] = (incl_size, incl_set)
                else:
                    Opt[i][j] = (excl_size, excl_set)
    pprint(Opt)
    return Opt[n][K]

states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
    "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
    "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
    "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
    "West Virginia", "Wisconsin", "Wyoming"
]

electoral_votes_2024 = [
    9, 3, 11, 6, 54, 10, 7, 3, 3, 30, 16, 4, 4, 19, 11, 6, 6, 8, 8, 4, 10, 11, 15, 10, 6, 10, 4, 5, 6, 4,
    14, 5, 28, 16, 3, 17, 7, 8, 19, 4, 9, 3, 11, 40, 6, 3, 13, 12, 4, 10, 3
]

result = SmallestSubsetSum(electoral_votes_2024, len(electoral_votes_2024), 269)
print("Size of the smallest subset sum:", result[0])
for state_idx in result[1]:
    print(states[state_idx])
