"""
Read and parse each sequence from the directory ../oeisdata/seq
"""

import os
from pathlib import Path
from typing import List, Optional
import re
from models.oeis_models import OEISLine, OEISLineType, validate_sequence_id
from oeis_reader import OEISReader
