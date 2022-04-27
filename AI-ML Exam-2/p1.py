inp = ['F', 'B', 'F', 'F', 'F', 'F', 'F', 'F', 'B', 'B', 'B', 'B', 'B'] # input list
# inp = ['F', 'B', 'F', 'B', 'F', 'B', 'F', 'B', 'F', 'B', 'F', 'B', 'F']
# inp = ['F', 'B', 'B', 'B', 'B', 'B', 'B', 'F', 'F', 'F', 'B', 'B', 'B']

start = end = 0
style = inp[0]  # forwards or backwards
op_list = []  # list containing start index, end index and style of set of similarly worn caps
for i, v in enumerate(inp):
    if v == style:
        end = i
    else:
        op_list.append((start, end, style))
        style = v
        start = i
        end = i
op_list.append((start, end, style))
# print(op_list)

if len(op_list) == 1:
    style = op_list[0][2]
    commands = 0
elif op_list[0][2] == op_list[-1][2]:
    style = op_list[1][2]
    commands = (len(op_list) - 1)/2
else:
    style = op_list[0][2]
    commands = len(op_list)/2
    
print(int(commands))

for tup in op_list:
    if tup[2] == style and commands != 0:
        if tup[0] == tup[1]:
            print('Flip {}'.format(tup[0]))
        elif commands == 0:
            print('No Flip')
        else:
            print('Flip {} to {}'.format(tup[0], tup[1]))
        