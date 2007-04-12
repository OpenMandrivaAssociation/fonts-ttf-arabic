Summary:	Free Arabic TrueType fonts
Name:		fonts-ttf-arabic
Version:	1.1
Release:	%mkrel 5
License:	GPL
Group:		System/Fonts/True type

Source0:	http://www.linux.org.sa/download/KacstArabicFonts-%{version}.tar.bz2
Source1:	nastaliq_unicode.ttf.bz2

BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools
Requires(post):		chkfontpath
Requires(postun):	chkfontpath
Requires(post): fontconfig
Requires(postun): fontconfig

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

%post
[ -x %_sbindir/chkfontpath ] && %_sbindir/chkfontpath -q -a %_datadir/fonts/TTF/arabic
touch %{_datadir}/fonts/TTF
[ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %_sbindir/chkfontpath ] && \
   %_sbindir/chkfontpath -q -r %_datadir/fonts/TTF/arabic
   [ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc *txt
#
%dir %_datadir/fonts/TTF/
%dir %_datadir/fonts/TTF/arabic/
%_datadir/fonts/TTF/arabic/*



