# revision 27638
# category Package
# catalog-ctan /macros/latex/contrib/censor
# catalog-date 2012-09-10 12:31:33 +0200
# catalog-license lppl1.3
# catalog-version 2.10
Name:		texlive-censor
Version:	2.10
Release:	1
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
information, as well as for those who are forced to work in a
more inefficient environment when dealing with restricted
information.

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
