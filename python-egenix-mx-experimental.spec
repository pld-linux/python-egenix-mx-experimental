# TODO:
# - split into subpackages
#

%define		module	egenix-mx-experimental
%define		mxdir	%{py_sitedir}/mx

Summary:	eGenix mx-Extensions - EXPERIMENTAL package
Summary(pl):	eGenix mx-Extensions - pakiet EKSPERYMENTALNY
Name:		python-%{module}
Version:	0.7.0
Release:	2
License:	Copyright (c) 2000-2001, eGenix.com Software GmbH, All Rights Reserved (partly only for non-comercial use)
Vendor:		eGenix.com Software GmbH, Langenfeld, Germany <info@egenix.com>
Group:		Libraries/Python
Source0:	http://www.egenix.com/files/python/%{module}-%{version}.tar.gz
# Source0-md5:	1cfedef4f3582ed72857afb2c567207e
URL:		http://www.lemburg.com/files/python/eGenix-mx-Extensions.html
Requires:	python-egenix-mx-base
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

%description -l pl
Kolekcja rozszerzeñ dla jêzyka Python napisana w ANSI C i Pythonie
dodaj±ca szerokie spektrum u¿ytecznych rozszerzeñ dla programowania w
jêzyku Python.

Ten pakiet zawiera eksperymentalne podpakiety z serii. Prosze mieæ na
uwadze ¿e oprogramowanie w tych pakietach jest ci±gle w stanie alfa i
nie spe³nia wymagañ opgrogramowania w wersji produkcyjnej.

To oprogramowanie jest dostarczone przez eGenix.com. Za³±czone pakiety
s± udostêpniane przy u¿yciu eGenix.com Public License albo eGenix.com
Commercial License albo pod innymi licencjami. Nale¿y sprawdziæ
licencje dla poszczególnych podpakietów b±d¼ skontaktowaæ siê z eGenix
bezpo¶rednio w tej sprawie.

%prep
%setup -q -n %{module}-%{version}

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

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
