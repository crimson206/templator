from crimson.templator import format_indent

template = r"""
    \{lines1\} some more text
        \{lines2\}
"""

lines1 = """\
1
2
3\
"""

lines2 = """\
a
b
c\
"""

print(format_indent(template=template, lines1=lines1, lines2=lines2))
