-- --------------------------------------------------
-- Entrega 1 : 	Resolución del problema de la mochila 
--				con Programción Dinámica
--
--Autores:
-- 	Marialicia Suarez
-- 	12-10621
-- 	Sergio Teran
-- 	11-11020
--	
--	13/10/2017
-- --------------------------------------------------

mochila :: [(Int,Int)] -> Int -> Int
mochila [] _ = 0
mochila ((pj,bj):xs) c = if c-pj < 0 then 0 else (mochila xs c) `max`  ((mochila xs (c-pj)) + bj)
