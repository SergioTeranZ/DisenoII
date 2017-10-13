-- --------------------------------------------------
-- Entrega 1 : 	Resolución del problema de la mochila 
--				con Progrmacion Dinámica
--
--Autores:
-- 	Marialicia Suarez
-- 	12-10621
-- 	Sergio Teran
-- 	11-11020
--	
--	13/10/2017
-- --------------------------------------------------

module Optimo where
import Data.List
import Data.Function(on)

-- SOLUCION EXPONENCIAL
mochila' :: [(Int,Int)] -> Int -> Int
mochila' [] _ = 0
mochila' ((pj,bj):xs) c = if c-pj < 0 then 0 else (mochila' xs c) `max`  ((mochila' xs (c-pj)) + bj)
-------------------

-- version CHINO+MANDARIN AVANZADO
mochila :: [(Int, Int)] -> [(Int, Int)] -> Int -> [(Int, Int)]
mochila xs [] _   = xs
mochila xs ys max =
    foldr (maxDe) [] (xs: [mochila (y:xs) (delete y ys) max | y <- ys, peso(y:xs) <= max ] ) 
                           where
                             peso = sum . map snd

maxDe :: [(Int, Int)] -> [(Int, Int)] -> [(Int, Int)]
maxDe a b = maximumBy (compare `on` valueOf) [a,b] where
            valueOf = sum . map fst