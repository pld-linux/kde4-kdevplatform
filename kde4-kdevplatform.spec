%define		_state		unstable
%define		orgname		kdevplatform
%define		svnrev		979473
%define		_kdevelopver	3.9.91
%define		_kdever		4.2.0
%define		_qtver		4.4

Summary:	KDevelop Development Platform
Summary(pl.UTF-8):	KDevelop Development Platform
Name:		kde4-kdevplatform
Version:	0.9.93
Release:	0.%{svnrev}.1
License:	GPL
Group:		X11/Development/Tools
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{_kdevelopver}/src/%{orgname}-%{version}.tar.bz2
Source0:	ftp://ftp.kde.org/pub/kde/snapshots/%{orgname}-%{svnrev}.tar.bz2
# Source0-md5:	0a91173e6f46bab59e0ecc196ed5bb88
Patch0:		%{name}-codegen.patch
#Patch0:		%{name}-cmake.patch
URL:		http://www.kdevelop.org/
BuildRequires:	rpm-build
BuildRequires:	libstdc++-devel
BuildRequires:	kde4-kdelibs-devel >= %{_kdever}
BuildRequires:	QtCore-devel >= %{_qtver}
BuildRequires:	QtDBus-devel >= %{_qtver}
BuildRequires:	QtDesigner-devel >= %{_qtver}
BuildRequires:	QtTest-devel >= %{_qtver}
BuildRequires:	QtSvg-devel >= %{_qtver}
BuildRequires:	QtNetwork-devel >= %{_qtver}
BuildRequires:	Qt3Support-devel >= %{_qtver}
BuildRequires:	QtGui-devel >= %{_qtver}
BuildRequires:	apr-devel
BuildRequires:	apr-util-devel
BuildRequires:	automoc4
BuildRequires:	boost-devel
BuildRequires:	perl-base
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	phonon-devel
BuildRequires:	subversion-devel
BuildRequires:	zlib-devel
BuildRequires:	glibc-devel
BuildRequires:	libgcc
Requires:	kde4-kdelibs-libs >= %{_kdever}
Requires:	QtCore >= %{_qtver}
Requires:	QtDBus >= %{_qtver}
Requires:	QtDesigner >= %{_qtver}
Requires:	QtTest >= %{_qtver}
Requires:	QtSvg >= %{_qtver}
Requires:	QtNetwork >= %{_qtver}
Requires:	Qt3Support >= %{_qtver}
Requires:	QtGui >= %{_qtver}
Requires:	apr
Requires:	apr-util
Requires:	glibc
Requires:	libgcc
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

%description devel
This package contains header files and development documentation for
kdevplatform.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących kdevplatform.

%prep
%setup -q -n %{orgname}-%{svnrev}
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kdevteamwork_server
#%attr(755,root,root) %{_bindir}/lcov_geninfo

%attr(755,root,root) %{_libdir}/libkdevplatformdebugger.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformdebugger.so.?
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
%attr(755,root,root) %{_libdir}/libkdevplatformtestshell.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformtestshell.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformutil.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformvcs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformvcs.so.?
%attr(755,root,root) %{_libdir}/libsublime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsublime.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformveritas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdevplatformveritas.so.?

#%attr(755,root,root) %{_libdir}/libkdevveritascoverage.so
#%attr(755,root,root) %{_libdir}/libkdevteamwork_diff2.so
#%attr(755,root,root) %{_libdir}/libkdevteamwork_dynamictext.so
#%attr(755,root,root) %{_libdir}/libkdevteamwork_network.so

