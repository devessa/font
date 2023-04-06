#!/usr/bin/env -S deno run --allow-write

type TOML = string[][];

const fontAmount = 3;
const fontNames = ['bunni', 'bunnit', 'bunniq'];

const headers: TOML = [
  [
    '[buildPlans.bunni]',
    'family = "bunni"',
    'spacing = "normal"',
    'serifs = "sans"',
    'no-cv-ss = true',
    'export-glyph-names = true',
  ],
  [
    '[buildPlans.bunnit]',
    'family = "bunnit"',
    'spacing = "term"',
    'serifs = "sans"',
    'no-cv-ss = true',
    'export-glyph-names = true',
  ],
  [
    '[buildPlans.bunniq]',
    'family = "bunniq"',
    'spacing = "quasi-proportional-extension-only"',
    'serifs = "sans"',
    'no-cv-ss = true',
    'export-glyph-names = true',
  ],
];

const rulesNormal: TOML = [
  ['capital-d = "more-rounded-serifless"'],
  ['capital-w = "straight"'],
  ['capital-z = "curly-serifless"'],
  ['capital-x = "straight-serifless"'],
  ['capital-q = "horizontal-tailed"'],
  ['capital-i = "short-serifed"'],
  ['capital-f = "serifless"'],
  ['capital-c = "serifless"'],
  ['capital-j = "flat-hook-serifed"'],
  ['capital-b = "standard-serifless"'],
  //  ['capital-g = "toothless-rounded-serifless-hooked"'],
  ['capital-g = "toothless-corner-serifless-hookless"'],
  ['capital-k = "straight-serifless"'],
  ['capital-y = "straight-serifless"'],
  ['capital-u = "toothless-corner"'],
  ['capital-n = "asymmetric"'],
  ['capital-r = "curly"'],
  ['a = "single-storey-earless-corner-serifless"'],
  ['b = "toothed"'],
  ['c = "serifless"'],
  ['d = "toothed-serifless"'],
  ['f = "flat-hook-crossbar-at-x-height"'],
  //  ['g = "single-storey-earless-corner-flat-hook"'],
  ['g = "double-storey"'],
  //  ['g = "single-storey-flat-hook-serifless"'],
  ['i = "hooky"'],
  ['j = "flat-hook-serifed"'],
  ['k = "curly-serifless"'],
  ['l = "tailed-serifed"'],
  ['m = "normal"'],
  ['n = "straight"'],
  ['q = "earless-corner"'],
  ['p = "eared"'],
  ['r = "corner-hooked"'],
  // ['r = "serifless"'],
  ['s = "serifless"'],
  ['t = "flat-hook-short-neck2"'],
  ['u = "toothed"'],
  ['v = "straight"'],
  ['w = "straight"'],
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
  ['four = "semi-open-non-crossing"'],
  ['five = "vertical-upper-left-bar"'],
  ['six = "straight-bar"'],
  ['seven = "curly-serifed"'],
  ['eight = "crossing"'],
  ['nine = "straight-bar"'],
  ['zero = "slashed-split"'],
  ['asterisk = "penta-low"'],
  ['underscore = "low"'],
  ['pilcrow = "low"'],
  ['caret = "low"'],
  ['paren = "large-contour"'],
  ['brace = "curly-flat-boundary"'],
  ['number-sign = "slanted-open"'],
  ['ampersand = "closed"'],
  ['at = "short"'],
  ['dollar = "interrupted"'],
  ['cent = "bar-interrupted"'],
  ['percent = "rings-continuous-slash"'],
  ['bar = "natural-slope"'],
  ['lig-ltgteq = "slanted"'],
  ['lig-neq = "more-slanted"'],
  ['question = "smooth"'],
  ['punctuation-dot = "square"'],
  ['diacritic-dot = "square"'],
  ['lig-equal-chain = "without-notch"'],
  ['lig-hypen-chain = "without-notch"'],
];

const rulesItalic: TOML = [
  ['a = "single-storey-earless-corner-serifless"'],
  ['e = "rounded"'],
  ['f = "serifless-crossbar-at-x-height"'],
  ['g = "earless-corner"'],
  ['i = "tailed-serifed"'],
  ['j = "serifed"'],
  ['k = "cursive-serifless"'],
  ['l = "tailed-serifed"'],
  ['m = "normal"'],
  ['t = "standard"'],
  ['u = "toothed"'],
  ['w = "straight"'],
  ['y = "cursive"'],
  ['z = "curly-serifless"'],
];

const footers: TOML = [
  [
    '[buildPlans.bunni.widths.normal]',
    'shape = 600',
    'menu = 5',
    'css = "normal"',
    '\n',
    '[buildPlans.bunni.metric-override]',
    'powerlineScaleX = 1',
    'powerlineScaleY = 1',
    '\n',
    '[buildPlans.bunni.ligations]',
    'inherits = "dlig"',
  ],
  [
    '[buildPlans.bunnit.widths.normal]',
    'shape = 600',
    'menu = 5',
    'css = "normal"',
    '\n',
    '[buildPlans.bunnit.metric-override]',
    'powerlineScaleX = 1',
    'powerlineScaleY = 1',
    '\n',
    '[buildPlans.bunnit.ligations]',
    'inherits = "dlig"',
  ],
  [
    '[buildPlans.bunniq.widths.normal]',
    'shape = 600',
    'menu = 5',
    'css = "normal"',
    '\n',
    '[buildPlans.bunniq.metric-override]',
    'powerlineScaleX = 1',
    'powerlineScaleY = 1',
    '\n',
    '[buildPlans.bunniq.ligations]',
    'inherits = "dlig"',
  ],
];

const rulesNormalList = rulesNormal.join('\n');
const rulesItalicList = rulesItalic.join('\n');

let file = '';

for (let i = 0; i < fontAmount; i++) {
  file += headers[i].join('\n');
  file += '\n\n';
  file += `[buildPlans.${fontNames[i]}.variants.design]\n`;
  file += rulesNormalList;
  file += '\n\n';
  file += `[buildPlans.${fontNames[i]}.variants.italic]\n`;
  file += rulesItalicList;
  file += '\n\n';
  file += footers[i].join('\n');
  file += '\n\n';
}

await Deno.writeTextFile('V7.toml', file);
