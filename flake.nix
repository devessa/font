{
  description = "nixos flake for code, type, and term";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: {
    packages.x86_64-linux.fontdreams = with nixpkgs.legacyPackages.x86_64-linux; stdenv.mkDerivation {
      name = "fontdreams";
      src = ./.; # path to your source file
      buildInputs = [ ttfautohint npm nodejs just python3 ];

      buildPhase = ''
        git submodule update --init --depth 1
        just gen && just build_all
      '';

      installPhase = ''
        install -Dm644 ./type*/ttf/*.ttf -t $out/share/fonts
        install -Dm644 ./code*/ttf/*.tff -t $out/share/fonts
        install -Dm644 ./term*/ttf/*.ttf -t $out/share/fonts
      '';
    };

    packages.x86_64-linux.default = self.packages.x86_64-linux.myProgram;
  };
}
