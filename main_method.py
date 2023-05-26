import regular_expressions as x

file = open("texto.txt", "r", encoding="utf-8")
contents = file.read()
file.close()

test = open("new_file.txt", "w", encoding="utf-8")
contents = x.supr_special_characters(contents)
test.write(x.summary(contents) + x.body(contents))
test.close()
