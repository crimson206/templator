# flake8: noqa E501

def format_insert(
    text: str,
    open: str = r"\[",
    close: str = r"\]",
    **kwargs
):
    for key, value in kwargs.items():
        pattern = open + key + close
        text = text.replace(pattern, value)

    return text

def format_indent(
    text: str,
    open: str = r"\{",
    close: str = r"\}",
    **kwargs
):
    for key, value in kwargs.items():
        text = _format_indent_single(text, key, value, open, close)

    return text

def add_prefix(text, prefix= " "*4):
    split = text.split('\n')
    text = prefix + f'\n{prefix}'.join(split)
    return text

def _format_indent_single(
    text: str,
    key:str,
    value:str,
    open: str = r"\{",
    close: str = r"\}",
):
    pattern = open + key + close
    new_lines = []
    for line in text.split('\n'):
        if line.find(pattern) != -1:
            _check_indent_line(line, pattern)
            indent = line[:line.find(pattern)]
            new_lines.append(add_prefix(value, indent))
        else:
            new_lines.append(line)
            
    return '\n'.join(new_lines)

def _check_indent_line(text: str, pattern:str):
    remaining_text = text.replace(pattern, '').strip()

    if remaining_text:
        raise ValueError(f"The line contains characters other than '{pattern}'")

    return True

