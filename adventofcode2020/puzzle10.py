example = [
28,
33,
18,
42,
31,
14,
46,
20,
48,
47,
24,
23,
49,
45,
19,
38,
39,
11,
1,
32,
25,
35,
8,
17,
7,
9,
4,
2,
34,
10,
3,
]

my = [
67,
118,
90,
41,
105,
24,
137,
129,
124,
15,
59,
91,
94,
60,
108,
63,
112,
48,
62,
125,
68,
126,
131,
4,
1,
44,
77,
115,
75,
89,
7,
3,
82,
28,
97,
130,
104,
54,
40,
80,
76,
19,
136,
31,
98,
110,
133,
84,
2,
51,
18,
70,
12,
120,
47,
66,
27,
39,
109,
61,
34,
121,
38,
96,
30,
83,
69,
13,
81,
37,
119,
55,
20,
87,
95,
29,
88,
111,
45,
46,
14,
11,
8,
74,
101,
73,
56,
132,
23,

]

def fn(lst):
    lst.sort()
    ones = 0
    threes = 0
    for n in range(0, lst.__len__() - 1):
        curr = lst[n]
        next = lst[n + 1]
        if (next - curr) == 3:
            threes += 1
        elif (next - curr) == 1:
            ones += 1
    print(ones + 1)
    print(threes + 1)
    print((ones+1) * (threes+1))
    return

#fn(example)
#fn(my)

def fn2(lst):
    num_paths = {}
    lst.reverse()
    num_paths[max(lst)] = 1
    for adapter in lst[1:]:
        num_paths[adapter] = num_paths.get(num_paths+1, 0) + num_paths.get(num_paths+2, 0) + num_paths.get(num_paths+3, 0)
    return num_paths[0]

#fn2(example)
fn2(my)