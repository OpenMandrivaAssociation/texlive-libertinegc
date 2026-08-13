%global tl_name libertinegc
%global tl_revision 44616
%global tl_version 1.01

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Libertine add-on to support Greek and Cyrillic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/libertinegc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinegc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/libertinegc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package provides LaTeX support files to access the Greek and
Cyrillic glyphs in LinuxLibertine. It functions as an add-on to the
libertine package, using filenames and macro names that are compatible
with that package. Supported encodings: LGR, T2A, T2B, T2C, OT2.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from libertinegc:
Map libertinegc.map
TL_DROPIN_EOF
