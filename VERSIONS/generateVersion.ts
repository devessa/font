#!/usr/bin/env -S deno run --allow-write

type TOML = string[][];

const fontAmount = 3;
const fontNames = ["bunni", "bunnit", "bunniq"];

const headers: TOML = [
  [
    "[buildPlans.bunni]",
    'family = "bunni"',
    'spacing = "normal"',
    'serifs = "sans"',
    "no-cv-ss = true",
    "export-glyph-names = true",
  ],
  [
    "[buildPlans.bunnit]",
    'family = "bunnit"',
    'spacing = "term"',
    'serifs = "sans"',
    "no-cv-ss = true",
    "export-glyph-names = true",
  ],
  [
    "[buildPlans.bunniq]",
    'family = "bunniq"',
    'spacing = "quasi-proportional-extension-only"',
    'serifs = "sans"',
    "no-cv-ss = true",
    "export-glyph-names = true",
  ],
];

const rulesNormal: TOML = [
  ['capital-d = "more-rounded-serifless"'],
  ['capital-z = "curly-serifless"'],
  ['capital-x = "straight-serifless"'],
  ['capital-q = "straight"'],
  ['capital-i = "short-serifed"'],
  ['capital-f = "serifless"'],
  ['capital-c = "serifless"'],
  ['capital-j = "serifless"'],
  ['capital-b = "standard-serifless"'],
  ['capital-g = "toothless-rounded-serifless-hooked"'],
  ['capital-k = "symmetric-connected-serifless"'],
  ['capital-y = "curly-serifless"'],
  ['capital-u = "toothed"'],
  ['capital-n = "asymmetric"'],
  ['capital-r = "curly"'],
  ['a = "single-storey-earless-corner-tailed"'],
  ['b = "toothless-corner"'],
  ['c = "serifless"'],
  ['d = "toothed-serifless"'],
  ['f = "flat-hook"'],
  ['g = "single-storey-earless-corner-flat-hook"'],
  ['i = "serifed-flat-tailed"'],
  ['j = "serifed"'],
  ['k = "symmetric-connected-serifless"'],
  ['l = "zshaped"'],
  ['m = "normal"'],
  ['q = "earless-corner"'],
  ['r = "corner-hooked"'],
  ['s = "serifless"'],
  ['t = "standard"'],
  ['u = "toothed"'],
  ['v = "straight"'],
  ['x = "straight-serifless"'],
  ['y = "straight-turn"'],
  ['z = "curly-serifless"'],
  ['long-s = "flat-hook"'],
  ['eszet = "longs-s-lig"'],
  ['lower-alpha = "tailed-barred"'],
  ['lower-delta = "flat-top"'],
  ['lower-lambda = "straight-turn"'],
  ['lower-xi = "rounded"'],
  ['cyrl-capital-ka = "straight-serifless"'],
  ['cyrl-ka = "straight-serifless"'],
  ['cyrl-capital-u = "straight-turn"'],
  ['one = "no-base"'],
  ['two = "curly-neck"'],
  ['three = "two-arcs"'],
  ['four = "closed"'],
  ['five = "vertical-upper-left-bar"'],
  ['six = "closed-contour"'],
  ['seven = "curly-serifless"'],
  ['eight = "crossing"'],
  ['nine = "closed-contour"'],
  ['zero = "slashed-split"'],
  ['asterisk = "hex-low"'],
  ['underscore = "low"'],
  ['pilcrow = "low"'],
  ['caret = "low"'],
  ['paren = "large-contour"'],
  ['brace = "curly-flat-boundary"'],
  ['number-sign = "slanted"'],
  ['ampersand = "closed"'],
  ['at = "short"'],
  ['dollar = "interrupted"'],
  ['cent = "bar-interrupted"'],
  ['percent = "rings-continuous-slash"'],
  ['bar = "force-upright"'],
  ['lig-ltgteq = "slanted"'],
  ['lig-neq = "more-slanted"'],
  ['question = "smooth"'],
  ['punctuation-dot = "round"'],
  ['diacritic-dot = "round"'],
];
const rulesItalic: TOML = [
  ['capital-g = "toothless-rounded-serifless-hooked"'],
  ['capital-k = "symmetric-connected-serifless"'],
  ['a = "single-storey-earless-corner-serifless"'],
  ['b = "toothless-corner"'],
  ['c = "serifless"'],
  ['d = "toothed-serifless"'],
  ['e = "rounded"'],
  ['f = "flat-hook"'],
  ['g = "single-storey-serifless"'],
  ['h = "straight"'],
  ['i = "tailed-serifed"'],
  ['j = "serifed"'],
  ['k = "cursive-serifless"'],
  ['l = "tailed-serifed"'],
  ['m = "normal"'],
  ['s = "bilateral-inward-serifed"'],
  ['t = "standard"'],
  ['u = "toothed"'],
  ['v = "straight"'],
  ['w = "straight"'],
  ['y = "straight-turn"'],
  ['z = "curly-serifless"'],
];

const footers: TOML = [
  [
    "[buildPlans.bunni.widths.normal]",
    "shape = 600",
    "menu = 5",
    'css = "normal"',
    "\n",
    "[buildPlans.bunni.metric-override]",
    "powerlineScaleX = 1",
    "powerlineScaleY = 1",
    "\n",
    "[buildPlans.bunni.ligations]",
    'inherits = "calt"',
  ],
  [
    "[buildPlans.bunnit.widths.normal]",
    "shape = 600",
    "menu = 5",
    'css = "normal"',
    "\n",
    "[buildPlans.bunnit.metric-override]",
    "powerlineScaleX = 1",
    "powerlineScaleY = 1",
    "\n",
    "[buildPlans.bunnit.ligations]",
    'inherits = "calt"',
  ],
  [
    "[buildPlans.bunniq.widths.normal]",
    "shape = 600",
    "menu = 5",
    'css = "normal"',
    "\n",
    "[buildPlans.bunniq.metric-override]",
    "powerlineScaleX = 1",
    "powerlineScaleY = 1",
    "\n",
    "[buildPlans.bunniq.ligations]",
    'inherits = "calt"',
  ],
];

const rulesNormalList = rulesNormal.join("\n");
const rulesItalicList = rulesItalic.join("\n");

let file = "";

for (let i = 0; i < fontAmount; i++) {
  file += headers[i].join("\n");
  file += "\n\n";
  file += `[buildPlans.${fontNames[i]}.variants.design]\n`;
  file += rulesNormalList;
  file += "\n\n";
  file += `[buildPlans.${fontNames[i]}.variants.italic]\n`;
  file += rulesItalicList;
  file += "\n\n";
  file += footers[i].join("\n");
  file += "\n\n";
}

await Deno.writeTextFile("V6.toml", file);
