alias b := build_all
alias bty := build_type
alias bte := build_term
alias bc := build_code
alias c := clean_all
alias cp := copy

default:
   just gen && just build_all && just copy

gen:
   cd generator; ./gen

build_all: build_type build_code build_term

prebuild:
   rm -rf iosevka/dist
   rm -rf iosevka/build
   rm -rf iosevka/private-build-plans.toml

clean_type:
  rm -rf type
clean_term:
  rm -rf term
clean_code:
  rm -rf code

clean_all: clean_type clean_term clean_code

copy:
   cp -r ./type*/ttf ~/.local/share/fonts/type || :
   cp -r ./code*/ttf ~/.local/share/fonts/code || :
   cp -r ./term*/ttf ~/.local/share/fonts/term || :
   fc-cache -r -f -v

build_type: prebuild clean_type
   cp /tmp/type.toml iosevka/private-build-plans.toml
   cd iosevka; npm run build -- ttf::type && cp -r dist/type ../

build_code: prebuild clean_code
   cp /tmp/code.toml iosevka/private-build-plans.toml
   cd iosevka; npm run build -- ttf::code && cp -r dist/code ../

build_term: prebuild clean_term
   cp /tmp/term.toml iosevka/private-build-plans.toml
   cd iosevka; npm run build -- ttf::term && cp -r dist/term ../
