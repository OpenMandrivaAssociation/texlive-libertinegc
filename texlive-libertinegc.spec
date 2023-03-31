Name:		texlive-libertinegc
Version:	44616
Release:	2
Summary:	Libertine add-on to support Greek and Cyrillic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/libertinegc
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinegc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinegc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides LaTeX support files to access the Greek
and Cyrillic glyphs in LinuxLibertine. It functions as an
add-on to the libertine package, using filenames and macro
names that are compatible with that package. Supported
encodings: LGR, T2A, T2B, T2C, OT2.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/libertinegc
%{_texmfdistdir}/fonts/tfm/public/libertinegc
%{_texmfdistdir}/fonts/map/dvips/libertinegc
%{_texmfdistdir}/fonts/enc/dvips/libertinegc
%doc %{_texmfdistdir}/doc/fonts/libertinegc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
