Summary:	Builds circuit images
Name:		cirkuit
Version: 	0.3.1
Release: 	%mkrel 1
Source0: 	http://wwwu.uni-klu.ac.at/magostin/src/%name-%version.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://wwwu.uni-klu.ac.at/magostin/cirkuit.html
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%_kde_datadir/config.kcfg/cirkuit.kcfg
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

%clean
rm -rf %{buildroot}
