.PHONY build clean copy all

PLAN=v5

all: copy

copy: build
	cp -r ./bunni*/ttf ~/.local/share/fonts/bunnifonts

build: clean
	cd iosevka
	rm -rf private-build-plans.toml
	cp ../$(PLAN).toml private-build-plans.toml
	npm install
	npm run build -- ttf::bunni && cp -r dist/bunni ../
	npm run build -- ttf::bunnit && cp -r dist/bunnit ../
	npm run build -- ttf::bunniq && cp -r dist/bunniq ../

clean:
	rm -rf bunni bunniq bunnit
	rm -rf iosevka/dist
	rm -rf iosevka/.build
   rm -rf "$HOME"/.local/share/fonts/bunnifonts/*