from LatexTemplater.TemplateFilter import TemplateFilter
from LatexTemplater.TemplateCore import TemplateCore
from typing import Dict, Callable, List
import os
def registrationInfo() -> Dict[str, Callable[[any], str]]:
    return {
        EducationFilter.name: EducationFilter.filter
    }


class EducationFilter(TemplateFilter):
    name = "Education"
    def filter(val: any) -> str:
        school = str(val["school"])
        degree = str(val["degree"])
        GPA = str(val["GPA"])
        graduation = str(val["graduation"])
        awards = str(val["awards"])
        inst = TemplateCore.instance()
        return (inst.filter("KeepTogether", 
                           inst.filter("DoubleLineEntry", [f"{school}({degree})",
                                                           f'GPA: {GPA}',
                                                           f'Graduation: {graduation}',
                                                           awards
                                                           ]
                                       ) + inst.filter("CSV", val["RelevantClasses"]) + os.linesep
                            ))
