from conan import ConanFile
from conan.tools.gnu import Autotools
from conan.tools.layout import basic_layout


class foobarConan(ConanFile):
    name = "foobar"
    version = "0.1.0"
    package_type = "library"
    win_bash = True
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    requires = "fmt/11.2.0", "zlib/1.3.1"
    exports_sources = "configure.ac", "Makefile.am", "src/*"
    generators = "AutotoolsToolchain", "PkgConfigDeps"
    implements = ["auto_shared_fpic"]

    def layout(self):
        basic_layout(self)

    def build_requirements(self):
        if self.settings.os == "Windows":
            self.tool_requires("libtool/2.4.7")
            self.win_bash = True
            if not self.conf.get("tools.microsoft.bash:path", check_type=str):
                self.tool_requires("msys2/cci.latest")

    def build(self):
        autotools = Autotools(self)
        autotools.autoreconf()
        autotools.configure()
        autotools.make()

    def package(self):
        autotools = Autotools(self)
        autotools.install()

    def package_info(self):
        self.cpp_info.libs = ["foobar"]
