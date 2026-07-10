%global tl_name chembst
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.5
Release:	%{tl_revision}.1
Summary:	A collection of BibTeX files for chemistry journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/chembst
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chembst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chembst.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chembst.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers a collection of advanced BibTeX style files suitable
for publications in chemistry journals. Currently, style files for
journals published by the American Chemical Society, Wiley-VCH and The
Royal Society of Chemistry are available. The style files support
advanced features such as automatic formatting of errata or creating an
appropriate entry for publications in Angewandte Chemie where both
English and German should be cited simultaneously.

