file = open("pelican.txt", 'a')
file.write("A wonderful bird is the pelican,\n" "His bill holds more than his belican.\n")
#file.write("His bill holds more than his belican.\n")
#file.close()

lines = ["He can take in his beak,\n" "Enough food for a week,\n" "But i'm damned to see how the helican.\n"]
file.writelines(lines)

file = open("pelican.txt", "r")
print(file.read())
file.close()