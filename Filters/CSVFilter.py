from LatexTemplater.TemplateFilter import TemplateFilter
from LatexTemplater.TemplateCore import TemplateCore
from typing import Dict, Callable, List
import os
def registrationInfo() -> Dict[str, Callable[[any], str]]:
    return {
        CSVListFilter.name: CSVListFilter.filter
    }


class CSVListFilter(TemplateFilter):
    name = "CSV"
    def filter(csvlist: List[str]) -> str:
        return ", ".join(csvlist)
