.PHONY: build clean copy all test
PLAN=V7

all: copy

copy: build
	cp -r ./bunni*/ttf ~/.local/share/fonts/bunnifonts

build: clean
	cd VERSIONS; ./generateVersion.ts
	rm -rf iosevka/private-build-plans.toml
	cp VERSIONS/$(PLAN).toml iosevka/private-build-plans.toml
	cd iosevka; npm install; npm run build -- ttf::bunni && cp -r dist/bunni ../; npm run build -- ttf::bunnit && cp -r dist/bunnit ../; npm run build -- ttf::bunniq && cp -r dist/bunniq ../;

clean:
	rm -rf bunni bunniq bunnit
	rm -rf iosevka/dist
	rm -rf iosevka/.build

test:
	@echo -e '\033[1m abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
	@echo -e '\033[3m abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
	@echo -e '\033[3m\033[1m abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
	@echo -e ' abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
