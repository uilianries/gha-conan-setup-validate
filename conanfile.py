from conan import ConanFile
from conan.tools.gnu import Autotools
from conan.tools.layout import basic_layout
from conan.tools.microsoft import is_msvc


class foobarConan(ConanFile):
    name = "foobar"
    version = "0.1.0"
    package_type = "library"
    win_bash = True
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    requires = "nlohmann_json/3.12.0", "zlib/1.3.1"
    exports_sources = "configure.ac", "Makefile.am", "src/*"
    generators = "AutotoolsToolchain", "PkgConfigDeps"
    implements = ["auto_shared_fpic"]

    def layout(self):
        basic_layout(self)

    def build_requirements(self):
        self.tool_requires("libtool/2.4.7")
        if not self.conf.get("tools.gnu:pkg_config", check_type=str):
            self.tool_requires("pkgconf/[>=2.2 <3]")
        if self.settings_build.os == "Windows":
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
