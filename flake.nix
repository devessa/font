{
  description = "nixos flake for code, type, and term";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: {
    packages.x86_64-linux.fontdreams = with nixpkgs.legacyPackages.x86_64-linux; stdenv.mkDerivation {
      name = "fontdreams";
      src = self; # path to your source file
      buildInputs = [ ttfautohint git nodejs just python3 gnutar ];

      configurePhase = ''
        tar -xzvf iosevka.tar.gz
      '';

      buildPhase = ''
        just gen && just build_all;
      '';

      installPhase = ''
        install -Dm644 ./type*/ttf/*.ttf -t $out/share/fonts
        install -Dm644 ./code*/ttf/*.tff -t $out/share/fonts
        install -Dm644 ./term*/ttf/*.ttf -t $out/share/fonts
      '';
    };

    packages.x86_64-linux.default = self.packages.x86_64-linux.fontdreams;
  };
}
