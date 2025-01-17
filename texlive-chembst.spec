Name:		texlive-chembst
Version:	15878
Release:	2
Summary:	A collection of BibTeX files for chemistry journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/chembst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chembst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chembst.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chembst.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a collection of advanced BibTeX style files
suitable for publications in chemistry journals. Currently,
style files for journals published by the American Chemical
Society, Wiley-VCH and The Royal Society of Chemistry are
available. The style files support advanced features such as
automatic formatting of errata or creating an appropriate entry
for publications in Angewandte Chemie where both English and
German should be cited simultaneously.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/chembst/ChemCommun.bst
%{_texmfdistdir}/bibtex/bst/chembst/ChemEurJ.bst
%{_texmfdistdir}/bibtex/bst/chembst/InorgChem.bst
%{_texmfdistdir}/bibtex/bst/chembst/JAmChemSoc.bst
%{_texmfdistdir}/bibtex/bst/chembst/JAmChemSoc_all.bst
%{_texmfdistdir}/bibtex/bst/chembst/cv.bst
%doc %{_texmfdistdir}/doc/latex/chembst/README
%doc %{_texmfdistdir}/doc/latex/chembst/chembst.pdf
#- source
%doc %{_texmfdistdir}/source/latex/chembst/chembst.dtx
%doc %{_texmfdistdir}/source/latex/chembst/chembst.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc source %{buildroot}%{_texmfdistdir}
