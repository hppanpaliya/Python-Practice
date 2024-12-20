def stone_piles(n):
    result = []
    current_stones = n
    
    for i in range(n):
        result.append(current_stones)
        current_stones += 2  
    
    return result

if __name__ == "__main__":
    n = 3
    assert stone_piles(n) == [3, 5, 7]