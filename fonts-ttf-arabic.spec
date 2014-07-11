Summary:	Arabic TrueType fonts
Name:		fonts-ttf-arabic
Version:	1.1
Release:	24
License:	GPLv2
Group:		System/Fonts/True type
Source0:	http://www.linux.org.sa/download/KacstArabicFonts-%{version}.tar.bz2
Source1:	nastaliq_unicode.ttf.bz2
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	mkfontscale

%description
This Package provides Free Arabic TrueType fonts.

%prep

%setup -q -c

%build
bzcat %{SOURCE1} > nastaliq_unicode.ttf

%install
mkdir -p %buildroot/%{_datadir}/fonts/TTF/arabic/
cp *.ttf %buildroot/%{_datadir}/fonts/TTF/arabic/

(
cd %buildroot/%{_datadir}/fonts/TTF/arabic/
mkfontscale
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/arabic \
    %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-arabic:pri=50

%post
touch %{_datadir}/fonts/TTF

%files
%doc *txt
%dir %{_datadir}/fonts/TTF/arabic/
%{_datadir}/fonts/TTF/arabic/*
%{_sysconfdir}/X11/fontpath.d/ttf-arabic:pri=50

