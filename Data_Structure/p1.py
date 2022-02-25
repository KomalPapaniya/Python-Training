List =  [11, 45, 8, 23, 14, 12, 78, 45, 89, 4, 0, 21]
result = []
part = 3
n = int(len(List)/part)
i = 0    
while(i < len(List)):
    # print(i)
    chunk = List[i:i+n]
    chunk.reverse()
    # print(chunk)
    result.append(chunk)
    i += n
print(result)