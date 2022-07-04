# simple.nix
with (import <nixpkgs> {});
mkShell {
  buildInputs = [
    pandoc haskellPackages.pandoc-crossref
    texlive.combined.scheme-medium
  ];
}
