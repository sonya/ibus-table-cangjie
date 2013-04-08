# vim:set ts=4
#
# ibus-table-cangjie - The CangJie for IBus Tables.
#
# Copyright (c) 2008-2009 Yu Yuwei <acevery@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

# if not 1, append datestamp to the version number.
m4_define([package_name], [ibus-table-cangjie])
m4_define([ibus_released], [0])
m4_define([ibus_major_version], [1])
m4_define([ibus_minor_version], [1])
m4_define([ibus_micro_version], [0])
m4_define(ibus_maybe_datestamp,
    m4_esyscmd([if test x]ibus_released[ != x1; then date +.%Y%m%d | tr -d '\n\r'; fi]))

m4_define([ibus_version],
    ibus_major_version.ibus_minor_version.ibus_micro_version[]ibus_maybe_datestamp)

AC_INIT([package_name], [ibus_version], [http://code.google.com/p/ibus/issues/entry], [package_name])
AM_INIT_AUTOMAKE([1.10])
AM_MAINTAINER_MODE

# AC_CONFIG_HEADERS([config.h])
AC_CONFIG_MACRO_DIR([m4])

# check python
AM_PATH_PYTHON([2.5])

# check for ibus-table-createdb
PKG_CHECK_MODULES([IBUS_TABLE], [ibus-table >= 1.1.0])
AC_ARG_VAR([IBUS_TABLE_CREATEDB],[[ibus-table-createdb, which generate db]])

AC_PATH_PROG([IBUS_TABLE_CREATEDB],[ibus-table-createdb],
        [AC_MSG_ERROR([ibus-table-createdb not found.])])

# choose table
AC_ARG_ENABLE([cangjie5_hans],
    [AC_HELP_STRING([--enable-cangjie5-hans],
        [Generate CangJie5 Hans Engine])], ,
    [enable_cangjie5_hans=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_CANGJIE5_HANS],[test x"$enable_cangjie5_hans" != x"no"])

AC_ARG_ENABLE([cangjie5_hant],
    [AC_HELP_STRING([--enable-cangjie5-hant],
        [Generate CangJie5 Hant Engine])], ,
    [enable_cangjie5_hant=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_CANGJIE5_HANT],[test x"$enable_cangjie5_hant" != x"no"])

AC_ARG_ENABLE([cangjie3_hans],
    [AC_HELP_STRING([--enable-cangjie3-hans],
        [Generate CangJie3 Hans Engine])], ,
    [enable_cangjie3_hans=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_CANGJIE3_HANS],[test x"$enable_cangjie3_hans" != x"no"])

AC_ARG_ENABLE([cangjie3_hant],
    [AC_HELP_STRING([--enable-cangjie3-hant],
        [Generate CangJie3 Hant Engine])], ,
    [enable_cangjie3_hant=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_CANGJIE3_HANT],[test x"$enable_cangjie3_hant" != x"no"])

AC_ARG_ENABLE([quick5],
    [AC_HELP_STRING([--enable-quick5],
        [Generate Quick5 Engine])], ,
    [enable_quick5=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_QUICK5],[test x"$enable_quick5" != x"no"])

AC_ARG_ENABLE([quick3],
    [AC_HELP_STRING([--enable-quick3],
        [Generate Quick3 Engine])], ,
    [enable_quick3=yes])

AM_CONDITIONAL([IBUS_TABLE_BUILD_QUICK3],[test x"$enable_quick3" != x"no"])

# OUTPUT files
AC_CONFIG_FILES(Makefile
icons/Makefile
tables/Makefile
m4/Makefile
ibus-table-cangjie.spec
)

AC_OUTPUT

AC_MSG_RESULT([
Build options:
  Version                   $VERSION
  Install prefix            $prefix
  Build CangJie3 Hans       $enable_cangjie3_hans
  Build CangJie3 Hant       $enable_cangjie3_hant
  Build CangJie5 Hans       $enable_cangjie5_hans
  Build CangJie5 Hant       $enable_cangjie5_hant
  Build Quick3              $enable_quick3
  Build Quick5              $enable_quick5
])

