let
  pkgs = import (fetchTarball ("channel:nixpkgs-unstable")) { };
in
pkgs.mkShell {
  buildInputs = [ pkgs.ttfautohint pkgs.nodejs pkgs.just pkgs.git pkgs.python3 ];
}
