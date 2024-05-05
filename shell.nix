{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
   buildInputs = [
      pkgs.ttfautohint
      pkgs.nodejs
   ];
}
