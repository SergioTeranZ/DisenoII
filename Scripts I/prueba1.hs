import Optimo
-- -----------
-- PRUEBAS 10
-- -----------
p1::[(Int,Int)]
p1 = [(1, 9), (1, 19), (2, 13), (3, 8), (4, 3), (4, 14), (6, 14), (10, 13), (16, 12)]

c1::Int
c1 = 11

-- Result: 63
-- * --
p2::[(Int,Int)]
p2 = [(1, 10), (10, 9), (10, 13), (11, 10), (11, 12), (12, 6), (12, 11), (18, 17), (19, 18)]

c2::Int
c2 = 45

-- Result: 56

-- -----------
-- PRUEBAS 20
-- -----------
p3::[(Int,Int)]
p3 = [(3, 4), (4, 12), (4, 28), (6, 16), (7, 36), (8, 6), (8, 15), (10, 1), (10, 18), (19, 28), (22, 15), (23, 4), (23, 8), (25, 20), (27, 32), (29, 17), (31, 20), (34, 20), (38, 9)]

c3::Int
c3 = 121

--Result: 215
-- * --
p4::[(Int,Int)]
p4 = [(1, 28), (1, 37), (2, 34), (3, 37), (9, 11), (11, 16), (14, 38), (15, 15), (17, 27), (18, 19), (18, 26), (24, 37), (25, 3), (25, 31), (28, 33), (29, 13), (32, 27), (38, 38), (39, 16)]

c4::Int
c4 = 57
-- Result: 227

-- -----------
-- PRUEBAS 30
-- -----------
p5::[(Int,Int)]
p5 = [(1, 21), (3, 38), (3, 53), (8, 55), (9, 5), (9, 58), (11, 6), (11, 19), (16, 15), (20, 25), (25, 2), (25, 26), (27, 40), (29, 2), (31, 43), (34, 35), (36, 8), (39, 7), (41, 9), (42, 36), (46, 42), (46, 59), (48, 51), (49, 29), (51, 33), (51, 41), (53, 17), (57, 37), (58, 53)]

c5::Int
c5 = 166

--Result: 412
-- * --
p6::[(Int,Int)]
p6 = [(1, 46), (1, 54), (8, 40), (10, 12), (10, 22), (14, 3), (16, 8), (20, 11), (20, 28), (22, 27), (23, 8), (24, 52), (28, 4), (28, 18), (29, 24), (31, 8), (32, 34), (35, 23), (36, 7), (38, 38), (44, 45), (45, 21), (49, 48), (50, 3), (52, 49), (54, 26), (55, 28), (56, 49), (59, 34)]

c6::Int
c6 = 97
-- Result: 281
-- ************* --

-- -----------
-- PRUEBAS 40
-- -----------
p7::[(Int,Int)]
p7 = [(5, 69), (9, 51), (11, 2), (12, 25), (13, 25), (14, 58), (14, 72), (17, 4), (17, 42), (17, 74), (18, 22), (19, 26), (19, 62), (22, 43), (22, 53), (23, 66), (29, 8), (29, 53), (31, 26), (33, 37), (35, 40), (38, 40), (39, 1), (41, 38), (44, 72), (46, 34), (47, 78), (49, 1), (54, 36), (54, 54), (55, 33), (60, 21), (61, 18), (61, 24), (64, 1), (64, 47), (64, 67), (68, 10), (72, 71)]

c7::Int
c7 = 66

--Result: ---
-- * --
-- p8::[(Int,Int)]
-- p8 = [(1, 46), (1, 54), (8, 40), (10, 12), (10, 22), (14, 3), (16, 8), (20, 11), (20, 28), (22, 27), (23, 8), (24, 52), (28, 4), (28, 18), (29, 24), (31, 8), (32, 34), (35, 23), (36, 7), (38, 38), (44, 45), (45, 21), (49, 48), (50, 3), (52, 49), (54, 26), (55, 28), (56, 49), (59, 34)]
-- 
-- c8::Int
-- c8 = 248
-- Result: ---
-- ************* --

-- -----------
-- PRUEBAS 50
-- -----------
p9::[(Int,Int)]
p9 = [(3, 89), (5, 84), (6, 38), (8, 71), (15, 90), (19, 26), (22, 54), (26, 86), (27, 74), (29, 36), (30, 27), (34, 97), (36, 16), (37, 78), (39, 99), (40, 62), (41, 82), (43, 12), (46, 37), (49, 46), (50, 57), (56, 90), (65, 72), (69, 75), (71, 56), (73, 40), (75, 29), (79, 15), (80, 91), (85, 71), (86, 18), (86, 82), (87, 3), (88, 9), (88, 57), (92, 35), (93, 97), (95, 80), (97, 23)]

c9::Int
c9 = 485

--Result: 1231
-- * --
p10::[(Int,Int)]
p10 = [(1, 51), (2, 80), (4, 38), (10, 85), (18, 89), (21, 94), (25, 63), (27, 42), (28, 46), (29, 83), (35, 12), (36, 53), (37, 88), (40, 60), (46, 80), (47, 23), (50, 22), (56, 16), (56, 59), (60, 73), (61, 11), (63, 27), (66, 21), (71, 94), (76, 90), (78, 88), (79, 33), (79, 84), (80, 54), (81, 54), (82, 24), (84, 73), (85, 65), (92, 97), (93, 9), (93, 24), (95, 36), (96, 50), (97, 78)]

c10::Int
c10 = 211
-- Result: 770
-- ************* --

runTest':: [(Int,Int)]-> Int -> Int
runTest' = mochila'

--runTest:: [(Int,Int)]-> Int -> [(Int,Int)]
--runTest p c = mochila [] p c

--result p c = sum $ map snd (runTest p c)
