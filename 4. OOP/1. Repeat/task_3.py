# inversions

def inversions(sequence) -> int:
    count = 0
    for i in range(len(sequence)):
        for j in range(len(sequence)):
            if i < j and sequence[i] > sequence[j]:
                count += 1
    
    return count