
AC_INIT([foobar], [0.1.0], [])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AC_PROG_CXX
AM_PROG_AR
LT_INIT
AC_CONFIG_FILES([Makefile src/Makefile])
PKG_CHECK_MODULES([NLOHMANN_JSON], [nlohmann_json], [], [AC_MSG_ERROR([nlohmann_json not found])])
PKG_CHECK_MODULES([ZLIB], [zlib], [], [AC_MSG_ERROR([zlib library not found])])
AC_OUTPUT
