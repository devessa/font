#!/usr/bin/env python3

type_header = """[buildPlans.type]
family = "type"
spacing = "quasi-proportional"
serifs = "sans"
noCvSs = true
exportGlyphNames = true"""

normal = """
capital-d = "standard-serifless"
capital-g = "toothless-corner-serifless-hooked"
capital-i = "short-serifed"
capital-j = "serifless"
capital-k = "symmetric-connected-serifless"
capital-n = "asymmetric-serifless"
capital-q = "horizontal-tailed"
capital-r = "standing-serifless"
capital-x = "curly-serifless"
capital-y = "straight-serifless"
capital-z = "curly-serifless"
a = "single-storey-earless-corner-serifless"
f = "flat-hook-serifless"
g = "single-storey-serifless"
i = "serifless"
j = "flat-hook-serifed"
k = "symmetric-touching-serifless"
l = "serifed"
p = "earless-corner-serifless"
q = "earless-corner-straight-serifless"
r = "compact-serifless"
t = "flat-hook"
u = "toothed-serifless"
w = "straight-flat-top-serifless"
x = "curly-serifless"
z = "curly-serifless"
zero = "top-right-cutout"
one = "no-base-top-cut"
two = "straight-neck-serifless"
three = "flat-top-serifless"
five = "oblique-arched-serifless"
six = "straight-bar"
eight = "crossing-asymmetric"
nine = "straight-bar"
diacritic-dot = "square"
punctuation-dot = "square"
asterisk = "penta-low"
underscore = "low"
paren = "flat-arc"
brace = "curly-flat-boundary"
guillemet = "straight"
number-sign = "slanted"
ampersand = "closed"
at = "compact"
dollar = "through-cap"
question = "smooth"
cent = "through"
lig-equal-chain = "without-notch"
lig-hyphen-chain = "without-notch"
"""
italic = """
capital-j = "serifless"
a = "single-storey-earless-corner-tailed"
d = "toothed-serifless"
f = "flat-hook-serifless"
g = "single-storey-serifless"
i = "serifed"
j = "serifed"
k = "cursive-serifless"
r = "compact-serifless"
t = "bent-hook"
v = "cursive-serifless"
"""

version = "type"
f = open("/tmp/" + version + ".toml", "w")
f = open("/tmp/" + version + ".toml", "w")

# file-finally
def generate_filenally():
    filenally = ""
    filenally += type_header
    filenally += "\n\n"
    filenally += "[buildPlans.type.variants.design]"
    filenally += normal
    filenally += "\n"
    filenally += "[buildPlans.type.variants.italic]"
    filenally += italic
    return filenally

f.write(generate_filenally())
print("[info] generated type.toml")
print("[info] generated type.toml")
f.close()
