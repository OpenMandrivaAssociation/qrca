Name:		qrca
Version:	25.08.1
Release:	1
Source0:	https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary:	QR code scanner and generator
URL:		https://invent.kde.org/utilities/qrca
License:	GPL
Group:		Graphical desktop/KDE
BuildSystem:	cmake
BuildRequires:	cmake(ECM)

%description
QR code scanner and generator

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.qrca.desktop
%{_datadir}/applications/org.kde.qrca.wifi.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.qrca.svg
%{_datadir}/metainfo/org.kde.qrca.appdata.xml
