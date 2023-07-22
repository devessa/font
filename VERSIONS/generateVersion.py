#!/usr/bin/python3

dreamsheader = """[buildPlans.dreams]
family = "dreams"
spacing = "normal"
serifs = "sans"
no-cv-ss = true
export-glyph-names = true"""
dreamersheader = """[buildPlans.dreamers]
family = "dreamers"
spacing = "term"
serifs = "sans"
no-cv-ss = true
export-glyph-names = true"""
dreamilyheader = """[buildPlans.dreamily]
family = "dreamily"
spacing = "quasi-proportional"
serifs = "sans"
no-cv-ss = true
export-glyph-names = true"""

rulesNormal = """capital-d = "more-rounded-serifless"
capital-w = "straight-serifless"
capital-z = "curly-serifless"
capital-x = "straight-serifless"
capital-q = "horizontal-tailed"
capital-i = "short-serifed"
capital-f = "serifless"
capital-c = "serifless"
capital-j = "flat-hook-serifed"
capital-b = "standard-serifless"
capital-g = "toothless-corner-serifless-hookless"
capital-k = "straight-serifless"
capital-y = "straight-serifless"
capital-u = "toothless-corner-serifless"
capital-n = "asymmetric-serifless"
capital-r = "curly-serifless"
a = "single-storey-earless-corner-serifless"
b = "toothless-corner-serifless"
c = "serifless"
d = "toothless-corner-serifless"
f = "flat-hook-serifless"
g = "single-storey-flat-hook-earless-corner"
i = "tailed-serifed"
j = "flat-hook-serifed"
k = "curly-serifless"
l = "hooky"
m = "short-leg-serifless"
n = "earless-corner-straight-serifless"
q = "earless-corner-straight-serifless"
p = "earless-corner-serifless"
r = "earless-corner-serifless"
s = "serifless"
t = "standard"
u = "toothless-corner-serifless"
v = "straight-serifless"
w = "straight-serifless"
x = "straight-serifless"
y = "straight-turn-serifless"
z = "curly-serifless"
long-s = "flat-hook-serifless"
eszet = "longs-s-lig"
lower-alpha = "tailed-barred"
lower-delta = "flat-top"
lower-lambda = "straight-turn"
lower-xi = "rounded"
cyrl-capital-ka = "straight-serifless"
cyrl-ka = "straight-serifless"
cyrl-capital-u = "straight-turn-serifless"
one = "no-base"
two = "curly-neck"
three = "two-arcs"
four = "semi-open-non-crossing"
five = "vertical-upper-left-bar"
six = "straight-bar"
seven = "curly-serifed"
eight = "crossing"
nine = "straight-bar"
zero = "slashed-split"
asterisk = "penta-low"
underscore = "low"
pilcrow = "low"
caret = "low"
paren = "large-contour"
brace = "curly-flat-boundary"
number-sign = "slanted-open"
ampersand = "closed"
at = "compact"
dollar = "interrupted"
cent = "bar-interrupted"
percent = "rings-continuous-slash"
bar = "natural-slope"
lig-ltgteq = "slanted"
lig-neq = "more-slanted"
question = "smooth"
punctuation-dot = "square"
diacritic-dot = "square"
lig-equal-chain = "without-notch"
lig-hyphen-chain = "without-notch"
"""
rulesItalic = """capital-j = "serifed"
capital-u = "toothless-rounded-serifless"
a = "single-storey-earless-rounded-serifless"
b = "toothless-rounded-serifless"
d = "toothless-rounded-serifless"
e = "rounded"
f = "flat-hook-tailed"
g = "single-storey-flat-hook-earless-rounded"
i = "tailed-serifed"
j = "serifed"
k = "cursive-serifless"
l = "tailed-serifed"
m = "short-leg-serifless"
n = "earless-rounded-straight-serifless"
p = "earless-rounded-serifless"
q = "earless-rounded-straight-serifless"
r = "earless-rounded-serifless"
t = "standard"
u = "toothless-rounded-serifless"
v = "cursive-serifless"
w = "straight-serifless"
y = "cursive-serifless"
z = "curly-serifless"
one = "no-base-top-cut"
"""

footerdreams = """[buildPlans.dreams.widths.normal]
shape = 600
menu = 5
css = "normal"

[buildPlans.dreams.metric-override]
powerlineScaleX = 1
powerlineScaleY = 1

[buildPlans.dreams.ligations]
"""
footerdreamers = """[buildPlans.dreamers.widths.normal]
shape = 600
menu = 5
css = "normal"

[buildPlans.dreamers.metric-override]
powerlineScaleX = 1
powerlineScaleY = 1

[buildPlans.dreamers.ligations]
"""
footerdreamily = """[buildPlans.dreamily.widths.normal]
shape = 600
menu = 5
css = "normal"

[buildPlans.dreamily.metric-override]
powerlineScaleX = 1
powerlineScaleY = 1

[buildPlans.dreamily.ligations]
"""

version = "dreams"
f = open(version + ".toml", "w")

# file-finally
def generate_filenally():
    filenally = ""
    filenally += dreamsheader
    filenally += "\n\n"
    filenally += "[buildPlans.dreams.variants.design]\n"
    filenally += rulesNormal
    filenally += "\n\n"
    filenally += "[buildPlans.dreams.variants.italic]\n"
    filenally += rulesItalic
    filenally += "\n\n"
    filenally += footerdreams
    filenally += "\n\n"
    filenally += dreamersheader
    filenally += "\n\n"
    filenally += "[buildPlans.dreamers.variants.design]\n"
    filenally += rulesNormal
    filenally += "\n\n"
    filenally += "[buildPlans.dreamers.variants.italic]\n"
    filenally += rulesItalic
    filenally += "\n\n"
    filenally += footerdreamers
    filenally += "\n\n"
    filenally += dreamilyheader
    filenally += "\n\n"
    filenally += "[buildPlans.dreamily.variants.design]\n"
    filenally += rulesNormal
    filenally += "\n\n"
    filenally += "[buildPlans.dreamily.variants.italic]\n"
    filenally += rulesItalic
    filenally += "\n\n"
    filenally += footerdreamily
    filenally += "\n\n"
    return filenally

f.write(generate_filenally())
f.close()
