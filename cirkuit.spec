Summary:	Builds circuit images
Name:		cirkuit
Version: 	0.4
Release: 	%mkrel 1
Source0: 	http://wwwu.uni-klu.ac.at/magostin/src/%name-%version.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://wwwu.uni-klu.ac.at/magostin/cirkuit.html
BuildRequires: 	kdelibs4-devel
BuildRequires:	libpoppler-qt4-devel
Requires:	tetex
Requires:	m4
Requires:	ghostscript
Requires:	pdf2svg

%description 
Cirkuit is a KDE4 GUI for the Circuit macros by Dwight Aplevich, which
is a set of macros for drawing high-quality line diagrams to include
in TeX, LaTeX, or similar documents. Cirkuit builds a live preview of
the source code and can export the resulting images in EPS, PDF, PNG
or PSTricks format.

%files
%defattr(-,root,root)
%doc README Changelog
%_kde_bindir/*
%_kde_appsdir/cirkuit
%_kde_appsdir/katepart/syntax/*.xml
%{_kde_libdir}/kde4/*.so
%{_kde_libdir}/*.so.*
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_datadir}/config/*.knsrc
%{_kde_services}/cirkuit
%{_kde_servicetypes}/*.desktop
%_kde_applicationsdir/*.desktop
%_kde_datadir/mime/packages/*.xml
%_kde_iconsdir/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

rm -f %{buildroot}%{_libdir}/*.so

%clean
rm -rf %{buildroot}


%changelog
* Thu Aug 11 2011 Funda Wang <fwang@mandriva.org> 0.4-1mdv2012.0
+ Revision: 693919
- new version 0.4

* Wed May 18 2011 Funda Wang <fwang@mandriva.org> 0.3.2-1
+ Revision: 676025
- update to new version 0.3.2

* Mon Dec 20 2010 Funda Wang <fwang@mandriva.org> 0.3.1.1-1mdv2011.0
+ Revision: 623351
- update to new version 0.3.1.1

* Thu Dec 16 2010 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 622369
- update to new version 0.3.1
- bump rel
- br pdf2svg
- new version 0.3

  + Giuseppe Ghibò <ghibo@mandriva.com>
    - Use default tetex as Requires instead of texlive as it's the main TeX package.

* Thu Dec 17 2009 Funda Wang <fwang@mandriva.org> 0.2.2-1mdv2010.1
+ Revision: 479738
- new version 0.2.2

* Thu Aug 06 2009 Funda Wang <fwang@mandriva.org> 0.2.1-1mdv2010.0
+ Revision: 410439
- new version 0.2.1

* Fri Jul 31 2009 Funda Wang <fwang@mandriva.org> 0.2-1mdv2010.0
+ Revision: 405070
- fix file list
- new version 0.2

* Sat Jul 11 2009 Funda Wang <fwang@mandriva.org> 0.1.2-1mdv2010.0
+ Revision: 394432
- new version 0.1.2

* Wed Jun 24 2009 Funda Wang <fwang@mandriva.org> 0.1.1-1mdv2010.0
+ Revision: 388836
- New version 0.1.1

* Thu Jun 18 2009 Funda Wang <fwang@mandriva.org> 0.1-1mdv2010.0
+ Revision: 386923
- add requires and docs
- import cirkuit


