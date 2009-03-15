%define		_state		unstable
%define		orgname		kdevplatform
#%define		svnrev		903434
%define		_kdevelopver	3.9.91

Summary:	kdevplatform
Summary(pl.UTF-8):	kdevplatform
Name:		kde4-kdevplatform
Version:	0.9.91
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{_kdevelopver}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	24de5a242aa1a19adb5f1b09344c13eb
#Patch0:		%{name}-cmake.patch
URL:		http://www.kdevelop.org/
BuildRequires:	apr-devel
BuildRequires:	apr-util-devel
BuildRequires:	automoc4
BuildRequires:	boost-devel
BuildRequires:	commoncpp2-devel
BuildRequires:	phonon-devel
BuildRequires:	subversion-devel
BuildRequires:	zlib-devel
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
%setup -q -n %{orgname}-%{version}
#%patch0 -p1

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

%attr(755,root,root) %{_libdir}/libkdevplatforminterfaces.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdevplatforminterfaces.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformlanguage.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdevplatformlanguage.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformoutputview.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdevplatformoutputview.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformproject.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdevplatformproject.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformshell.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdevplatformshell.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformtestshell.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdevplatformtestshell.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformutil.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdevplatformutil.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformvcs.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdevplatformvcs.so.?
%attr(755,root,root) %{_libdir}/libsublime.so.*.*.*
%attr(755,root,root) %{_libdir}/libsublime.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformveritas.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdevplatformveritas.so.?
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
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_runsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdevsourceformattersettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_uisettings.so
#%attr(755,root,root) %{_libdir}/kde4/kdevbzr.so
#%attr(755,root,root) %{_libdir}/kde4/kdevclassbrowser.so
%attr(755,root,root) %{_libdir}/kde4/kdevcontextbrowser.so
#%attr(755,root,root) %{_libdir}/kde4/kdevcoverage.so
%attr(755,root,root) %{_libdir}/kde4/kdevcvs.so
#%attr(755,root,root) %{_libdir}/kde4/kdevduchainview.so
%attr(755,root,root) %{_libdir}/kde4/kdevexecute.so
%attr(755,root,root) %{_libdir}/kde4/kdevfilemanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevgenericmanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevgit.so
#%attr(755,root,root) %{_libdir}/kde4/kdevhg.so
%attr(755,root,root) %{_libdir}/kde4/kdevkonsoleview.so
%attr(755,root,root) %{_libdir}/kde4/kdevkrossplugin.so
%attr(755,root,root) %{_libdir}/kde4/kdevproblemreporter.so
%attr(755,root,root) %{_libdir}/kde4/kdevprojectmanagerview.so
%attr(755,root,root) %{_libdir}/kde4/kdevquickopen.so
%attr(755,root,root) %{_libdir}/kde4/kdevsnippet.so
%attr(755,root,root) %{_libdir}/kde4/kdevsourceformatter.so
%attr(755,root,root) %{_libdir}/kde4/kdevstandardoutputview.so
%attr(755,root,root) %{_libdir}/kde4/kdevsubversion.so
#%attr(755,root,root) %{_libdir}/kde4/kdevteamwork.so
%attr(755,root,root) %{_libdir}/kde4/kdevvcscommon.so
%attr(755,root,root) %{_libdir}/kde4/kdevappwizard.so
%dir %{_datadir}/apps/kdevstandardoutputview
%{_datadir}/apps/kdevstandardoutputview/kdevstandardoutputview.rc
#%dir %{_datadir}/apps/kdevclassbrowser
#%{_datadir}/apps/kdevclassbrowser/kdevclassbrowser.rc
#%dir %{_datadir}/apps/kdevbzr
#%{_datadir}/apps/kdevbzr/kdevbzr.rc
%dir %{_datadir}/apps/kdevcvs
%{_datadir}/apps/kdevcvs/kdevcvs.rc
#%dir %{_datadir}/apps/kdevduchainview
#%{_datadir}/apps/kdevduchainview/kdevduchainview.rc
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
#%dir %{_datadir}/apps/kdevcoverage
#%{_datadir}/apps/kdevcoverage/kdevcoverage.rc
%dir %{_datadir}/apps/kdevgit
%{_datadir}/apps/kdevgit/kdevgit.rc
#%dir %{_datadir}/apps/kdevhg
#%{_datadir}/apps/kdevhg/kdevhg.rc
#%dir %{_datadir}/apps/kdevteamwork
#%{_datadir}/apps/kdevteamwork/kdevteamwork.rc
%dir %{_datadir}/apps/kdevsourceformatter
%{_datadir}/apps/kdevsourceformatter/kdevsourceformatter.rc
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/servicetypes/kdevelopplugin.desktop
%{_iconsdir}/hicolor/*/actions/*.png
%{_datadir}/apps/kdevappwizard/kdevappwizard.rc
%{_datadir}/apps/kdevappwizard/template_previews/default-kdevelop.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/kdevplatform/*
#%{_libdir}/libkdevplatformeditor.so
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
%{_libdir}/kdevplatform/KDevPlatformConfig.cmake
%{_libdir}/kdevplatform/KDevPlatformConfigVersion.cmake
%{_libdir}/kdevplatform/KDevPlatformTargets.cmake
%{_libdir}/kdevplatform/KDevPlatformTargets-relwithdebinfo.cmake
