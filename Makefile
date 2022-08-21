.PHONY: build clean copy all
PLAN=V5

all: copy

copy: build
	cp -r ./bunni*/ttf ~/.local/share/fonts/bunnifonts

build: clean
	rm -rf iosevka/private-build-plans.toml
	cp VERSIONS/$(PLAN).toml iosevka/private-build-plans.toml
	cd iosevka; npm install; npm run build -- ttf::bunni && cp -r dist/bunni ../; npm run build -- ttf::bunnit && cp -r dist/bunnit ../; npm run build -- ttf::bunniq && cp -r dist/bunniq ../;

clean:
	rm -rf bunni bunniq bunnit
	rm -rf iosevka/dist
	rm -rf iosevka/.build