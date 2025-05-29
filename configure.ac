
AC_INIT([foobar], [0.1.0], [])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AC_PROG_CXX
AM_PROG_AR
LT_INIT
AC_CONFIG_FILES([Makefile src/Makefile])
PKG_CHECK_MODULES([ZLIB], [zlib], [], [AC_MSG_ERROR([zlib not found])])
PKG_CHECK_MODULES([FMT], [fmt], [], [AC_MSG_ERROR([fmt library not found])])
AC_OUTPUT
