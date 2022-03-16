# Slice list into 3 equal chunks and reverse each chunk
# Sample:  [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Result: [[8, 45, 11], [12, 14, 23], [89, 45, 78]]

List =  [11, 45, 8, 23, 14, 12, 78, 45, 89, 4, 0, 21]
result = []
total_chunks = 3
len_of_each_chunk = int(len(List)/total_chunks)
index = 0    
while(index < len(List)):
    # print(i)
    chunk = List[index:index + len_of_each_chunk]
    chunk.reverse()
    # print(chunk)
    result.append(chunk)
    index += len_of_each_chunk
print(result)