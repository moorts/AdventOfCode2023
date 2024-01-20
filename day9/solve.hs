allZero :: [Integer] -> Bool
allZero = all (==0)

recurse :: [Integer] -> [Integer]
recurse l@(x:xs) = zipWith (-) xs l

handleLine :: [Integer] -> Integer
handleLine l
    | allZero l = 0
    | otherwise = last l + handleLine (recurse l)

handleLine' :: [Integer] -> Integer
handleLine' l
    | allZero l = 0
    | otherwise = head l - handleLine' (recurse l)
    

parseLine :: String -> [Integer]
parseLine = (map read) . words

main :: IO ()
main = do
    contents <- lines <$> readFile "data"
    result1 <- return $ sum $ map (handleLine . parseLine) contents
    result2 <- return $ sum $ map (handleLine' . parseLine) contents
    -- You can use handleLine for part2 (buuuuuuut shouldn't):
    -- result3 <- return $ sum $ map (handleLine . (map ((-1)*)) . reverse . parseLine) contents
    print(result1)
    print(result2)
