from LatexTemplater.TemplateFilter import TemplateFilter
from typing import Dict, Callable, List
import os

def registrationInfo() -> Dict[str, Callable[[any], str]]:
    return {
        DoubleLineEntryFilter.name: DoubleLineEntryFilter.filter
    }


class DoubleLineEntryFilter(TemplateFilter):
    name = "DoubleLineEntry"
    
    def filter(entries: list[str]) -> str:
        return (r'\entry{' + entries[0] + r'} \hfill \textbf{' + entries[1] + r"}\\" + os.linesep + 
                entries[2] + r"\hfill " + entries[3] + r"\\")
