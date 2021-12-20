from LatexTemplater.TemplateCore import TemplateCore
from . import EducationFilter
from . import WorkFilter
from . import ProjectFilter
from . import SkillsFilter
from . import DoubleLineEntryFilter
from . import KeepTogetherFilter
from . import CSVFilter
from . import BulletedFilter


def initialize():
    """
    Registers all the types with the latex filter
    """
    instance = TemplateCore.instance()
    registrationFuncs = [
        EducationFilter.registrationInfo,
        DoubleLineEntryFilter.registrationInfo,
        KeepTogetherFilter.registrationInfo,
        CSVFilter.registrationInfo,
        WorkFilter.registrationInfo,
        BulletedFilter.registrationInfo,
        ProjectFilter.registrationInfo,
        SkillsFilter.registrationInfo
    ]
    for registerFunc in registrationFuncs:
        filterinfo = registerFunc()
        for name, filter in filterinfo.items():
            instance.registerFilter(name, filter)
