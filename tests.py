import unittest

from solution import count_paper_streets


def add_cases(cls):
    cases = [
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(0, 1), (1, 0), (1, 2), (2, 1)],
            'expected': 0,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(1, 0), (1, 2), (2, 1)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(0, 1), (1, 2), (2, 1)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(0, 1), (1, 0), (2, 1)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(0, 1), (1, 0), (1, 2)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(1, 2), (2, 1)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(0, 1), (1, 0)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(0, 1), (1, 2)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(1, 0), (2, 1)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(1, 0), (1, 2)],
            'expected': 2,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(0, 1), (2, 1)],
            'expected': 2,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(0, 1)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(1, 0)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(1, 2)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [(2, 1)],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2],
            'y_intercepts': [0, 2],
            'homes': [],
            'expected': 1,
        },
        {
            'x_intercepts': [0, 2, 5, 7],
            'y_intercepts': [0, 3, 5, 7],
            'homes': [(0, 0), (0, 3), (0, 5), (0, 6), (0, 7), (1, 0), (1, 3), (1, 5), (1, 7), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 0), (4, 3), (4, 7), (5, 0), (5, 1), (5, 3), (5, 4), (5, 5), (5, 7), (6, 0), (6, 5), (6, 7), (7, 0), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)],
            'expected': 3,
        },
        {
            'x_intercepts': [0, 1, 2, 3, 4, 6, 9, 11, 12, 13, 14, 18, 19, 20, 21, 24, 27, 29, 31],
            'y_intercepts': [0, 3, 6, 7, 12, 14, 17, 18, 21, 22, 28, 30, 31],
            'homes': [(0, 1), (0, 4), (0, 9), (0, 10), (0, 11), (0, 15), (0, 16), (0, 19), (0, 20), (0, 23), (0, 24),
                      (0, 25), (0, 26), (0, 29), (0, 32), (1, 1), (1, 2), (1, 8), (1, 10), (1, 15), (1, 16), (1, 29),
                      (1, 32), (2, 1), (2, 2), (2, 4), (2, 8), (2, 10), (2, 13), (2, 15), (2, 16), (2, 20), (2, 23),
                      (2, 25), (2, 29), (3, 1), (3, 2), (3, 5), (3, 8), (3, 9), (3, 11), (3, 15), (3, 19), (3, 20),
                      (3, 23), (3, 25), (3, 27), (3, 29), (3, 32), (4, 8), (4, 19), (4, 20), (4, 25), (6, 5), (6, 9),
                      (6, 15), (6, 19), (6, 25), (6, 26), (6, 29), (9, 2), (9, 8), (9, 11), (9, 13), (9, 16), (9, 20),
                      (9, 23), (9, 24), (9, 25), (9, 26), (9, 29), (11, 4), (11, 9), (11, 10), (11, 15), (11, 20),
                      (11, 23), (11, 24), (11, 25), (11, 26), (11, 27), (11, 32), (12, 2), (12, 8), (12, 13), (12, 15),
                      (12, 16), (12, 20), (12, 23), (12, 24), (12, 25), (12, 29), (13, 1), (13, 2), (13, 4), (13, 10),
                      (13, 11), (13, 19), (13, 20), (13, 23), (13, 29), (13, 32), (14, 2), (14, 4), (14, 16), (14, 26),
                      (14, 32), (18, 2), (18, 4), (18, 8), (18, 10), (18, 11), (18, 16), (18, 25), (18, 26), (19, 10),
                      (19, 11), (19, 15), (19, 16), (19, 20), (19, 25), (19, 29), (20, 8), (20, 10), (20, 11), (20, 16),
                      (20, 19), (20, 20), (20, 23), (20, 24), (20, 27), (21, 1), (21, 2), (21, 4), (21, 5), (21, 9),
                      (21, 11), (21, 13), (21, 15), (21, 16), (21, 23), (21, 24), (21, 26), (21, 27), (24, 1), (24, 2),
                      (24, 9), (24, 10), (24, 15), (24, 19), (24, 20), (24, 24), (24, 29), (27, 2), (27, 5), (27, 9),
                      (27, 25), (27, 29), (27, 32), (29, 1), (29, 2), (29, 8), (29, 9), (29, 11), (29, 15), (29, 19),
                      (29, 25), (29, 32), (31, 1), (31, 2), (31, 9), (31, 10), (31, 11), (31, 13), (31, 15), (31, 23),
                      (31, 29), (5, 0), (7, 0), (8, 0), (17, 0), (22, 0), (23, 0), (25, 0), (30, 0), (5, 3), (8, 3),
                      (10, 3), (23, 3), (25, 3), (26, 3), (28, 3), (5, 6), (7, 6), (8, 6), (15, 6), (16, 6), (17, 6),
                      (23, 6), (26, 6), (28, 6), (30, 6), (32, 6), (10, 7), (15, 7), (16, 7), (17, 7), (28, 7), (5, 12),
                      (7, 12), (16, 12), (17, 12), (23, 12), (28, 12), (5, 14), (8, 14), (10, 14), (16, 14), (25, 14),
                      (30, 14), (32, 14), (15, 17), (16, 17), (17, 17), (25, 17), (28, 17), (32, 17), (7, 18), (8, 18),
                      (10, 18), (16, 18), (17, 18), (25, 18), (26, 18), (28, 18), (32, 18), (5, 21), (7, 21), (10, 21),
                      (15, 21), (23, 21), (26, 21), (28, 21), (30, 21), (32, 21), (7, 22), (8, 22), (16, 22), (23, 22),
                      (26, 22), (32, 22), (8, 28), (10, 28), (17, 28), (23, 28), (26, 28), (30, 28), (32, 28), (8, 30),
                      (10, 30), (16, 30), (17, 30), (22, 30), (23, 30), (25, 30), (26, 30), (30, 30), (7, 31), (10, 31),
                      (15, 31), (16, 31), (17, 31), (23, 31), (26, 31), (28, 31)],
            'expected': 13,
        },
    ]

    for i, case in enumerate(cases):
        setattr(cls, 'test_case_{}'.format(i), lambda self, case=case: self.base(case))
    return cls


@add_cases
class CountPaperStreetsTests(unittest.TestCase):
    def base(self, case):
        count = count_paper_streets(case['x_intercepts'], case['y_intercepts'], case['homes'])
        if count != case['expected']:
            x_intercepts = set(case['x_intercepts'])
            y_intercepts = set(case['y_intercepts'])
            homes = set(case['homes'])
            width = max(x_intercepts)
            height = max(y_intercepts)
            rows = ["Expected: {}, Counted: {}".format(case['expected'], count)]
            for y in range(height, -1, -1):
                y_separator = '-' if y in y_intercepts else ' '
                line = y_separator * 3
                intersections = []
                for x in range(width+1):
                    if (x, y) in homes:
                        intersections.append('X')
                    elif x in x_intercepts and y in y_intercepts:
                        intersections.append('+')
                    elif x in x_intercepts:
                        intersections.append('|')
                    else:
                        intersections.append(y_separator)
                rows.append('{:<3}{}'.format(y, line.join(intersections)))
                if y:
                    rows.append('   {}'.format('   '.join(('|' if x in x_intercepts else ' ' for x in range(width+1)))))

            rows.append(''.join(('{:4}'.format(x) for x in range(width+1))))

            self.assertEqual(case['expected'], count, msg='\n'*2 + '\n'.join(rows))



