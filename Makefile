.PHONY: build clean copy all test
PLAN=dreams
PLAN2=type

all: copy

copy: build_dreams
	cp -r ./dream*/ttf ~/.local/share/fonts/dream
	cp -r ./type*/ttf ~/.local/share/fonts/type

build_dreams: build_type
	cd VERSIONS; ./$(PLAN).py
	rm -rf iosevka/private-build-plans.toml
	cp VERSIONS/$(PLAN).toml iosevka/private-build-plans.toml
	cd iosevka; npm install; npm run build -- ttf::dreams && cp -r dist/dreams ../; npm run build -- ttf::dreamers && cp -r dist/dreamers ../; npm run build -- ttf::dreamily && cp -r dist/dreamily ../;

build_type: clean
	cd VERSIONS; ./$(PLAN2).py
	rm -rf iosevka/private-build-plans.toml
	cp VERSIONS/$(PLAN2).toml iosevka/private-build-plans.toml
	cd iosevka; npm install; npm run build -- ttf::type && cp -r dist/type ../

clean:
	rm -rf dreams dreamers dreamily
	rm -rf type
	rm -rf iosevka/dist
	rm -rf iosevka/.build

test:
	@echo -e '\033[1m abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
	@echo -e '\033[3m abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
	@echo -e '\033[3m\033[1m abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
	@echo -e ' abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890-=!@#\ %^&*()[]{}\|:;'""'.>/?,< \033[0m'
	@echo -e ' The quick brown fox jumps over the lazy dog.'
	@echo -e '\033[3m The quick brown fox jumps over the lazy dog.\033[0m'
	@echo -e ' THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
	@echo -e '\033[3m THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.\033[0m'
