/* Astartup Cookbook @version 0.x
@link    https://github.com/kabuki-starship/astartup.cookbook.git
@file    /_seams/01.release.h
@author  Cale McCollough <https://calemccollough.github.io>
@license Copyright 2014-9 (C) Cale McCollough; all rights reserved (R). This
source code form is covered under the Kabuki Strong Source-available License.
A copy of the license that YOU MUST READ can be found in the readme.md file
in this folder. */

#pragma once
#include <_config.h>

#if SEAM == ASTARTUP_COOKBOOK_RELEASE
#include "_debug.inl"
#else
#include "_release.inl"
#endif

using namespace _;

namespace astartup { namespace cookbook { 
inline const CH1* Release (CH1* seam_log, CH1* seam_end, const CH1* args) {
#if SEAM >= ASTARTUP_COOKBOOK_RELEASE
  TEST_BEGIN;

  PRINT_HEADING ("Testing Foo fun.");

#endif
  return 0;
}
}  //< namespace cookbook
}  //< namespace astartup
