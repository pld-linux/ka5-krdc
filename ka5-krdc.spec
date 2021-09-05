%define		kdeappsver	21.08.1
%define		kframever	5.25.0
%define		qtver		5.14.0
%define		kaname		krdc
Summary:	krdc
Name:		ka5-%{kaname}
Version:	21.08.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1ac78accbf204016bf0ce37cfafb22f0
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.0
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kbookmarks-devel >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kdnssd-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	libssh-devel
BuildRequires:	libvncserver-devel >= 0.9
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5Gui >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	kf5-kbookmarks >= %{kframever}
Requires:	kf5-kcmutils >= %{kframever}
Requires:	kf5-kcompletion >= %{kframever}
Requires:	kf5-kconfig >= %{kframever}
Requires:	kf5-kconfigwidgets >= %{kframever}
Requires:	kf5-kcoreaddons >= %{kframever}
Requires:	kf5-kdnssd >= %{kframever}
Requires:	kf5-ki18n >= %{kframever}
Requires:	kf5-knotifications >= %{kframever}
Requires:	kf5-knotifyconfig >= %{kframever}
Requires:	kf5-kservice >= %{kframever}
Requires:	kf5-kwallet >= %{kframever}
Requires:	kf5-kwidgetsaddons >= %{kframever}
Requires:	kf5-kwindowsystem >= %{kframever}
Requires:	kf5-kxmlgui >= %{kframever}
Requires:	libvncserver >= 0.9
Suggests:	freerdp2-x11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KRDC is a client application that allows you to view or even control
the desktop session on another machine that is running a compatible
server. VNC and RDP is supported.

%description -l pl.UTF-8
KRDC jest aplikacją kliencką, która pozwala oglądać a nawet
kontrolować sesję desktopową na zdalnej maszynie, na której jest
uruchomiony kompatybilny serwer. Wspierane są VNC i RDP.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DFREERDP_EXECUTABLE:PATH=/usr/bin/xfreerdp \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krdc
%attr(755,root,root) %{_libdir}/libkrdccore.so.*.*.*
%ghost %{_libdir}/libkrdccore.so.5
%dir %{_libdir}/qt5/plugins/krdc
%attr(755,root,root) %{_libdir}/qt5/plugins/krdc/libkrdc_testplugin.so
%{_desktopdir}/org.kde.krdc.desktop
%{_datadir}/config.kcfg/krdc.kcfg
%{_datadir}/metainfo/org.kde.krdc.appdata.xml
%dir %{_libdir}/qt5/plugins/krdc/kcms
%attr(755,root,root) %{_libdir}/qt5/plugins/krdc/kcms/libkcm_krdc_vncplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krdc/libkrdc_vncplugin.so
%{_datadir}/kservices5/krdc_vnc_config.desktop
%attr(755,root,root) %{_libdir}/qt5/plugins/krdc/kcms/libkcm_krdc_rdpplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krdc/libkrdc_rdpplugin.so
%{_datadir}/kservices5/ServiceMenus/smb2rdc.desktop
%{_datadir}/kservices5/krdc_rdp_config.desktop
%{_datadir}/kservicetypes5/krdc_plugin.desktop
%{_datadir}/qlogging-categories5/krdc.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/krdc
%{_includedir}/krdccore_export.h
%attr(755,root,root) %{_libdir}/libkrdccore.so
