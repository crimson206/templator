import unittest
from pydantic import BaseModel
from typing import List, Dict

from crimson.templator import (
    format_insert_loop,
)
from crimson.templator.utils import (
    convert_list_to_kwargs_list,
)


class TestSafeGuard(unittest.TestCase):
    def test_loop_kwargs_list(self):
        kwargs1 = {
            "name": "Jone",
            "age": "13",
            "address": "London",
        }

        kwargs2 = {
            "name": "Amy",
            "age": "25",
            "address": "Erlangen",
        }

        kwargs_list = [kwargs1, kwargs2]

        template = r"""{
    name : \[name\],
    age : \[age\],
    address : \[address\],
},"""
        expected_formatted = """{
    name : Jone,
    age : 13,
    address : London,
},
{
    name : Amy,
    age : 25,
    address : Erlangen,
},"""

        formatted = format_insert_loop(template=template, kwargs_list=kwargs_list)

        self.assertEqual(formatted, expected_formatted)

    def text_loop_list(self):
        # Setting
        class InputProps(BaseModel):
            template: str
            kwargs_list: List[Dict[str, str]]
            open: str = r"\["
            close: str = r"\]"
            safe: bool = True

        fields = InputProps.model_fields.keys()
        kwargs_list = convert_list_to_kwargs_list(inputs=fields, shared_key="field")
        template = r"""\[arg\]=\[arg\]"""
        expected_formatted = """template=template
kwargs_list=kwargs_list
open=open
close=close
safe=safe"""

        # Action
        formatted = format_insert_loop(template=template, kwargs_list=kwargs_list)

        # Assertion
        self.assertEqual(formatted, expected_formatted)


if __name__ == "__main__":
    unittest.main()
