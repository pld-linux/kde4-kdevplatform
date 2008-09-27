%define		_state		unstable
%define		orgname		kdevplatform
%define		_rel		863954

Summary:	kdevplatform
Summary(pl.UTF-8):	kdevplatform
Name:		kde4-kdevplatform
Version:	4.1.67
Release:	0.%{_rel}.1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/snapshots/%{orgname}-%{_rel}.tar.bz2
# Source0-md5:	78ce8758205ddea291d52a1382cb2051
URL:		http://www.kdevelop.org/
BuildRequires:	commoncpp2-devel
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
%setup -q -n %{orgname}-%{_rel}

%build
mkdir build
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
%attr(755,root,root) %{_bindir}/kdevteamwork_server
%attr(755,root,root) %{_bindir}/lcov_geninfo

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
%attr(755,root,root) %{_libdir}/libkdevplatformutil.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdevplatformutil.so.?
%attr(755,root,root) %{_libdir}/libkdevplatformvcs.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdevplatformvcs.so.?
%attr(755,root,root) %{_libdir}/libsublime.so.*.*.*
%attr(755,root,root) %{_libdir}/libsublime.so.?
%attr(755,root,root) %{_libdir}/libdiff2.so
%attr(755,root,root) %{_libdir}/libdynamictext.so
%attr(755,root,root) %{_libdir}/libkdevplatformveritas.so
%attr(755,root,root) %{_libdir}/libkdevveritascoverage.so
%attr(755,root,root) %{_libdir}/libnetwork.so

%attr(755,root,root) %{_libdir}/kde4/kdevbzr.so
%attr(755,root,root) %{_libdir}/kde4/kdevcoverage.so
%attr(755,root,root) %{_libdir}/kde4/kdevgit.so
%attr(755,root,root) %{_libdir}/kde4/kdevhg.so
%attr(755,root,root) %{_libdir}/kde4/kdevkrossplugin.so
%attr(755,root,root) %{_libdir}/kde4/kdevteamwork.so
%attr(755,root,root) %{_libdir}/kde4/kdevvcscommon.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_bgsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_ccsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_envsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_genericprojectmanagersettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_projectsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_runsettings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_uisettings.so
%attr(755,root,root) %{_libdir}/kde4/kdevclassbrowser.so
%attr(755,root,root) %{_libdir}/kde4/kdevcvs.so
%attr(755,root,root) %{_libdir}/kde4/kdevduchainview.so
%attr(755,root,root) %{_libdir}/kde4/kdevexecute.so
%attr(755,root,root) %{_libdir}/kde4/kdevfilemanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevgenericmanager.so
%attr(755,root,root) %{_libdir}/kde4/kdevkonsoleview.so
%attr(755,root,root) %{_libdir}/kde4/kdevproblemreporter.so
%attr(755,root,root) %{_libdir}/kde4/kdevprojectmanagerview.so
%attr(755,root,root) %{_libdir}/kde4/kdevquickopen.so
%attr(755,root,root) %{_libdir}/kde4/kdevsnippet.so
%attr(755,root,root) %{_libdir}/kde4/kdevstandardoutputview.so
%attr(755,root,root) %{_libdir}/kde4/kdevsubversion.so
%attr(755,root,root) %{_libdir}/kde4/kdevcontextbrowser.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kdevsourceformattersettings.so
%attr(755,root,root) %{_libdir}/kde4/kdevsourceformatter.so
%dir %{_datadir}/apps/kdevstandardoutputview
%{_datadir}/apps/kdevstandardoutputview/kdevstandardoutputview.rc
%dir %{_datadir}/apps/kdevclassbrowser
%{_datadir}/apps/kdevclassbrowser/kdevclassbrowser.rc
%dir %{_datadir}/apps/kdevbzr
%{_datadir}/apps/kdevbzr/kdevbzr.rc
%dir %{_datadir}/apps/kdevcvs
%{_datadir}/apps/kdevcvs/kdevcvs.rc
%dir %{_datadir}/apps/kdevduchainview
%{_datadir}/apps/kdevduchainview/kdevduchainview.rc
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
%dir %{_datadir}/apps/kdevcoverage
%{_datadir}/apps/kdevcoverage/kdevcoverage.rc
%dir %{_datadir}/apps/kdevgit
%{_datadir}/apps/kdevgit/kdevgit.rc
%dir %{_datadir}/apps/kdevhg
%{_datadir}/apps/kdevhg/kdevhg.rc
%dir %{_datadir}/apps/kdevteamwork
%{_datadir}/apps/kdevteamwork/kdevteamwork.rc
%dir %{_datadir}/apps/kdevsourceformatter
%{_datadir}/apps/kdevsourceformatter/kdevsourceformatter.rc

%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/servicetypes/kdevelopplugin.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/kdevplatform
#%{_libdir}/libkdevplatformeditor.so
%{_libdir}/libkdevplatforminterfaces.so
%{_libdir}/libkdevplatformlanguage.so
%{_libdir}/libkdevplatformoutputview.so
%{_libdir}/libkdevplatformproject.so
%{_libdir}/libkdevplatformshell.so
%{_libdir}/libkdevplatformutil.so
%{_libdir}/libkdevplatformvcs.so
%{_libdir}/libsublime.so
%{_datadir}/apps/cmake/modules/FindKDevPlatform.cmake
