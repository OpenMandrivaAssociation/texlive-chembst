Name:		texlive-chembst
Version:	0.2.5
Release:	1
Summary:	A collection of BibTeX files for chemistry journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/chembst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chembst.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chembst.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chembst.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package offers a collection of advanced BibTeX style files
suitable for publications in chemistry journals. Currently,
style files for journals published by the American Chemical
Society, Wiley-VCH and The Royal Society of Chemistry are
available. The style files support advanced features such as
automatic formatting of errata or creating an appropriate entry
for publications in Angewandte Chemie where both English and
German should be cited simultaneously.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc source %{buildroot}%{_texmfdistdir}
