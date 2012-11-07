
require 'fileutils'

task :default do
  puts "Nothing to do. Run `rake -T` to see your options."
end

NAME = 'slab-geoexplorer'
VERSION = '3.0'
GEOEXPLORER_DIR = 'suite/geoexplorer/externals/geoexplorer'
OUTPUT = [
  "BUILD/#{NAME}-#{VERSION}",
  "BUILDROOT/#{NAME}-#{VERSION}*",
  "RPMS/noarch",
  "SOURCES/#{NAME}-#{VERSION}*",
  "SRPMS/*.rpm",
  "tmp/rpm*",
]

desc 'Run the entire process (THIS IS THE ONLY TASK THAT CARES ABOUT DEPENDENCIES!).'
task :all => [
  :clean,
  :update,
  :build,
  :copywar,
  :srctar,
  :rpmbuild
]

desc 'This does a recursive git submodule update.'
task :update do
  sh %{git submodule update --init --recursive}
end

desc 'This builds the suite using maven.'
task :build do
  sh %{cd #{GEOEXPLORER_DIR} ; ant dist war}
end

desc 'This copies the built WAR file to the SOURCES directory.'
task :copywar do
  sh %{cp #{GEOEXPLORER_DIR}/build/geoexplorer.war SOURCES/#{NAME}-#{VERSION}/}
end

desc 'This creates a tarball from the SOURCES directory.'
task :srctar do
  sh %{cd SOURCES ; tar cfz #{NAME}-#{VERSION}.tar.gz #{NAME}-#{VERSION}}
end

desc 'This runs rpmbuild.'
task :rpmbuild do
  sh %{rpmbuild -ba SPECS/#{NAME}.spec}
end

desc 'This removes everything.'
task :clean do
  OUTPUT.each do |glob|
    FileUtils.rm_rf Dir[glob], :verbose => true
  end
end

desc 'This installs the RPM file.'
task :install do
  sh %{sudo yum install RPMS/noarch/#{NAME}-#{VERSION}-1.el6.noarch.rpm}
end

desc 'This uninstalls the RPM file.'
task :uninstall do
  sh %{sudo yum remove #{NAME}}
end
