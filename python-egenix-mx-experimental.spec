
#
# todo:
# - split into subpackages
#

%include	/usr/lib/rpm/macros.python

%define		module egenix-mx-experimental
%define		mxdir %{py_sitedir}/mx

Summary:	eGenix mx-Extensions - EXPERIMENTAL package
Summary(pl):	eGenix mx-Extensions - pakiet EKSPERYMENTALNY
Name:		python-module
Version:	0.7.0
Release:	0.9
Source0:	http://www.egenix.com/files/python/%{module}-%{version}.tar.gz
Copyright:	Copyright (c) 2000-2001, eGenix.com Software GmbH, All Rights Reserved (partly only for non-comercial use)
Group:		Libraries/Python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Vendor:		eGenix.com Software GmbH, Langenfeld, Germany <info@egenix.com>
Requires:	python-egenix-mx-base
Url:		http://www.lemburg.com/files/python/eGenix-mx-Extensions.html

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

%description(pl)
Kolekcja rozszerze dla j�zyka Python napisana w ANSI C i Pythonie
dodaj�ca szerokie spektrum u�ytecznych rozszerze� dla programowania w
j�zyku Python.

Ten pakiet zawiera eksperymentalne podpakiety z serii. Prosze mie� na
uwadze �e oprogramowanie w tych pakietach jest ci�gle w stanie alfa i
nie spe�nia wymaga� opgrogramowania w wersji produkcyjnej.

To oprogramowanie jest dostarczone przez eGenix.com. Za��czone pakiety
s� udost�pniane przy u�yciu eGenix.com Public License albo eGenix.com
Commercial License albo pod innymi licencjami. Prosze sprawdzi�
licencje dla poszczeg�lnych podpakiet�w b�d� skontaktowa� si� z eGenix
bezpo�rednio w tej sprawie.

%prep
%setup -q -n %{module}-%{version}

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

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
