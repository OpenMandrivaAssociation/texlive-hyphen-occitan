%global tl_name hyphen-occitan
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Occitan hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-occitan
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-occitan.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Occitan in T1/EC and UTF-8 encodings. They are
supposed to be valid for all the Occitan variants spoken and written in
the wide area called 'Occitanie' by the French. It ranges from the Val
d'Aran within Catalunya, to the South Western Italian Alps encompassing
the southern half of the French pentagon.

