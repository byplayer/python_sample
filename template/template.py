from string import Template

file = open('template', 'r')
t = Template(file.read())
file.close()

out = open('out.txt', 'w')

out.write(t.substitute(REPLACE='ZZZ'))

out.close()
