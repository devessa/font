#!/usr/bin/python3

code_header = """[buildPlans.code]
family = "code"
spacing = "normal"
serifs = "sans"
no-cv-ss = true
export-glyph-names = true"""

normal = """
capital-d = "standard-serifless"
capital-g = "toothless-corner-serifless-hooked"
capital-i = "short-serifed"
capital-j = "flat-hook-serifless"
capital-k = "symmetric-connected-serifless"
capital-n = "asymmetric-serifless"
capital-q = "horizontal-tailed"
capital-r = "standing-serifless"
capital-x = "curly-serifless"
capital-y = "straight-serifless"
capital-z = "curly-serifless"
a = "single-storey-earless-corner-serifless"
f = "flat-hook-serifless"
g = "single-storey-flat-hook-serifless"
i = "tailed-serifed"
j = "flat-hook-serifed"
k = "symmetric-connected-serifless"
l = "tailed-serifed"
p = "earless-corner-serifless"
q = "earless-corner-straight-serifless"
r = "hookless-serifless"
t = "flat-hook"
u = "toothless-rounded-serifless"
w = "straight-flat-top-serifless"
x = "curly-serifless"
z = "curly-serifless"
lower-lambda = "curly-turn"
zero = "tall-slashed-cutout"
one = "no-base"
two = "straight-neck"
three = "flat-top"
six = "closed-contour"
eight = "crossing-asymmetric"
nine = "closed-contour"
diacritic-dot = "round"
punctuation-dot = "round"
asterisk = "penta-low"
underscore = "low"
paren = "flat-arc"
brace = "curly-flat-boundary"
ampersand = "upper-open"
at = "fourfold"
dollar = "interrupted-cap"
question = "corner-flat-hooked"
cent = "bar-interrupted"
lig-equal-chain = "without-notch"
lig-hyphen-chain = "without-notch"
"""
italic = """
capital-j = "serifless"
a = "single-storey-earless-corner-tailed"
d = "toothed-serifless"
f = "flat-hook-tailed"
g = "single-storey-serifless"
i = "tailed-serifed"
j = "serifed"
k = "cursive-serifless"
r = "hookless-serifless"
t = "standard"
v = "cursive-serifless"
"""

version = "code"
f = open("/tmp/" + version + ".toml", "w")

# file-finally
def generate_filenally():
    filenally = ""
    filenally += code_header
    filenally += "\n\n"
    filenally += "[buildPlans.code.variants.design]"
    filenally += normal
    filenally += "\n"
    filenally += "[buildPlans.code.variants.italic]"
    filenally += italic
    return filenally

f.write(generate_filenally())
print("[info] generated code.toml")
f.close()
