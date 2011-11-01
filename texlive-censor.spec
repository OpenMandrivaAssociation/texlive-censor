Name:		texlive-censor
Version:	1.00
Release:	1
Summary:	Facilities for controlling restricted text in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/censor
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/censor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/censor.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package allows a convenient redaction/censor capability to
be employed, for those who need to protect restricted
information, as well as for those who are forced to work in a
more inefficient environment when dealing with restricted
information.

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
%{_texmfdistdir}/tex/latex/censor/censor.sty
%doc %{_texmfdistdir}/doc/latex/censor/README
%doc %{_texmfdistdir}/doc/latex/censor/censor.pdf
%doc %{_texmfdistdir}/doc/latex/censor/censor.tex
%doc %{_texmfdistdir}/doc/latex/censor/manifest.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
