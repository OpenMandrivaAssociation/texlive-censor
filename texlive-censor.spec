# revision 20937
# category Package
# catalog-ctan /macros/latex/contrib/censor
# catalog-date 2011-01-04 21:24:54 +0100
# catalog-license lppl1.3
# catalog-version 1.00
Name:		texlive-censor
Version:	1.00
Release:	3
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
%doc %{_texmfdistdir}/doc/latex/censor/manifest.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.00-2
+ Revision: 750050
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.00-1
+ Revision: 718027
- texlive-censor
- texlive-censor
- texlive-censor
- texlive-censor
- texlive-censor

