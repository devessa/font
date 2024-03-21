alias b := build_all
alias c := clean
alias cp := copy

default:
   just pull && just gen && just build_all && just copy

pull:
   git submodule update --init --depth 1
   cd iosevka; npm install

gen:
   cd generator; bash gen

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
   fc-cache -r -f -v

build_type: clean
   cp /tmp/type.toml iosevka/private-build-plans.toml
   cd iosevka; npx verda -f ./verdafile.mjs ttf::type && cp -r dist/type ../

build_code: clean
   cp /tmp/code.toml iosevka/private-build-plans.toml
   cd iosevka; npx verda -f ./verdafile.mjs ttf::code && cp -r dist/code ../

build_term: clean
   cp /tmp/term.toml iosevka/private-build-plans.toml
   cd iosevka; npx verda -f ./verdafile.mjs ttf::term && cp -r dist/term ../
