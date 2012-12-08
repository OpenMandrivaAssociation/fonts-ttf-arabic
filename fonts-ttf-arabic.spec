Summary:	Arabic TrueType fonts
Name:		fonts-ttf-arabic
Version:	1.1
Release:	%mkrel 18
License:	GPL
Group:		System/Fonts/True type

Source0:	http://www.linux.org.sa/download/KacstArabicFonts-%{version}.tar.bz2
Source1:	nastaliq_unicode.ttf.bz2

BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	mkfontscale

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
mkfontscale
cp fonts.scale fonts.dir
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



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.1-15mdv2011.0
+ Revision: 675405
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.1-14
+ Revision: 675169
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-13
+ Revision: 664318
- mass rebuild

* Fri Dec 03 2010 Funda Wang <fwang@mandriva.org> 1.1-12mdv2011.0
+ Revision: 605825
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1-11mdv2010.1
+ Revision: 494116
- fc-cache is now called by an rpm filetrigger

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.1-10mdv2009.1
+ Revision: 351034
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.1-9mdv2009.0
+ Revision: 220854
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.1-8mdv2008.1
+ Revision: 170833
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.1-7mdv2008.1
+ Revision: 149731
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1-6mdv2008.0
+ Revision: 48734
- fontpath.d conversion (#31756)
- minor cleanups


* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 23:09:52 (52880)
- Normalize fonts with new paths

* Fri Aug 04 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-04 20:59:59 (52794)
- import fonts-ttf-arabic-1.1-4mdk

* Fri Feb 03 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1-4mdk
- Don't package fonts.cache-2 file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)
- Remove dependency on freetype, this is old stuff

* Wed Aug 06 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 1.1-3mdk
- added Urdu Nastaliq GPL font (covering Urdu and Farsi)

