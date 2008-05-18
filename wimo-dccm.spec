Summary:	WiMo-DCCM - detect plugged and unplugged USB PocketPC devices
Name:		wimo-dccm
Version:	0.5.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/wimo/%{name}-%{version}.tar.bz2
# Source0-md5:	9a2102103d34f07594f848c08f10d137
URL:		http://www.wimol.org/
BuildRequires:	mono-csharp
BuildRequires:	nant
BuildRequires:	pkgconfig
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Windows Mobile devices support for Linux desktop.

WiMo-DCCM purpose is to detect plugged and unplugged USB PocketPC
devices and creation of PPP connection to them. If device is password
protected it sends password request do DBus to be captured by
gnome-wimo-manager. Signals of connected and disconnected PocketPC
device are send to DBus. Also all connected devices can be listed
throught DBus.

Ideas took from SynCE odccm project.

%prep
%setup -q

%build
nant -D:PREFIX=%{_prefix}  \
	-D:LOCALSTATEDIR=%{_localstatedir} \
	-D:SYSCONFDIR=%{_sysconfdir}

%install
rm -rf $RPM_BUILD_ROOT
nant install \
	-D:DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q haldaemon restart

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/dccm
%attr(755,root,root) %{_libdir}/%{name}/dccm*.sh
%attr(755,root,root) %{_libdir}/%{name}/wimo-serial-chat
%{_libdir}/%{name}/%{name}*
%{_datadir}/hal/information/20thirdparty/20-usb-pocketpc.fdi
