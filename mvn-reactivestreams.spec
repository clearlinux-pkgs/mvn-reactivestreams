#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-reactivestreams
Version  : 1.0.3
Release  : 1
URL      : https://github.com/reactive-streams/reactive-streams-jvm/archive/v1.0.3.tar.gz
Source0  : https://github.com/reactive-streams/reactive-streams-jvm/archive/v1.0.3.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.0/reactive-streams-1.0.0.jar
Source2  : https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.0/reactive-streams-1.0.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0
Requires: mvn-reactivestreams-data = %{version}-%{release}
Requires: mvn-reactivestreams-license = %{version}-%{release}

%description
# Reactive Streams #
The purpose of Reactive Streams is to provide a standard for asynchronous stream processing with non-blocking backpressure.

%package data
Summary: data components for the mvn-reactivestreams package.
Group: Data

%description data
data components for the mvn-reactivestreams package.


%package license
Summary: license components for the mvn-reactivestreams package.
Group: Default

%description license
license components for the mvn-reactivestreams package.


%prep
%setup -q -n reactive-streams-jvm-1.0.3

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-reactivestreams
cp COPYING %{buildroot}/usr/share/package-licenses/mvn-reactivestreams/COPYING
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/reactivestreams/reactive-streams/1.0.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/reactivestreams/reactive-streams/1.0.0/reactive-streams-1.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/reactivestreams/reactive-streams/1.0.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/reactivestreams/reactive-streams/1.0.0/reactive-streams-1.0.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/reactivestreams/reactive-streams/1.0.0/reactive-streams-1.0.0.jar
/usr/share/java/.m2/repository/org/reactivestreams/reactive-streams/1.0.0/reactive-streams-1.0.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-reactivestreams/COPYING
