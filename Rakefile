
task :default do
  puts "Nothing to do. Run `rake -T` to see your options."
end

VERSION = '3.0'
GEOEXPLORER_DIR = 'suite/geoexplorer/externals/geoexplorer'

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
  sh %{cp #{GEOEXPLORER_DIR}/build/geoexplorer.war SOURCES/slab-geoexplorer-#{VERSION}/}
end

desc 'This creates a tarball from the SOURCES directory.'
task :srctar do
  sh %{cd SOURCES ; tar cfz slab-geoexplorer-#{VERSION}.tar.gz slab-geoexplorer-#{VERSION}}
end

desc 'This runs rpmbuild.'
task :rpmbuild do
  sh %{rpmbuild -ba SPECS/slab-geoexplorer.spec}
end

desc 'This removes everything.'
task :clean do
  # TODO
end

desc 'This installs the RPM file.'
task :install do
  sh %{sudo yum install RPMS/noarch/slab-geoexplorer-3.0-1.el6.noarch.rpm}
end

desc 'This uninstalls the RPM file.'
task :uninstall do
  sh %{sudo yum remove slab-geoexplorer}
end

