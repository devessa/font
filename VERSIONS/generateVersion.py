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
dreamingheader = """[buildPlans.dreaming]
family = "dreaming"
spacing = "quasi-proportional-extension-only"
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
a = "double-storey-serifless"
b = "toothed-serifless"
c = "serifless"
d = "toothed-serifless"
f = "flat-hook-serifless-crossbar-at-x-height"
g = "single-storey-flat-hook-serifless"
i = "hooky"
j = "flat-hook-serifed"
k = "curly-serifless"
l = "hooky"
m = "serifless"
n = "straight-serifless"
q = "earless-corner-straight-serifless"
p = "earless-corner-serifless"
r = "corner-hooked-serifless"
s = "serifless"
t = "flat-hook-short-neck2"
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
one = "no-base-top-cut"
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
rulesItalic = """a = "single-storey-earless-corner-serifless"
e = "rounded"
f = "serifless-crossbar-at-x-height"
g = "single-storey-earless-corner"
i = "tailed-serifed"
j = "serifed"
k = "cursive-serifless"
l = "tailed-serifed"
m = "serifless"
t = "standard"
u = "toothless-corner-serifless"
w = "straight-serifless"
y = "cursive-serifless"
z = "curly-serifless"
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
footerdreaming = """[buildPlans.dreaming.widths.normal]
shape = 600
menu = 5
css = "normal"

[buildPlans.dreaming.metric-override]
powerlineScaleX = 1
powerlineScaleY = 1

[buildPlans.dreaming.ligations]
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
    filenally += dreamingheader
    filenally += "\n\n"
    filenally += "[buildPlans.dreaming.variants.design]\n"
    filenally += rulesNormal
    filenally += "\n\n"
    filenally += "[buildPlans.dreaming.variants.italic]\n"
    filenally += rulesItalic
    filenally += "\n\n"
    filenally += footerdreaming
    filenally += "\n\n"
    return filenally

f.write(generate_filenally())
f.close()
