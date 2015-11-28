# TODO:
# - split into subpackages
#

%define		module	egenix-mx-experimental
%define		mxdir	%{py_sitedir}/mx

Summary:	eGenix mx-Extensions - EXPERIMENTAL package
Summary(pl.UTF-8):	eGenix mx-Extensions - pakiet EKSPERYMENTALNY
Name:		python-%{module}
Version:	0.7.0
Release:	8
License:	Copyright (c) 2000-2001, eGenix.com Software GmbH, All Rights Reserved (partly only for non-comercial use)
Group:		Libraries/Python
Source0:	http://www.egenix.com/files/python/%{module}-%{version}.tar.gz
# Source0-md5:	1cfedef4f3582ed72857afb2c567207e
URL:		http://www.lemburg.com/files/python/eGenix-mx-Extensions.html
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python-egenix-mx-base
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The eGenix mx Extension Series are a collection of Python extensions
written in ANSI C and Python which provide a large spectrum of useful
additions to everyday Python programming.

This package includes experimental subpackages of the series. Please
understand that the software in these packages is still in alpha state
and does not meet the quality standards of production quality
software.

This software is brought to you by eGenix.com. The included
subpackages are either covered by the eGenix.com Public License or the
eGenix.com Commercial License and/or other licenses. Please check the
subpackage documentation for details or contact eGenix.com for more
license information.

%description -l pl.UTF-8
Kolekcja rozszerzeń dla języka Python napisana w ANSI C i Pythonie
dodająca szerokie spektrum użytecznych rozszerzeń dla programowania w
języku Python.

Ten pakiet zawiera eksperymentalne podpakiety z serii. Proszę mieć na
uwadze że oprogramowanie w tych pakietach jest ciągle w stanie alfa i
nie spełnia wymagań opgrogramowania w wersji produkcyjnej.

To oprogramowanie jest dostarczone przez eGenix.com. Załączone pakiety
są udostępniane przy użyciu eGenix.com Public License albo eGenix.com
Commercial License albo pod innymi licencjami. Należy sprawdzić
licencje dla poszczególnych podpakietów bądź skontaktować się z eGenix
bezpośrednio w tej sprawie.

%prep
%setup -q -n %{module}-%{version}

%build
env CFLAGS="%{rpmcflags}" %py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README mx/Number/Doc mx/Tidy/Doc mx/UID/Doc mx/URL/Doc

%dir %{mxdir}/Number
%dir %{mxdir}/Number/mxNumber
%attr(755,root,root) %{mxdir}/Number/mxNumber/*.so
%{mxdir}/Number/*.py[co]
%{mxdir}/Number/mxNumber/*.py[co]

%dir %{mxdir}/Tidy
%dir %{mxdir}/Tidy/mxTidy
%attr(755,root,root) %{mxdir}/Tidy/mxTidy/*.so
%{mxdir}/Tidy/*.py[co]
%{mxdir}/Tidy/mxTidy/*.py[co]

%dir %{mxdir}/UID
%dir %{mxdir}/UID/mxUID
%attr(755,root,root) %{mxdir}/UID/mxUID/*.so
%{mxdir}/UID/*.py[co]
%{mxdir}/UID/mxUID/*.py[co]

%dir %{mxdir}/URL
%dir %{mxdir}/URL/mxURL
%attr(755,root,root) %{mxdir}/URL/mxURL/*.so
%{mxdir}/URL/*.py[co]
%{mxdir}/URL/mxURL/*.py[co]
