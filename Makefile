.PHONY: build clean copy all test
PLAN=dreams

all: copy

copy: build
	cp -r ./dream*/ttf ~/.local/share/fonts/dream

build: clean
	cd VERSIONS; ./generateVersion.py
	rm -rf iosevka/private-build-plans.toml
	cp VERSIONS/$(PLAN).toml iosevka/private-build-plans.toml
	cd iosevka; npm install; npm run build -- ttf::dreams && cp -r dist/dreams ../; npm run build -- ttf::dreamers && cp -r dist/dreamers ../; npm run build -- ttf::dreaming && cp -r dist/dreaming ../;

clean:
	rm -rf dreams dreamers dreaming
	rm -rf iosevka/dist
	rm -rf iosevka/.build

test:
	@echo -e '\033[1m abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
	@echo -e '\033[3m abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
	@echo -e '\033[3m\033[1m abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
	@echo -e ' abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
