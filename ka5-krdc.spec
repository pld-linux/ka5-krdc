%define		kdeappsver	21.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		krdc
Summary:	krdc
Name:		ka5-%{kaname}
Version:	21.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	70e9b6e1dcd3d6ea629a632a84de33ab
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kbookmarks-devel >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kdnssd-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	libvncserver-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KRDC is a client application that allows you to view or even control
the desktop session on another machine that is running a compatible
server. VNC and RDP is supported.

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
%dir %{_datadir}/kxmlgui5/krdc
%{_datadir}/kxmlgui5/krdc/krdcui.rc
%{_datadir}/metainfo/org.kde.krdc.appdata.xml
%dir %{_libdir}/qt5/plugins/krdc/kcms
%attr(755,root,root) %{_libdir}/qt5/plugins/krdc/kcms/libkcm_krdc_vncplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/krdc/libkrdc_vncplugin.so
%{_datadir}/kservices5/krdc_vnc_config.desktop
%{_datadir}/kservices5/vnc.protocol

%files devel
%defattr(644,root,root,755)
%{_includedir}/krdc
%{_includedir}/krdccore_export.h
%attr(755,root,root) %{_libdir}/libkrdccore.so
