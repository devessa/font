{
  description = "custom build of Iosevka I personally use.";
  outputs = inputs:
    inputs.flake-parts.lib.mkFlake {inherit inputs;} {
      imports = [
        inputs.devshell.flakeModule
      ];
      systems = ["x86_64-linux"];
      perSystem = {pkgs, ...}: {
        devshells.default = {
          packages = [pkgs.ttfautohint pkgs.nodejs pkgs.just pkgs.git pkgs.python3];
          commands = [
            {
              help = "initialize submodules";
              name = "upd";
              command = "git submodule update --init --depth 1";
            }
            {
              help = "update submodules to latest revision";
              name = "revupd";
              command = "git submodule update --init --remote";
            }
            {
              help = "build fonts";
              name = "build";
              command = "just gen && just build_all";
            }
            {
              help = "build and install all fonts";
              name = "instfonts";
              command = "just";
            }
          ];
          motd = ''
            {63}welcome to devshell{reset}
            $(type -p menu &>/dev/null && menu)'';
        };
      };
    };
  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    devshell.url = "github:numtide/devshell";
  };
}
