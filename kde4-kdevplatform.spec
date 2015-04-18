#
# TODO: Add 'Requires:' for grantlee version with which it is built
#

%define		_state		stable
%define		orgname		kdevplatform
%define		_kdevelopver	4.7.1
%define		kdever		4.8.0
%define		qtver		4.8.0

Summary:	KDevelop Development Platform
Summary(pl.UTF-8):	KDevelop Development Platform
Name:		kde4-kdevplatform
Version:	1.7.1
Release:	2
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{_kdevelopver}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	f6c123d65ae8d5c50944d548c8bc812f
Patch0:		%{name}-boost.patch
URL:		http://www.kdevelop.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.9
BuildRequires:	gettext-tools
BuildRequires:	grantlee-devel
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	libstdc++-devel
BuildRequires:	qjson-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	soprano-devel
BuildRequires:	subversion-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	zlib-devel
Requires:	subversion-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         filterout       -flto

%description
kdevplatform

%description -l pl.UTF-8
kdevplatform

%package devel
Summary:	kdevplatform - header files and development documentation
Summary(pl.UTF-8):	kdevplatform - pliki nagłówkowe i dokumentacja
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{kdever}

%description devel
This package contains header files and development documentation for
kdevplatform.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących kdevplatform.

%prep
%setup -q -n %{orgname}-%{version}

