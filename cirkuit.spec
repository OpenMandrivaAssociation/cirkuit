Name:		cirkuit
Summary:	KDE interface for LaTeX graphic tools
Version:	0.4.3
Release:	2
Group:		Sciences/Physics
License:	GPLv2
URL:		https://wwwu.uni-klu.ac.at/magostin/cirkuit.html
Source0:	http://wwwu.uni-klu.ac.at/magostin/src/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(poppler-qt4)
Requires:	ghostscript
Requires:	dpic
Requires:	m4
Requires:	pdf2svg
# Textlive is required for dvips
Requires:	texlive

%description
KDE interface for LaTeX graphic tools (such as TikZ, Gnuplot, Circuit Macros)
to produce publication-ready pictures.

%files -f %{name}.lang
%{_kde_bindir}/cirkuit
%{_kde_libdir}/kde4/cirkuit_circuitmacrosbackend.so
%{_kde_libdir}/kde4/cirkuit_nullbackend.so
%{_kde_datadir}/config.kcfg/circuitmacrosbackend.kcfg
%{_kde_datadir}/config.kcfg/cirkuit.kcfg
%{_kde_datadir}/config/cirkuit_example.knsrc
%{_kde_datadir}/config/cirkuit_template.knsrc
%{_kde_datadir}/mime/packages/cirkuit.xml
%{_kde_applicationsdir}/cirkuit.desktop
%{_kde_services}/cirkuit/circuitmacrosbackend.desktop
%{_kde_services}/cirkuit/nullbackend.desktop
%{_kde_servicetypes}/cirkuit_backend.desktop
%{_kde_appsdir}/cirkuit/
%{_kde_appsdir}/katepart/syntax/m4cm.xml
%{_kde_iconsdir}/hicolor/*/apps/cirkuit.png
%{_kde_iconsdir}/oxygen/scalable/mimetypes/application-x-cirkuit.svgz

#------------------------------------------------------------------------------

%package gnuplot-backend
Summary:	Gnuplot backend for %{name}
Group:		Sciences/Physics
Conflicts:	%{name} < 0.4.3
Requires:	%{name} = %{EVRD}

%description gnuplot-backend
KDE interface for LaTeX graphic tools (such as TikZ, Gnuplot, Circuit Macros)
to produce publication-ready pictures.

This package provides the gnuplot backend for %{name}.

%files gnuplot-backend
%{_kde_libdir}/kde4/cirkuit_gnuplotbackend.so
%{_kde_appsdir}/katepart/syntax/gnuplot.xml
%{_kde_datadir}/config.kcfg/gnuplotbackend.kcfg
%{_kde_services}/cirkuit/gnuplotbackend.desktop

#------------------------------------------------------------------------------

%package pstricks-backend
Summary:	Pstricks backend for %{name}
Group:		Sciences/Physics
Conflicts:	%{name} < 0.4.3
Requires:	%{name} = %{EVRD}

%description pstricks-backend
KDE interface for LaTeX graphic tools (such as TikZ, Gnuplot, Circuit Macros)
to produce publication-ready pictures.

This package provides the pstricks backend for %{name}.

%files pstricks-backend
%{_kde_libdir}/kde4/cirkuit_pstricksbackend.so
%{_kde_datadir}/config.kcfg/pstricksbackend.kcfg
%{_kde_services}/cirkuit/pstricksbackend.desktop

#------------------------------------------------------------------------------

%package tikz-backend
Summary:	Tikz backend for %{name}
Group:		Sciences/Physics
Conflicts:	%{name} < 0.4.3
Requires:	%{name} = %{EVRD}

%description tikz-backend
KDE interface for LaTeX graphic tools (such as TikZ, Gnuplot, Circuit Macros)
to produce publication-ready pictures.

This package provides the tikz backend for %{name}.

%files tikz-backend
%{_kde_libdir}/kde4/cirkuit_tikzbackend.so
%{_kde_datadir}/config.kcfg/tikzbackend.kcfg
%{_kde_services}/cirkuit/tikzbackend.desktop

#------------------------------------------------------------------------------

%define cirkuit_major 1
%define libcirkuit %mklibname cirkuit %{cirkuit_major}

%package -n %{libcirkuit}
Group:		System/Libraries
Summary:	Runtime library for %{name}
Conflicts:	%{name} < 0.4.3

%description -n %{libcirkuit}
KDE interface for LaTeX graphic tools (such as TikZ, Gnuplot, Circuit Macros)
to produce publication-ready pictures.

This package provides the runtime library for %{name}

%files -n %{libcirkuit}
%{_kde_libdir}/libcirkuitlibs.so.%{cirkuit_major}*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde_libdir}/libcirkuitlibs.so

%find_lang %{name}

