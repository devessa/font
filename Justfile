alias ba := build_all
alias b := build
alias c := clean
alias cp := copy

# shows help
default:
   @just --list --list-heading "" --list-prefix "  ->  " --justfile {{justfile()}}

# gen -> build_all -> copy
d:
   @just gen && just build_all && just copy

# generates toml files used for building
gen:
   @cd generator; ./gen

# builds "type", "term", and "code"
build_all: (build "type") (build "term") (build "code")

# removes iosevka stuff
prebuild:
   @rm -rf iosevka/dist
   @rm -rf iosevka/build
   @rm -rf iosevka/private-build-plans.toml

# rm -rf {font}
clean font:
   @rm -rf {{font}}

# copies a font to ~/.local/share/{font}
copy font:
   @cp -r ./{{font}}*/ttf ~/.local/share/fonts/{{font}}

# runs through the entire process to build a font.
build font: prebuild (clean font)
   @cp /tmp/{{font}}.toml iosevka/private-build-plans.toml
   @cd iosevka; npm run build -- ttf::{{font}} && cp -r dist/{{font}} ../