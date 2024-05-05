# about

Personal font I use, created by using Iosevka's custom build feature.

Current fonts:
- `type`: a quasiproportional font specifically for any variation of non-programming reading.
- `code`: a monospace font great for reading code.
- `term`: edit of `code` for terminal.

# development

Use [my own custom git conventions](https://github.com/kyoline/git-conventions) when creating branches or committing.

Create issues in order to log tasks, such as an issue dedicated to revamping the font.

Only create pull requests that merge into main when you want a release to be added to the releases page.

Otherwise, commit to `dev`.

# building

```shell
gh repo clone kyoline/font
# install ttfautohint & update submodules, or run:
./setup

just gen && just build_all && just copy
```
