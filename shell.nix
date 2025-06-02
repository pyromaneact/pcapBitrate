
{pkgs ? import <nixpkgs> {}}: 
pkgs.mkShell{
  packages  = [
    pkgs.wireshark
    pkgs.python313
    (pkgs.python313.withPackages(
      pypkgs: with pypkgs;[
        dpkt
      ]
    ))
  ];
}
