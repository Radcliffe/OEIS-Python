from pydantic import AfterValidator, BaseModel, ValidationError
from typing import Annotated, List, Optional
from enum import Enum

# Line format: %x A000001 content. All the possible lines:

# %I A000001 Identification line (required)
# %S A000001 First line of sequence (required)
# %T A000001 2nd line of sequence.
# %U A000001 3rd line of sequence.
# %N A000001 Name (required)
# %D A000001 Detailed reference line.
# %D A000001 Detailed references (2).
# %H A000001 Link to other site.
# %H A000001 Link to other site (2).
# %F A000001 Formula.
# %F A000001 Formula (2).
# %Y A000001 Cross-references to other sequences.
# %A A000001 Author (required)
# %O A000001 Offset (required)
# %E A000001 Extensions, errors, etc.
# %e A000001 examples to illustrate initial terms.
# %p A000001 Maple program.
# %t A000001 Mathematica program.
# %o A000001 Program in another language.
# %K A000001 Keywords (required)
# %C A000001 Comments.

class OEISLineType(str, Enum):
    IDENTIFICATION = "%I"
    SEQUENCE = "%S"
    SECOND_LINE = "%T"
    THIRD_LINE = "%U"
    NAME = "%N"
    DETAILED_REFERENCE = "%D"
    LINK = "%H"
    FORMULA = "%F"
    CROSS_REFERENCES = "%Y"
    AUTHOR = "%A"
    OFFSET = "%O"
    EXTENSIONS = "%E"
    EXAMPLES = "%e"
    MAPLE_PROGRAM = "%p"
    MATHEMATICA_PROGRAM = "%t"
    OTHER_PROGRAM = "%o"
    KEYWORDS = "%K"
    COMMENTS = "%C"


def validate_sequence_id(sequence_id: str) -> str:
    """
    Validate the sequence ID format.
    """
    if len(sequence_id) != 7 or not sequence_id.startswith("A") or not sequence_id[1:].isdigit():
        raise ValueError(f"Invalid sequence ID format: {sequence_id}")
    return sequence_id


class OEISLine(BaseModel):
    """
    A class to represent a line in the OEIS file.
    """
    line_type: OEISLineType
    sequence_id: Annotated[str, AfterValidator(validate_sequence_id)]
    content: str
    language: Optional[str] = None

    def __str__(self):
        return f"{self.line_type.value} {self.sequence_id} {self.content}"




