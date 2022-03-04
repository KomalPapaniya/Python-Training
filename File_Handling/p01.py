question_file = open('Questions.txt', 'r')
answer_file = open('Answers.txt', 'r')
output_file = open("Notes.txt", "w")

q_dict = {}
a_dict = {}

for line in question_file:
    values = line.split(". ")
    q_dict[int(values[0])] = values[1][:-1]
# print(q_dict)

for line in answer_file:
    values = line.split(". ")
    a_dict[int(values[0])] = values[1][:-1]
# print(a_dict)

for key1 in sorted(q_dict):
    for key in a_dict.keys():
        if key1 == key:
            output_file.write("{}. {}\n".format(key1, q_dict[key1]))
            output_file.write("{}\n".format(a_dict[key]))

output_file = open("Notes.txt", "r")
print(output_file.read())
output_file.close()
