from LatexTemplater.TemplateFilter import TemplateFilter
from LatexTemplater.TemplateCore import TemplateCore
from typing import Dict, Callable, List
import os
def registrationInfo() -> Dict[str, Callable[[any], str]]:
    return {
        ProjectFilter.name: ProjectFilter.filter
    }


class ProjectFilter(TemplateFilter):
    name = "Project"
    def filter(val: any) -> str:
        name = str(val["name"])
        parent = str(val["parent"])
        startDate = str(val["start"])
        stopDate = str(val["stop"])
        role = str(val["role"])
        description = str(val["description"])
        accomplishments = val["accomplishments"]
        inst = TemplateCore.instance()
        return (inst.filter("KeepTogether", 
                           inst.filter("DoubleLineEntry", [f"{name}({parent})",
                                                           f'{startDate} - {stopDate}',
                                                           f'{role}',
                                                           ""
                                                           ]
                                       ) + description + os.linesep + 
                            inst.filter("Bulleted", accomplishments) + os.linesep
                            ))
