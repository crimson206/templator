from typing import Dict, Any


def format_insert(
    # Text to convert.
    text: str,
    # Custom open bracket.
    open: str = r"\[",
    # Custom close bracket.
    close: str = r"\]",
    # Wrap values with str(value). 
    # Otherwise, values such as 1, None, True and non-string values will cause an error.
    safe: bool = True,
    # Target name & new text pairs.
    # Pass it like
    # 'format_insert(..., kwarg1='value1', kwarg2='value2')' or
    # 'format_insert(..., **dictionary)'
    **kwargs: Dict[str, str],
):
    """
    String format function with custom brackets.

    Parameters
    ----------
    text: str,
        Text to convert.
    open: str = r"\[",
        Custom open bracket.
    close: str = r"\]",
        Custom close bracket.
    **kwargs
        Target name & new text pairs.
        Pass it like
        'format_insert(..., kwarg1='value1', kwarg2='value2')' or
        'format_insert(..., **dictionary)'
    """
    for key, value in kwargs.items():
        if safe:
            value = _convert_to_str(value)

        pattern = open + key + close
        text = text.replace(pattern, value)

    return text


def format_indent(
    # Text to convert.
    text: str,
    # Custom open bracket.
    open: str = r"\{",
    # Custom close bracket.
    close: str = r"\}",
    # Wrap values with str(value). 
    # Otherwise, values such as 1, None, True and non-string values will cause an error.
    safe: bool = True,
    # Target name & new text pairs.
    # Pass it like
    # 'format_insert(..., kwarg1='value1', kwarg2='value2')' or
    # 'format_insert(..., **dictionary)'
    **kwargs: Dict[str, str],
):
    '''
    String format function with custom brackets.
    The line with the target pattern can't have other letter than the pattern.

    Parameters
    ----------
    text: str,
        Text to convert.
    open: str = r"\{",
        Custom open bracket.
    close: str = r"\}",
        Custom close bracket.
    **kwargs,
        Target name & new text pairs.
        Pass it like
        'format_insert(..., kwarg1='value1', kwarg2='value2')' or
        'format_insert(..., **dictionary)'
    '''
    for key, value in kwargs.items():
        if safe:
            value = _convert_to_str(value)
        text = _format_indent_single(text, key, value, open, close)

    return text

def _convert_to_str(value:Any):
    return str(value)

def add_prefix(
    # Parameters
    # ----------
    text: str,
    # Text to convert
    prefix: str = " " * 4
    # Prefix to be added to all the lines
):
    '''
    Parameters
    ----------
    text: str,
        Text to convert
    prefix: str = " " * 4
        Prefix to be added to all the lines
    '''
    split = text.split("\n")
    text = prefix + f"\n{prefix}".join(split)
    return text


def _format_indent_single(
    text: str,
    key: str,
    value: str,
    open: str = r"\{",
    close: str = r"\}",
):
    pattern = open + key + close
    new_lines = []
    for line in text.split("\n"):
        if line.find(pattern) != -1:
            _check_indent_line(line, pattern)
            indent = line[: line.find(pattern)]
            new_lines.append(add_prefix(value, indent))
        else:
            new_lines.append(line)

    return "\n".join(new_lines)


def _check_indent_line(text: str, pattern: str):
    remaining_text = text.replace(pattern, "").strip()

    if remaining_text:
        raise ValueError(f"The line contains characters other than '{pattern}'")

    return True
