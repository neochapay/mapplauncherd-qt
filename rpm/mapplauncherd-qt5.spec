# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       mapplauncherd-qt5

# >> macros
# << macros

Summary:    Application launch boosters for Qt5
Version:    1.0.0
Release:    1
Group:      System/Daemons
License:    LGPLv2+
URL:        https://github.com/nemomobile/mapplauncherd-qt/
Source0:    %{name}-%{version}.tar.bz2
Requires:   mapplauncherd >= 4.1.0
Requires:   systemd-user-session-targets
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires(pre):  shadow-utils
BuildRequires:  pkgconfig(libshadowutils)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  mapplauncherd-devel >= 4.1.0

%description
Application launch boosters for Qt5


%package devel
Summary:    Development files for launchable applications
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for creating applications that can be launched
using mapplauncherd.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
mkdir -p %{buildroot}/usr/lib/systemd/user/user-session.target.wants || true
ln -s ../booster-qt5.service %{buildroot}/usr/lib/systemd/user/user-session.target.wants/
# << install post

%pre
groupadd -rf privileged

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%attr(2755, root, privileged) %{_libexecdir}/mapplauncherd/booster-qt5
%{_libdir}/libmdeclarativecache5.so.*
%{_libdir}/systemd/user/booster-qt5.service
%{_libdir}/systemd/user/user-session.target.wants/booster-qt5.service
%{_libdir}/systemd/user/booster-signal.service
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_datadir}/qt5/mkspecs/features/*.prf
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libmdeclarativecache5.so
%{_includedir}/mdeclarativecache5/
# >> files devel
# << files devel