%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_bgsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_ccsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_envsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_genericprojectmanagersettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_pluginsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_projectsettings.so
#%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_runsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdevsourceformattersettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_uisettings.so
%attr(755,root,root) %{_libdir}/kde4/kdevclassbrowser.so
%attr(755,root,root) %{_libdir}/kde4/kdevcontextbrowser.so
%attr(755,root,root) %{_libdir}/kde4/kdevcvs.so
%attr(755,root,root) %{_libdir}/kde4/kdevdocumentswitcher.so
%attr(755,root,root) %{_libdir}/kde4/kdevexecute.so
%attr(755,root,root) %{_libdir}/kde4/kdevfilemanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevgenericmanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevgit.so
%attr(755,root,root) %{_libdir}/kde4/kdevkonsoleview.so
#%attr(755,root,root) %{_libdir}/kde4/kdevkrossplugin.so
%attr(755,root,root) %{_libdir}/kde4/kdevmercurial.so
%attr(755,root,root) %{_libdir}/kde4/kdevproblemreporter.so
%attr(755,root,root) %{_libdir}/kde4/kdevprojectmanagerview.so
%attr(755,root,root) %{_libdir}/kde4/kdevquickopen.so
%attr(755,root,root) %{_libdir}/kde4/kdevsnippet.so
%attr(755,root,root) %{_libdir}/kde4/kdevsourceformatter.so
%attr(755,root,root) %{_libdir}/kde4/kdevstandardoutputview.so
%attr(755,root,root) %{_libdir}/kde4/kdevsubversion.so

#%attr(755,root,root) %{_libdir}/kde4/kdevteamwork.so

#%attr(755,root,root) %{_libdir}/kde4/kdevvcscommon.so
%attr(755,root,root) %{_libdir}/kde4/kdevappwizard.so
%dir %{_datadir}/apps/kdevstandardoutputview
%{_datadir}/apps/kdevstandardoutputview/kdevstandardoutputview.rc
%dir %{_datadir}/apps/kdevcvs
%{_datadir}/apps/kdevcvs/kdevcvs.rc
%dir %{_datadir}/apps/kdevclassbrowser
%{_datadir}/apps/kdevclassbrowser/kdevclassbrowser.rc
%dir %{_datadir}/apps/kdevdebugger
%{_datadir}/apps/kdevdebugger/kdevdebuggershellui.rc
%dir %{_datadir}/apps/kdevdocumentswitcher
%{_datadir}/apps/kdevdocumentswitcher/kdevdocumentswitcher.rc
%dir %{_datadir}/apps/kdevmercurial
%{_datadir}/apps/kdevmercurial/kdevmercurial.rc
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
%dir %{_datadir}/apps/kdevgit
%{_datadir}/apps/kdevgit/kdevgit.rc

%{_datadir}/apps/kdevcodegen

#%dir %{_datadir}/apps/kdevhg
#%{_datadir}/apps/kdevhg/kdevhg.rc
#%dir %{_datadir}/apps/kdevteamwork
#%{_datadir}/apps/kdevteamwork/kdevteamwork.rc

%dir %{_datadir}/apps/kdevsourceformatter
%{_datadir}/apps/kdevsourceformatter/kdevsourceformatter.rc
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/servicetypes/kdevelopplugin.desktop
%{_iconsdir}/hicolor/*/actions/*.png
%dir %{_datadir}/apps/kdevappwizard
%{_datadir}/apps/kdevappwizard/kdevappwizard.rc
%dir %{_datadir}/apps/kdevappwizard/template_previews
%{_datadir}/apps/kdevappwizard/template_previews/default-kdevelop.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/kdevplatform
%{_libdir}/libkdevplatformdebugger.so
%{_libdir}/libkdevplatforminterfaces.so
%{_libdir}/libkdevplatformlanguage.so
%{_libdir}/libkdevplatformoutputview.so
%{_libdir}/libkdevplatformproject.so
%{_libdir}/libkdevplatformshell.so
%{_libdir}/libkdevplatformtestshell.so
%{_libdir}/libkdevplatformutil.so
%{_libdir}/libkdevplatformvcs.so
%{_libdir}/libkdevplatformveritas.so
%{_libdir}/libsublime.so
%{_datadir}/apps/cmake/modules/FindKDevPlatform.cmake
%dir %{_libdir}/cmake/kdevplatform
%{_libdir}/cmake/kdevplatform/KDevPlatformConfig.cmake
%{_libdir}/cmake/kdevplatform/KDevPlatformConfigVersion.cmake
%{_libdir}/cmake/kdevplatform/KDevPlatformMacros.cmake
%{_libdir}/cmake/kdevplatform/KDevPlatformTargets.cmake
%{_libdir}/cmake/kdevplatform/KDevPlatformTargets-relwithdebinfo.cmake
