%define		_state		unstable
%define		orgname		kdevplatform
%define		_kdevelopver	4.1.80
%define		kdever		4.5.4
%define		qtver		4.7.0

Summary:	KDevelop Development Platform
Summary(pl.UTF-8):	KDevelop Development Platform
Name:		kde4-kdevplatform
Version:	1.1.80
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{_kdevelopver}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	0553a3bb9e7740ce65cc0b09e342567a
URL:		http://www.kdevelop.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	libstdc++-devel
BuildRequires:	qjson-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	soprano-devel
BuildRequires:	subversion-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	zlib-devel
Requires:	subversion-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdevplatform/profiles

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
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_bgsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_ccsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_envsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_genericprojectmanagersettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_pluginsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_projectsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdevsourceformattersettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_uisettings.so
%attr(755,root,root) %{_libdir}/kde4/kdevclassbrowser.so
%attr(755,root,root) %{_libdir}/kde4/kdevcodeutils.so
%attr(755,root,root) %{_libdir}/kde4/kdevcontextbrowser.so
%attr(755,root,root) %{_libdir}/kde4/kdevcvs.so
%attr(755,root,root) %{_libdir}/kde4/kdevdocumentswitcher.so
%attr(755,root,root) %{_libdir}/kde4/kdevdocumentview.so
%attr(755,root,root) %{_libdir}/kde4/kdevexecute.so
%attr(755,root,root) %{_libdir}/kde4/kdevexternalscript.so
%attr(755,root,root) %{_libdir}/kde4/kdevfilemanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevgenericmanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevgit.so
%attr(755,root,root) %{_libdir}/kde4/kdevgrepview.so
%attr(755,root,root) %{_libdir}/kde4/kdevkonsoleview.so
%attr(755,root,root) %{_libdir}/kde4/kdevopenwith.so
%attr(755,root,root) %{_libdir}/kde4/kdevpastebin.so
%attr(755,root,root) %{_libdir}/kde4/kdevpatchreview.so
%attr(755,root,root) %{_libdir}/kde4/kdevproblemreporter.so
%attr(755,root,root) %{_libdir}/kde4/kdevprojectmanagerview.so
%attr(755,root,root) %{_libdir}/kde4/kdevquickopen.so
%attr(755,root,root) %{_libdir}/kde4/kdevreviewboard.so
%attr(755,root,root) %{_libdir}/kde4/kdevsnippet.so
%attr(755,root,root) %{_libdir}/kde4/kdevstandardoutputview.so
%attr(755,root,root) %{_libdir}/kde4/kdevsubversion.so
%attr(755,root,root) %{_libdir}/kde4/kdevappwizard.so
%dir %{_datadir}/apps/kdevplatform
%dir %{_datadir}/apps/kdevplatform/profiles
%dir %{_datadir}/apps/kdevstandardoutputview
%{_datadir}/apps/kdevstandardoutputview/kdevstandardoutputview.rc
%dir %{_datadir}/apps/kdevcodeutils
%{_datadir}/apps/kdevcodeutils/kdevcodeutils.rc
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
%{_datadir}/apps/kdevcodegen
%dir %{_datadir}/apps/kdevsourceformatter
%{_datadir}/apps/kdevsourceformatter/kdevsourceformatter.rc
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/servicetypes/kdevelopplugin.desktop
%{_iconsdir}/hicolor/*/actions/*.png
%{_iconsdir}/hicolor/*/apps/*.png
%dir %{_datadir}/apps/kdevappwizard
%{_datadir}/apps/kdevappwizard/kdevappwizard.rc
%dir %{_datadir}/apps/kdevappwizard/template_previews
%{_datadir}/apps/kdevappwizard/template_previews/default-kdevelop.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/kdevplatform
%{_libdir}/libkdevplatformdebugger.so
%{_libdir}/libkdevplatformdocumentation.so
%{_libdir}/libkdevplatforminterfaces.so
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
%{_libdir}/cmake/kdevplatform/KDevPlatformTargets-release.cmake
