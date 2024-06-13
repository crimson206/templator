from typing import List, Any, Iterable


def convert_lines(lines: List[str]) -> str:
    return "\n".join(lines)


def convert_list_to_kwargs_list(inputs: Iterable[Any], shared_key: str):
    kwargs = [{shared_key: input} for input in inputs]
    return kwargs


def add_prefix(
    # Parameters
    # ----------
    text: str,
    # Text to convert
    prefix: str = " " * 4,
    # Prefix to be added to all the lines
):
    """
    Parameters
    ----------
    text: str,
        Text to convert
    prefix: str = " " * 4
        Prefix to be added to all the lines
    """
    split = text.split("\n")
    text = prefix + f"\n{prefix}".join(split)
    return text
