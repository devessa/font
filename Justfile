alias b := build_all
alias c := clean
alias cp := copy

default:
   just gen && just build_all && just copy

gen:
   cd generator; ./gen

build_all: build_type build_code build_term

clean:
   rm -rf type code term
   rm -rf iosevka/dist
   rm -rf iosevka/build
   rm -rf iosevka/private-build-plans.toml

copy:
   cp -r ./type*/ttf ~/.local/share/fonts/type
   cp -r ./code*/ttf ~/.local/share/fonts/code
   cp -r ./term*/ttf ~/.local/share/fonts/term

build_type: clean
   cp /tmp/type.toml iosevka/private-build-plans.toml
   cd iosevka; npm run build -- ttf::type && cp -r dist/type ../

build_code: clean
   cp /tmp/code.toml iosevka/private-build-plans.toml
   cd iosevka; npm run build -- ttf::code && cp -r dist/code ../

build_term: clean
   cp /tmp/term.toml iosevka/private-build-plans.toml
   cd iosevka; npm run build -- ttf::term && cp -r dist/term ../