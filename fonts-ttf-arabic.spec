Summary:	Arabic TrueType fonts
Name:		fonts-ttf-arabic
Version:	1.1
Release:	%mkrel 12
License:	GPL
Group:		System/Fonts/True type

Source0:	http://www.linux.org.sa/download/KacstArabicFonts-%{version}.tar.bz2
Source1:	nastaliq_unicode.ttf.bz2

BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools

%description
This Package provides Free Arabic TrueType fonts.

%prep

%setup -q -c

%build
bzcat %{SOURCE1} > nastaliq_unicode.ttf

%install
rm -fr %buildroot

mkdir -p %buildroot/%_datadir/fonts/TTF/arabic/
cp *.ttf %buildroot/%_datadir/fonts/TTF/arabic/

(
cd %buildroot/%_datadir/fonts/TTF/arabic/
%_sbindir/ttmkfdir -u > fonts.scale
cp fonts.scale fonts.dir
%if %mdkversion < 20070
%_bindir/fc-cache . || touch fonts.cache-1
%endif
)

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/arabic \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-arabic:pri=50

%post
touch %{_datadir}/fonts/TTF

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc *txt
%dir %_datadir/fonts/TTF/arabic/
%_datadir/fonts/TTF/arabic/*
%_sysconfdir/X11/fontpath.d/ttf-arabic:pri=50

