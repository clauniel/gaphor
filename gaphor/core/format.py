"""Format() and parse() provide a simple interface to:

1. format a model element to text
2. Update model element contents based on text
"""

from functools import singledispatch

from gaphor.core.modeling import Diagram, Element, Relationship


@singledispatch
def format(el: Element, **kwargs) -> str:
    """Format an element."""
    raise TypeError(f"Format routine for type {type(el)} not implemented yet")


@singledispatch
def parse(el: Element, text: str) -> None:
    """Parse text and update `el` accordingly."""
    raise TypeError(f"Parsing routine for type {type(el)} not implemented yet")


@format.register(Diagram)
def format_diagram(el, **kwargs) -> str:
    if el.diagramType:
        return f"[{el.diagramType}] {el.name}"
    return el.name or ""


@parse.register(Diagram)
def parse_Diagram(el: Diagram, text: str) -> None:
    el.name = text


@format.register(Relationship)
def format_relationship(el):
    return el.__class__.__name__
