# revision 31332
# category Package
# catalog-ctan /macros/latex/contrib/censor
# catalog-date 2013-07-31 09:50:54 +0200
# catalog-license lppl1.3
# catalog-version 3.21
Name:		texlive-censor
Version:	3.21
Release:	5
Summary:	Facilities for controlling restricted text in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/censor
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/censor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/censor.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows a convenient redaction/censor capability to
be employed, for those who need to protect restricted
information, etc. The package can "redact" anything that can be
enclosed by a LaTeX box.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/censor/censor.sty
%doc %{_texmfdistdir}/doc/latex/censor/README
%doc %{_texmfdistdir}/doc/latex/censor/censor.pdf
%doc %{_texmfdistdir}/doc/latex/censor/censor.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