%patch0 -p1

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdevplatform/profiles
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdevfiletemplates/templates

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdev_dbus_socket_transformer
%attr(755,root,root) %{_bindir}/kdev_format_source
%attr(755,root,root) %{_bindir}/kdevplatform_shell_environment.sh
%attr(755,root,root) %{_libdir}/libkdevplatformdebugger.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformdebugger.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformdocumentation.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformdocumentation.so.?
%attr(755,root,root) %{_libdir}/libkdevplatforminterfaces.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatforminterfaces.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformlanguage.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformlanguage.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformoutputview.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformoutputview.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformproject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformproject.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformshell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformshell.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformtests.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformtests.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformutil.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformvcs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformvcs.so.?
%attr(755,root,root) %{_libdir}/libsublime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsublime.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformjsontests.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformjsontests.so.?
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_bgsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_ccsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_envsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_pluginsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdevprojectfilter.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_projectsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdevsourceformattersettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_uisettings.so
%attr(755,root,root) %{_libdir}/kde4/kdevbazaar.so
%attr(755,root,root) %{_libdir}/kde4/kdevclassbrowser.so
%attr(755,root,root) %{_libdir}/kde4/kdevcodeutils.so
%attr(755,root,root) %{_libdir}/kde4/kdevcontextbrowser.so
%attr(755,root,root) %{_libdir}/kde4/kdevcvs.so
%attr(755,root,root) %{_libdir}/kde4/kdevdocumentswitcher.so
%attr(755,root,root) %{_libdir}/kde4/kdevdocumentview.so
%attr(755,root,root) %{_libdir}/kde4/kdevexecute.so
%attr(755,root,root) %{_libdir}/kde4/kdevexecutescript.so
%attr(755,root,root) %{_libdir}/kde4/kdevexternalscript.so
%attr(755,root,root) %{_libdir}/kde4/kdevfilemanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevfiletemplates.so
%attr(755,root,root) %{_libdir}/kde4/kdevgenericmanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevgit.so
%attr(755,root,root) %{_libdir}/kde4/kdevgrepview.so
%attr(755,root,root) %{_libdir}/kde4/kdevkonsoleview.so
%attr(755,root,root) %{_libdir}/kde4/kdevopenwith.so
%attr(755,root,root) %{_libdir}/kde4/kdevpastebin.so
%attr(755,root,root) %{_libdir}/kde4/kdevpatchreview.so
%attr(755,root,root) %{_libdir}/kde4/kdevproblemreporter.so
%attr(755,root,root) %{_libdir}/kde4/kdevprojectdashboard.so
%attr(755,root,root) %{_libdir}/kde4/kdevprojectfilter.so
%attr(755,root,root) %{_libdir}/kde4/kdevprojectmanagerview.so
%attr(755,root,root) %{_libdir}/kde4/kdevquickopen.so
%attr(755,root,root) %{_libdir}/kde4/kdevreviewboard.so
%attr(755,root,root) %{_libdir}/kde4/kdevsnippet.so
%attr(755,root,root) %{_libdir}/kde4/kdevstandardoutputview.so
%attr(755,root,root) %{_libdir}/kde4/kdevsubversion.so
%attr(755,root,root) %{_libdir}/kde4/kdevswitchtobuddy.so
%attr(755,root,root) %{_libdir}/kde4/kdevtemplatemanager_config.so
%attr(755,root,root) %{_libdir}/kde4/kdevtestview.so
%attr(755,root,root) %{_libdir}/kde4/kdevvcschangesviewplugin.so
%attr(755,root,root) %{_libdir}/kde4/kdevappwizard.so
%attr(755,root,root) %{_libdir}/kde4/plasma_kdev_projectfileelement.so
%dir %{_libdir}/kde4/plugins/grantlee
%dir %{_libdir}/kde4/plugins/grantlee/*
%attr(755,root,root) %{_libdir}/kde4/plugins/grantlee/*/kdev_filters.so
%dir %{_libdir}/kde4/imports/org/kde/kdevplatform
%{_libdir}/kde4/imports/org/kde/kdevplatform/qmldir
%attr(755,root,root) %{_libdir}/kde4/imports/org/kde/kdevplatform/libkdevelopdashboarddeclarativeplugin.so
%dir %{_datadir}/apps/kdevplatform
%dir %{_datadir}/apps/kdevplatform/profiles
%dir %{_datadir}/apps/kdevstandardoutputview
%{_datadir}/apps/kdevstandardoutputview/kdevstandardoutputview.rc
%dir %{_datadir}/apps/kdevcodeutils
%{_datadir}/apps/kdevcodeutils/kdevcodeutils.rc
%{_datadir}/apps/kdevcodeutils/templates
%dir %{_datadir}/apps/kdevcvs
%{_datadir}/apps/kdevcvs/kdevcvs.rc
%dir %{_datadir}/apps/kdevclassbrowser
%{_datadir}/apps/kdevclassbrowser/kdevclassbrowser.rc
%dir %{_datadir}/apps/kdevdebugger
%{_datadir}/apps/kdevdebugger/kdevdebuggershellui.rc
%dir %{_datadir}/apps/kdevdocumentswitcher
%{_datadir}/apps/kdevdocumentswitcher/kdevdocumentswitcher.rc
%dir %{_datadir}/apps/kdevdocumentview
%{_datadir}/apps/kdevdocumentview/kdevdocumentview.rc
%dir %{_datadir}/apps/kdevexternalscript
%{_datadir}/apps/kdevexternalscript/kdevexternalscript.rc
%dir %{_datadir}/apps/kdevfiletemplates
%dir %{_datadir}/apps/kdevfiletemplates/templates
%{_datadir}/apps/kdevfiletemplates/kdevfiletemplates.rc
%dir %{_datadir}/apps/kdevgrepview
%{_datadir}/apps/kdevgrepview/kdevgrepview.rc
%dir %{_datadir}/apps/kdevfilemanager
%{_datadir}/apps/kdevfilemanager/kdevfilemanager.rc
%dir %{_datadir}/apps/kdevproblemreporter
%{_datadir}/apps/kdevproblemreporter/kdevproblemreporter.rc
%dir %{_datadir}/apps/kdevprojectmanagerview
%{_datadir}/apps/kdevprojectmanagerview/kdevprojectmanagerview.rc
%dir %{_datadir}/apps/kdevquickopen
%{_datadir}/apps/kdevquickopen/kdevquickopen.rc
%dir %{_datadir}/apps/kdevcontextbrowser
%{_datadir}/apps/kdevcontextbrowser/kdevcontextbrowser.rc
%dir %{_datadir}/apps/kdevsnippet
%{_datadir}/apps/kdevsnippet/kdevsnippet.rc
%dir %{_datadir}/apps/kdevpatchreview
%{_datadir}/apps/kdevpatchreview/kdevpatchreview.rc
%dir %{_datadir}/apps/kdevsession
%{_datadir}/apps/kdevsession/kdevsessionui.rc
%dir %{_datadir}/apps/kdevtestview/
%{_datadir}/apps/kdevtestview/kdevtestview.rc
%{_datadir}/apps/kdevcodegen
%dir %{_datadir}/apps/kdevsourceformatter
%{_datadir}/apps/kdevsourceformatter/kdevsourceformatter.rc
%{_datadir}/config/kdevappwizard.knsrc
%{_datadir}/config/kdevfiletemplates.knsrc
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/servicetypes/kdevelopplugin.desktop
%{_iconsdir}/hicolor/*/actions/*.png
%{_iconsdir}/hicolor/*/apps/*.png
%dir %{_datadir}/apps/kdevappwizard
%{_datadir}/apps/kdevappwizard/kdevappwizard.rc
%dir %{_datadir}/apps/kdevelop
%{_datadir}/apps/kdevelop/*.qml
%{_datadir}/apps/plasma/plasmoids/org.kdevelop.branches

%files devel
%defattr(644,root,root,755)
%{_includedir}/kdevplatform
%{_libdir}/libkdevplatformdebugger.so
%{_libdir}/libkdevplatformdocumentation.so
%{_libdir}/libkdevplatforminterfaces.so
%{_libdir}/libkdevplatformjsontests.so
%{_libdir}/libkdevplatformlanguage.so
%{_libdir}/libkdevplatformoutputview.so
%{_libdir}/libkdevplatformproject.so
%{_libdir}/libkdevplatformshell.so
%{_libdir}/libkdevplatformtests.so
%{_libdir}/libkdevplatformutil.so
%{_libdir}/libkdevplatformvcs.so
%{_libdir}/libsublime.so
%dir %{_libdir}/cmake/kdevplatform
%{_libdir}/cmake/kdevplatform/KDevPlatformConfig.cmake
%{_libdir}/cmake/kdevplatform/KDevPlatformConfigVersion.cmake
%{_libdir}/cmake/kdevplatform/KDevPlatformMacros.cmake
%{_libdir}/cmake/kdevplatform/KDevPlatformTargets.cmake
%{_libdir}/cmake/kdevplatform/KDevPlatformTargets-pld.cmake
