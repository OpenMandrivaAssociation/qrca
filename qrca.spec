Name:		qrca
Version:	25.08.2
Release:	1
Source0:	https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary:	QR code scanner and generator
URL:		https://invent.kde.org/utilities/qrca
License:	GPL
Group:		Graphical desktop/KDE
BuildSystem:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Prison)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6NetworkManagerQt)

%description
QR code scanner and generator

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.qrca.desktop
%{_datadir}/applications/org.kde.qrca.wifi.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.qrca.svg
%{_datadir}/metainfo/org.kde.qrca.appdata.xml
