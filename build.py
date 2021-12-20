#! /usr/bin/env python

from LatexTemplater.TemplatePluginManager import load_plugins
from LatexTemplater.TemplateCore import TemplateCore

load_plugins(["ResumeFilters"])


if __name__ == '__main__':
    inst = TemplateCore.instance()
    inst.templateDir = "Templates"
    inst.resultsFolder = "Education"
    inst.render("Education", "vars.json")
    inst.render("Work", "vars.json")
    inst.render("Projects", "vars.json")
    inst.render("Skills", "vars.json")
